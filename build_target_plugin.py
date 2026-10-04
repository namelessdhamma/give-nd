#!/usr/bin/env python3
import argparse
import hashlib
import json
import pathlib
import re

SECRET_PATTERNS = [
    re.compile(r'(?i)(api[_-]?key|access[_-]?token|refresh[_-]?token|client[_-]?secret|private[_-]?key|password)\s*[:=]\s*["\'][^"\']{8,}'),
    re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    re.compile(r'\b(?:sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AIza[0-9A-Za-z_-]{20,}|xox[baprs]-[A-Za-z0-9-]{10,})\b'),
]
LINEAR_URL = re.compile(r'https://linear\.app/namelessdhamma/issue/(NAM-\d+)(?:/[^\s"\'<>]+)?')
PLACEHOLDER = re.compile(r'\$\{[A-Z0-9_]+\}')
SKILL_URI = re.compile(r'skills://plugins/[A-Za-z0-9._-]+/[A-Za-z0-9._-]+')
SUPPORTED_BUNDLE_SCHEMAS = {"ND_PLUGIN_SOURCE_BUNDLE_v1"}


def fail(msg):
    raise SystemExit("FAIL: " + msg)


def has_placeholder(value):
    return isinstance(value, str) and PLACEHOLDER.search(value) is not None


def resolved_value(value):
    return isinstance(value, str) and value != "" and not has_placeholder(value)


def bundle_identity(src):
    schema = src.get("schema")
    if schema in SUPPORTED_BUNDLE_SCHEMAS:
        name = src.get("name")
        version = src.get("version")
        release = src.get("current_release_id")
    elif isinstance(src.get("plugin"), dict):
        # Backward-compatible read path for historical transfer bundles only.
        plugin = src["plugin"]
        name = plugin.get("name")
        version = plugin.get("version")
        release = plugin.get("current_release_id")
    else:
        fail("unsupported plugin source bundle schema")

    if not name:
        fail("plugin source bundle has no plugin name")
    if not isinstance(src.get("contents"), dict) or not src["contents"]:
        fail("plugin source bundle has no text contents")
    return name, version, release


def iter_literal_bindings(binding):
    for item in binding.get("literal_replacements", []):
        if isinstance(item, dict) and item.get("source"):
            yield item["source"], item.get("target")

    for item in binding.get("semantic_workspaces", {}).values():
        if isinstance(item, dict) and item.get("source"):
            yield item["source"], item.get("target")


def validate_required_bindings(original, binding):
    missing = []

    for source_id, item in binding.get("navigator_rebind", {}).items():
        if not isinstance(item, dict):
            continue

        source_url_marker = f"/issue/{source_id}"
        source_id_used = source_id in original
        source_url_used = source_url_marker in original

        if source_id_used and not resolved_value(item.get("target_identifier")):
            missing.append(f"{source_id}:target_identifier")
        if source_url_used and not resolved_value(item.get("target_url")):
            missing.append(f"{source_id}:target_url")

    for source, target in iter_literal_bindings(binding):
        if isinstance(source, str) and source and source in original and not resolved_value(target):
            missing.append(f"literal:{source}")

    if missing:
        fail("plugin-local target bindings unresolved: " + ", ".join(sorted(set(missing))))


def replacements(binding):
    out = []
    for source, target in iter_literal_bindings(binding):
        if isinstance(source, str) and source and resolved_value(target):
            out.append((source, target))
    return sorted(out, key=lambda x: len(x[0]), reverse=True)


def apply_bindings(text, binding):
    nav = binding.get("navigator_rebind", {})

    def repl_url(match):
        item = nav.get(match.group(1))
        if isinstance(item, dict) and resolved_value(item.get("target_url")):
            return item["target_url"]
        return match.group(0)

    text = LINEAR_URL.sub(repl_url, text)

    for source_id, item in sorted(nav.items(), key=lambda kv: len(kv[0]), reverse=True):
        if isinstance(item, dict) and resolved_value(item.get("target_identifier")):
            text = text.replace(source_id, item["target_identifier"])

    for old, new in replacements(binding):
        text = text.replace(old, new)

    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source_bundle")
    ap.add_argument("binding_map")
    ap.add_argument("output_dir")
    args = ap.parse_args()

    src = json.loads(pathlib.Path(args.source_bundle).read_text(encoding="utf-8"))
    bm = json.loads(pathlib.Path(args.binding_map).read_text(encoding="utf-8"))

    if bm.get("schema") != "ND_TARGET_BINDING_MAP_v3":
        fail("binding map must use ND_TARGET_BINDING_MAP_v3")

    name, source_version, source_release = bundle_identity(src)
    contents = src["contents"]
    original = json.dumps(contents, ensure_ascii=False)

    if any(p.search(original) for p in SECRET_PATTERNS):
        fail("source bundle contains secret-like literal; review required")

    # Staged installation is intentionally partial. Only bindings actually
    # referenced by this plugin must already be resolved.
    validate_required_bindings(original, bm)

    out = pathlib.Path(args.output_dir) / name
    out.mkdir(parents=True, exist_ok=True)

    changed = []
    before_uris = sorted(set(SKILL_URI.findall(original)))

    for rel, file_content in contents.items():
        if not isinstance(rel, str) or not isinstance(file_content, str):
            fail("plugin contents must be UTF-8 text path -> string entries")

        new = apply_bindings(file_content, bm)

        if any(p.search(new) for p in SECRET_PATTERNS):
            fail("target file contains secret-like literal: " + rel)
        if PLACEHOLDER.search(new):
            fail("unresolved placeholder remains in target file: " + rel)

        p = out / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(new, encoding="utf-8")
        if new != file_content:
            changed.append(rel)

    combined = "\n".join(
        p.read_text(encoding="utf-8", errors="ignore")
        for p in out.rglob("*")
        if p.is_file()
    )

    if "linear.app/namelessdhamma/issue/NAM-" in combined:
        fail("source Linear executable URL remains after target build")

    after_uris = sorted(set(SKILL_URI.findall(combined)))
    if before_uris != after_uris:
        fail("stable skills:// identity set changed during provider rebinding")

    report = {
        "plugin": name,
        "source_bundle_schema": src.get("schema"),
        "source_plugin_version": source_version,
        "source_release_id": source_release,
        "changed_files": sorted(changed),
        "file_count": len(contents),
        "skills_uri_count": len(after_uris),
        "output_sha256": hashlib.sha256(combined.encode("utf-8")).hexdigest(),
        "status": "BUILT_PROVIDER_REBIND_ONLY",
    }
    (out / "ND_TARGET_BUILD_REPORT.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
