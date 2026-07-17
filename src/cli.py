#!/usr/bin/env python3
import argparse
import sys
import json
from pathlib import Path

from config import load_config
from sender import send_message
from parser import read_file, detect_content_type


def safe_print(obj):
    """安全打印，处理 Unicode 编码问题，绝不抛出异常"""
    try:
        if isinstance(obj, (dict, list)):
            text = json.dumps(obj, ensure_ascii=True)
        else:
            text = str(obj)
    except:
        text = repr(obj)

    # 直接写入字节流，避免任何编码问题
    try:
        # 先尝试正常 print
        print(text)
        return
    except:
        pass

    # fallback: 直接写 buffer
    try:
        encoding = sys.stdout.encoding or 'utf-8'
        bytes_data = text.encode(encoding, errors='backslashreplace') + b'\n'
        sys.stdout.buffer.write(bytes_data)
        sys.stdout.flush()
    except:
        # 最后的终极 fallback
        try:
            bytes_data = text.encode('ascii', errors='backslashreplace') + b'\n'
            sys.stdout.buffer.write(bytes_data)
            sys.stdout.flush()
        except:
            # 彻底失败时也静默，不影响主程序
            pass


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
        base_dir = config.get("BASE_DIR")
        receive_id_type = config.get("RECEIVE_ID_TYPE")

        content = read_file(args.file_path, base_dir)

        msg_type = args.msg_type
        if msg_type == "auto":
            msg_type = detect_content_type(content, args.file_path)

        result = send_message(app_id, app_secret, receive_id, content, msg_type, receive_id_type)
        safe_print(f"Message sent successfully (type: {msg_type})")
        safe_print(f"Response: {result}")
        return 0

    except Exception as e:
        safe_print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
