#!/usr/bin/env python3
"""Build script to compile feishu-sender to binary."""
import subprocess
import sys
import shutil
from pathlib import Path


def main():
    print("Building feishu-sender binary...")

    # Clean up previous build
    dist_path = Path("dist")
    if dist_path.exists():
        shutil.rmtree(dist_path)

    # Build binary
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--name", "feishu-sender",
        "--clean",
        "--distpath", "dist/bin",
        "--paths", "src",
        "src/cli.py"
    ]
    result = subprocess.run(cmd)
    if result.returncode != 0:
        return result.returncode

    # Copy additional files
    print("Copying additional files...")

    # Copy SKILL.md
    shutil.copy("doc/output/SKILL.md", "dist/SKILL.md")

    # Copy config files
    shutil.copy("tests/testfile/config.test.json", "dist/bin/config.json")
    shutil.copy("doc/output/config.example.json", "dist/bin/config.example.json")

    print("Build complete! The results are available in: dist/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
