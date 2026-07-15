import json
import os
from pathlib import Path


def get_config_path() -> Path:
    """Get config.json path from the same directory as the executable/script."""
    if os.environ.get("FEISHU_SENDER_CONFIG"):
        return Path(os.environ["FEISHU_SENDER_CONFIG"])
    try:
        base_path = Path(__file__).parent
    except NameError:
        base_path = Path.cwd()
    config_path = base_path / "config.json"
    if not config_path.exists():
        config_path = Path.cwd() / "config.json"
    return config_path


def load_config(config_path: Path | None = None) -> dict:
    """Load config from config.json."""
    if config_path is None:
        config_path = get_config_path()
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)
