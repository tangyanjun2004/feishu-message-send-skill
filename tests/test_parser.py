import tempfile
from pathlib import Path
from parser import read_file, detect_content_type


def test_read_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.txt"
        test_content = "Hello Feishu"
        with open(test_file, "w") as f:
            f.write(test_content)
        assert read_file(test_file) == test_content


def test_detect_content_type_text():
    assert detect_content_type("plain text") == "text"


def test_detect_content_type_card():
    json_content = '{"card": {"elements": []}}'
    assert detect_content_type(json_content) == "card"


def test_detect_content_type_md_by_extension():
    # Markdown file by extension should return card
    assert detect_content_type("any content", "test.md") == "card"
    assert detect_content_type("any content", "test.MD") == "card"


def test_detect_content_type_non_md_extension():
    # Non-markdown file should rely on content detection
    assert detect_content_type("plain text", "test.txt") == "text"
