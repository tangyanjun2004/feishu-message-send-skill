import json
import tempfile
from pathlib import Path
from config import load_config, get_config_path


def test_load_config():
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / "config.json"
        config_data = {
            "APP_ID": "test_app_id",
            "APP_SECRET": "test_app_secret",
            "RECEIVE_ID": "test_receive_id"
        }
        with open(config_path, "w") as f:
            json.dump(config_data, f)
        loaded = load_config(config_path)
        assert loaded["APP_ID"] == "test_app_id"
        assert loaded["APP_SECRET"] == "test_app_secret"
        assert loaded["RECEIVE_ID"] == "test_receive_id"
