#!/usr/bin/env python3
"""Safely install the canonical AI DEV TEAM core into an existing project."""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy AGENTS.md and .agents/ into a project without overwriting files."
    )
    parser.add_argument(
        "--target",
        required=True,
        help="Existing project root where AI DEV TEAM will be installed.",
    )
    parser.add_argument(
        "--source",
        default=str(Path(__file__).resolve().parents[1]),
        help="AI_DEV_TEAM repository root (defaults to this script's repository).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned actions without writing files.",
    )
    parser.add_argument(
        "--skip-conflicts",
        action="store_true",
        help="Keep conflicting destination files and copy only missing files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = Path(args.source).expanduser().resolve()
    target = Path(args.target).expanduser().resolve()

    if not source.is_dir():
        print(f"ERROR: source directory does not exist: {source}", file=sys.stderr)
        return 2
    if not target.is_dir():
        print(f"ERROR: target must be an existing project directory: {target}", file=sys.stderr)
        return 2
    if source == target or source in target.parents:
        print("ERROR: target cannot be the AI_DEV_TEAM repository or a directory inside it.", file=sys.stderr)
        return 2

    canonical = [source / "AGENTS.md", source / ".agents"]
    missing_sources = [path for path in canonical if not path.exists()]
    if missing_sources:
        print("ERROR: incomplete AI_DEV_TEAM source: " + ", ".join(map(str, missing_sources)), file=sys.stderr)
        return 2

    files: list[tuple[Path, Path]] = []
    for item in canonical:
        if item.is_file():
            files.append((item, target / item.name))
        else:
            for child in sorted(item.rglob("*")):
                if child.is_symlink():
                    print(f"ERROR: symbolic links are not supported: {child}", file=sys.stderr)
                    return 2
                if child.is_file():
                    files.append((child, target / child.relative_to(source)))

    conflicts: list[tuple[Path, Path]] = []
    pending: list[tuple[Path, Path]] = []
    identical = 0

    for src, dest in files:
        if dest.exists():
            if not dest.is_file():
                conflicts.append((src, dest))
            elif src.read_bytes() == dest.read_bytes():
                identical += 1
            else:
                conflicts.append((src, dest))
        else:
            pending.append((src, dest))

    if conflicts and not args.skip_conflicts:
        print("ERROR: conflicts detected. No files were copied.", file=sys.stderr)
        for _, dest in conflicts:
            print(f"  CONFLICT: {dest}", file=sys.stderr)
        print("Review and merge these files manually, or rerun with --skip-conflicts to copy only missing files.", file=sys.stderr)
        return 3

    for src, dest in pending:
        print(f"COPY  {src.relative_to(source)} -> {dest}")
    for _, dest in conflicts:
        print(f"KEEP  {dest} (conflict; not overwritten)")
    print(f"SKIP  {identical} identical file(s)")

    if args.dry_run:
        print("DRY RUN: no files were changed.")
        return 0

    for src, dest in pending:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)

    print(f"AI DEV TEAM core installed. Copied {len(pending)} file(s); kept {len(conflicts)} conflict(s).")
    print("Next: consult docs/PROJECT-BOOTSTRAP.md and prompts/01-configure-assistant.md in the AI_DEV_TEAM source repository.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
