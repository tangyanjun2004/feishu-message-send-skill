#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

from config import load_config
from sender import send_message
from parser import read_file, detect_content_type


def main():
    parser = argparse.ArgumentParser(
        description="Send Feishu message from file content"
    )
    parser.add_argument("file_path", help="Path to the file to send")
    parser.add_argument(
        "msg_type",
        choices=["text", "card", "auto"],
        help="Message type (text/card/auto)"
    )
    args = parser.parse_args()

    try:
        config = load_config()
        app_id = config["APP_ID"]
        app_secret = config["APP_SECRET"]
        receive_id = config["RECEIVE_ID"]

        content = read_file(args.file_path)

        msg_type = args.msg_type
        if msg_type == "auto":
            msg_type = detect_content_type(content, args.file_path)

        result = send_message(app_id, app_secret, receive_id, content, msg_type)
        print(f"Message sent successfully (type: {msg_type})")
        print(f"Response: {result}")
        return 0

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
