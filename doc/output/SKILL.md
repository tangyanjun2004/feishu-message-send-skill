---
name: feishu-message-sender
description: 发送飞书（Lark）消息的 Skill，支持文本和交互式卡片格式
version: 1.1.0
---

## 概述

这是一个用于通过飞书（Lark）API 发送消息的 Skill。支持发送纯文本消息和交互式卡片消息。

## 适用场景

- 发送系统通知和告警
- 推送日报、周报等定期报告
- 发送构建/部署状态通知
- 分享数据分析结果
- 任何需要通过飞书发送消息的自动化场景

## 如何使用

### 进入脚本目录

```bash
cd {baseDir}/bin
```

## 输入

### 命令行参数

```bash
.\feishu-sender.exe <file-path> <message-type>
```

| 参数 | 类型 | 必需 | 说明 |
|------|------|------|------|
| `file-path` | string | 是 | 要发送的文件路径 |
| `message-type` | string | 是 | 消息类型：`text`/`card`/`auto` |

### 消息类型

- `text` - 以纯文本格式发送
- `card` - 以飞书交互式卡片格式发送
- `auto` - 自动检测：JSON 卡片或 .md 文件使用 `card`，其他使用 `text`

## 输出

### 成功

```
Message sent successfully (type: card)
Response: {"code": 0, "data": {...}, "msg": "success"}
```

退出码：`0`

### 失败

```
Error: ...
```

退出码：`1`

## 文件格式说明

### 卡片 JSON 格式

文件内容应为完整的飞书卡片 JSON，包含 `schema` 字段：

```json
{
  "schema": "2.0",
  "config": {"wide_screen_mode": true},
  "header": {
    "title": {"tag": "plain_text", "content": "标题"},
    "template": "blue"
  },
  "body": {
    "elements": [...]
  }
}
```

### Markdown 格式

`.md` 文件会被自动包装为卡片发送，内容支持 Markdown 语法。

### 文本格式

普通文本文件直接以文本消息发送。

## 使用示例

### 发送卡片（完整路径）

```bash
.\feishu-sender.exe C:\\reports\\report.json card
```

### 发送文本（完整路径）

```bash
.\feishu-sender.exe C:\\notices\\notice.txt text
```

### 自动检测（完整路径）

```bash
.\feishu-sender.exe C:\\data\\data.md auto
```

### 使用 BASE_DIR（只需文件名）

配置 BASE_DIR 后：

```bash
.\feishu-sender.exe report.json card
.\feishu-sender.exe notice.txt text
.\feishu-sender.exe data.md auto
```

## 目录结构

```
dist/
├── SKILL.md          # 本文档
└── bin/
    ├── feishu-sender.exe    # 主程序
    └── config.json          # 配置文件
```
