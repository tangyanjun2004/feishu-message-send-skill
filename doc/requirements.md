# 需求说明

## 项目目标

作为 OpenClaw 的 skill，提供一个将 Python 编译成二进制的 CLI 工具，用于通过飞书 API 发送消息。

## 功能需求

### 1. CLI 工具

- 可编译为独立二进制文件
- 读取同目录 `config.json` 配置文件
- 接受两个参数：
  - 参数1: 要发送的文件地址
  - 参数2: 消息类型（`card`/`text`/`auto`）

### 2. 消息类型

- `text`: 直接发送文本消息
- `card`: 发送飞书卡片消息
- `auto`: 自动判断内容类型

### 3. 配置文件

`config.json` 包含以下配置项：

```json
{
  "APP_ID": "飞书应用 APP ID",
  "APP_SECRET": "飞书应用 APP Secret",
  "RECEIVE_ID": "接收者 ID"
}
```

### 4. 飞书 API

使用飞书官方 API 发送消息，需先通过 `APP_ID` 和 `APP_SECRET` 获取 `tenant_access_token`。
