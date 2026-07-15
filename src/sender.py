import json
import requests


def get_tenant_access_token(app_id: str, app_secret: str) -> str:
    """Get tenant_access_token from Feishu API."""
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    payload = {
        "app_id": app_id,
        "app_secret": app_secret
    }
    resp = requests.post(url, json=payload)
    resp.raise_for_status()
    data = resp.json()
    if data.get("code") != 0:
        raise Exception(f"Failed to get token: {data}")
    return data["tenant_access_token"]


def send_text(access_token: str, receive_id: str, content: str) -> dict:
    """Send plain text message via Feishu API."""
    url = "https://open.feishu.cn/open-apis/im/v1/messages"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    # receive_id starts with "ou_" indicates open_id
    receive_id_type = "open_id" if receive_id.startswith("ou_") else "user_id"
    params = {"receive_id_type": receive_id_type}
    payload = {
        "receive_id": receive_id,
        "msg_type": "text",
        "content": json.dumps({"text": content})
    }
    resp = requests.post(url, headers=headers, params=params, json=payload)
    resp.raise_for_status()
    return resp.json()


def send_card(access_token: str, receive_id: str, content: str) -> dict:
    """Send interactive card message via Feishu API.

    If content is a complete JSON card (with "schema"), send it directly.
    Otherwise wrap as a simple markdown card.
    """
    url = "https://open.feishu.cn/open-apis/im/v1/messages"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    # receive_id starts with "ou_" indicates open_id
    receive_id_type = "open_id" if receive_id.startswith("ou_") else "user_id"
    params = {"receive_id_type": receive_id_type}
    try:
        parsed_content = json.loads(content)
        if isinstance(parsed_content, dict) and "schema" in parsed_content:
            card = parsed_content
        else:
            raise ValueError()
    except (json.JSONDecodeError, ValueError):
        card = {
            "elements": [
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": content
                    }
                }
            ]
        }
    payload = {
        "receive_id": receive_id,
        "msg_type": "interactive",
        "content": json.dumps(card)
    }
    resp = requests.post(url, headers=headers, params=params, json=payload)
    resp.raise_for_status()
    return resp.json()


def send_message(app_id: str, app_secret: str, receive_id: str, content: str, msg_type: str) -> dict:
    """Send message with specified type."""
    access_token = get_tenant_access_token(app_id, app_secret)
    if msg_type == "text":
        return send_text(access_token, receive_id, content)
    elif msg_type == "card":
        return send_card(access_token, receive_id, content)
    else:
        raise ValueError(f"Unknown message type: {msg_type}")
