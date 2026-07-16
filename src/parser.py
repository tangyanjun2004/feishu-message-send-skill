import json
from pathlib import Path


def read_file(file_path: Path | str, base_dir: Path | str | None = None) -> str:
    """Read content from file.

    Args:
        file_path: Path to the file (absolute or relative)
        base_dir: Optional base directory. If provided and file_path doesn't exist,
                  try to join base_dir with file_path.
    """
    path = Path(file_path)
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    if base_dir:
        base_path = Path(base_dir)
        joined_path = base_path / path
        if joined_path.exists():
            with open(joined_path, "r", encoding="utf-8") as f:
                return f.read()
    raise FileNotFoundError(f"File not found: {file_path}")


def detect_content_type(content: str, file_path: Path | str | None = None) -> str:
    """Auto-detect message type from content and/or file extension."""
    # First check file extension if available
    if file_path:
        path = Path(file_path)
        if path.suffix.lower() == ".md":
            return "card"
    # Then check if content is JSON card format
    try:
        data = json.loads(content)
        if isinstance(data, dict) and ("card" in data or "msg_type" in data or "schema" in data):
            return "card"
    except json.JSONDecodeError:
        pass
    return "text"
