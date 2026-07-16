import tempfile
from pathlib import Path
from parser import read_file, detect_content_type

# Path to test files
TESTFILE_DIR = Path(__file__).parent / "testfile"


def test_read_file():
    # Test with real text file
    content = read_file(TESTFILE_DIR / "text_example.txt")
    assert content.strip() == "这个一个测试消息"


def test_read_file_with_base_dir():
    # Use testfile dir as base_dir, read just the filename
    content = read_file("text_example.txt", TESTFILE_DIR)
    assert content.strip() == "这个一个测试消息"


def test_read_file_prefer_absolute_path():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create two files with same name in different locations
        other_dir = Path(tmpdir)
        other_file = other_dir / "text_example.txt"
        with open(other_file, "w", encoding="utf-8") as f:
            f.write("from other dir")

        # Should prefer absolute path even when base_dir is provided
        assert read_file(other_file, TESTFILE_DIR) == "from other dir"


def test_detect_content_type_text():
    # Use real text file content
    content = read_file(TESTFILE_DIR / "text_example.txt")
    assert detect_content_type(content) == "text"


def test_detect_content_type_card():
    # Use real card json file
    content = read_file(TESTFILE_DIR / "card_example.json")
    assert detect_content_type(content) == "card"


def test_detect_content_type_md_by_extension():
    # Test with .md file path
    assert detect_content_type("any content", TESTFILE_DIR / "report_example.md") == "card"


def test_detect_content_type_non_md_extension():
    # Test with .txt file path
    content = read_file(TESTFILE_DIR / "text_example.txt")
    assert detect_content_type(content, TESTFILE_DIR / "text_example.txt") == "text"


def test_read_all_example_files():
    # Test reading all example files
    assert read_file(TESTFILE_DIR / "text_example.txt") != ""
    assert read_file(TESTFILE_DIR / "card_example.json") != ""
    assert read_file(TESTFILE_DIR / "report_example.md") != ""
