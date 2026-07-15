# 飞书消息发送 Skill 项目

## 项目概述

这是一个 OpenClaw skill 项目，提供通过飞书 API 发送消息的功能。项目包含一个可编译为二进制的 CLI 工具。

## 目录结构

```
send-feishu-card-skill/
├── CLAUDE.md                 # 项目文档
├── README.md                 # Skill 说明
├── pyproject.toml            # Python 项目配置
├── build.py                  # 构建脚本
├── .gitignore                # Git 忽略文件
├── src/                      # 源代码目录
│   ├── __init__.py
│   ├── cli.py                # CLI 入口
│   ├── config.py             # 配置管理
│   ├── sender.py             # 消息发送
│   └── parser.py             # 内容解析
├── tests/                    # 测试代码目录
│   ├── __init__.py
│   ├── test_config.py
│   ├── test_parser.py
│   ├── test_sender.py
│   └── testfile/             # 测试文件
│       ├── config.test.json
│       ├── card_example.json
│       ├── report_example.md
│       └── text_example.txt
├── doc/                      # 文档目录
│   └── output/
│       └── SKILL.md          # Skill 发布文档
└── dist/                     # 编译输出目录（git 忽略）
    ├── SKILL.md
    └── bin/
        ├── feishu-sender.exe
        ├── config.json
        └── config.example.json
```

## 项目规范

- **源代码**: 必须放在 `src/` 目录下
- **测试代码**: 严格放在 `tests/` 目录下
- **配置文件**: `config.json` 与二进制同目录
- **依赖管理**: 使用 `pyproject.toml`
- **编译工具**: PyInstaller
- **构建输出**: 编译产物放在 `dist/bin/` 目录，`dist/` 整体 git 忽略

## 主要功能

1. 读取同目录 `config.json` 配置（APP_ID, APP_SECRET, RECEIVE_ID）
2. CLI 接受两个参数: 文件路径、消息类型（卡片/文本/auto）
3. 读取文件内容，通过飞书 API 发送
4. 支持通过文件扩展名自动检测：`.md` 文件自动用卡片方式发送

## 开发指南

### 安装依赖

```bash
pip install -e .
```

### 运行测试

```bash
pytest -v
```

### 构建二进制

```bash
pip install pyinstaller
python build.py
```

### 手动测试发送

```bash
cd dist/bin
feishu-sender.exe ../../tests/testfile/text_example.txt text
```
