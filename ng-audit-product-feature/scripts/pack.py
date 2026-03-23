#!/usr/bin/env python3
"""Pack target project into context file for auditing.

Usage:
    python scripts/pack.py /path/to/project
    python scripts/pack.py /path/to/project --name my-project

Output: output/context.xml (repomix packed file)

Requirements: repomix (npm install -g repomix)
"""

import argparse
import os
import shutil
import subprocess
import sys


def find_repomix():
    """Find repomix binary, install if missing."""
    if shutil.which("repomix"):
        return "repomix"

    # Try npx fallback
    if shutil.which("npx"):
        return "npx repomix"

    print("Error: repomix not found. Install with: npm install -g repomix")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Pack project for audit")
    parser.add_argument("project_path", help="Path to project to audit")
    parser.add_argument("--name", default=None, help="Project name (default: directory name)")
    args = parser.parse_args()

    project_path = os.path.abspath(args.project_path)
    project_name = args.name or os.path.basename(project_path)
    output_dir = "output"
    output_file = os.path.join(output_dir, "context.xml")

    if not os.path.isdir(project_path):
        print(f"Error: {project_path} is not a directory")
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)

    print(f"Project : {project_name}")
    print(f"Path    : {project_path}")
    print(f"Output  : {output_file}")
    print()

    repomix = find_repomix()

    cmd = (
        f"{repomix}"
        f" --input {project_path}"
        f" --output {output_file}"
        f' --ignore "node_modules,dist,.git,*.lock,*.log,coverage,.env*"'
        f' --include "**/*.md,**/*.ts,**/*.js,**/*.py,**/*.json,src/**,docs/**,app/**"'
    )

    result = subprocess.run(cmd, shell=True)

    if result.returncode != 0:
        print("Error: repomix failed")
        sys.exit(1)

    print()
    print(f"Done. Context saved to {output_file}")
    print(f"Now run: claude --add-dir {project_path}")


if __name__ == "__main__":
    main()
