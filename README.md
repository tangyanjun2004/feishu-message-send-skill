# send-feishu-card-skill

OpenClaw skill for sending messages via Feishu (Lark) API.

## Features

- Send plain text messages
- Send interactive card messages
- Auto-detect message type from file extension (.md = card)
- Auto-detect card format from JSON content

## Quick Start

### 1. Configure

Create `config.json` in the same directory as the binary:

```json
{
  "APP_ID": "cli_xxx",
  "APP_SECRET": "xxx",
  "RECEIVE_ID": "ou_xxx"
}
```

### 2. CLI Usage

```bash
feishu-sender <file-path> <message-type>
```

Message types:
- `text` - Send as plain text
- `card` - Send as Feishu interactive card
- `auto` - Auto-detect content type

Examples:
```bash
# Send as card
feishu-sender report.json card

# Send markdown as card
feishu-sender update.md auto

# Send as text
feishu-sender notice.txt text
```

### 3. Build Binary

```bash
pip install pyinstaller
python build.py
```

Binary will be in `dist/bin/` directory.

## Directory Structure

```
dist/
├── SKILL.md              # Skill documentation
└── bin/
    ├── feishu-sender.exe
    ├── config.json
    └── config.example.json
```

## Development

See [CLAUDE.md](CLAUDE.md) for detailed development documentation.
