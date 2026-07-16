from pathlib import Path
from config import load_config, get_config_path

# Path to test files
TESTFILE_DIR = Path(__file__).parent / "testfile"


def test_load_config():
    config_path = TESTFILE_DIR / "config.test.json"
    loaded = load_config(config_path)
    assert loaded["APP_ID"] == "cli_a9622b75c53a5bd9"
    assert loaded["APP_SECRET"] == "toxynel66y3ShRkoHEBGwegJQVGoKQNE"
    assert loaded["RECEIVE_ID"] == "ou_fbedb11e450d89e17b6e4212892f8429"
    assert loaded["BASE_DIR"] == ""
