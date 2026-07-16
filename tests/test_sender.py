#!/usr/bin/env python3
"""Run real sender tests with config.test.json."""
import json
import sys
from pathlib import Path
import pytest

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from config import load_config
from sender import send_message
from parser import read_file

# Path to test files
TESTFILE_DIR = Path(__file__).parent / "testfile"


def test_sender_import():
    """Test that sender module can be imported."""
    assert send_message is not None


def test_sender_read_config():
    """Test reading config with BASE_DIR."""
    config = load_config(TESTFILE_DIR / "config.test.json")
    assert "APP_ID" in config
    assert "APP_SECRET" in config
    assert "RECEIVE_ID" in config
    assert "BASE_DIR" in config


def test_sender_read_all_test_files():
    """Test reading all test files with parser."""
    assert read_file(TESTFILE_DIR / "text_example.txt") != ""
    assert read_file(TESTFILE_DIR / "card_example.json") != ""
    assert read_file(TESTFILE_DIR / "report_example.md") != ""


def run_real_send(test_name: str, file_path: str, msg_type: str):
    """Run real send (not run by pytest by default)."""
    print(f"\n{'='*60}")
    print(f"Test: {test_name}")
    print(f"File: {file_path}")
    print(f"Type: {msg_type}")
    print('='*60)

    try:
        config = load_config(TESTFILE_DIR / "config.test.json")
        content = read_file(TESTFILE_DIR / file_path)
        result = send_message(
            config["APP_ID"],
            config["APP_SECRET"],
            config["RECEIVE_ID"],
            content,
            msg_type
        )
        print(f"Success! Response code: {result.get('code')}, msg: {result.get('msg')}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    results = []

    # Test 1: card_example.json as card
    results.append(("card_example.json (card)", run_real_send(
        "card_example.json as card",
        "card_example.json",
        "card"
    )))

    # Test 2: report_example.md as card
    results.append(("report_example.md (card)", run_real_send(
        "report_example.md as card",
        "report_example.md",
        "card"
    )))

    # Test 3: text_example.txt as text
    results.append(("text_example.txt (text)", run_real_send(
        "text_example.txt as text",
        "text_example.txt",
        "text"
    )))

    # Test 4: report_example.md as text
    results.append(("report_example.md (text)", run_real_send(
        "report_example.md as text",
        "report_example.md",
        "text"
    )))

    # Summary
    print(f"\n{'='*60}")
    print("Summary:")
    print('='*60)
    for name, success in results:
        status = "PASS" if success else "FAIL"
        print(f"{status}: {name}")

    return 0 if all(r[1] for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
