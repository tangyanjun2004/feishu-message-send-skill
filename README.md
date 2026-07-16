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
  "RECEIVE_ID": "ou_xxx",
  "BASE_DIR": "C:\\path\\to\\files"
}
```

**BASE_DIR (optional)**: Base directory for files. If configured, you can pass just filenames or relative paths to the CLI.

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
# Send as card (full path)
feishu-sender C:\\reports\\report.json card

# Send markdown as card (full path)
feishu-sender C:\\reports\\update.md auto

# Send as text (full path)
feishu-sender C:\\notices\\notice.txt text

# With BASE_DIR configured, you can use just filenames:
feishu-sender report.json card
feishu-sender update.md auto
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
