# Code Edith

A lightweight, terminal-based AI coding agent. Connects to any OpenAI-compatible API endpoint — hosted providers or self-hosted models both work.

![License](https://img.shields.io/badge/license-Apache--2.0-orange) ![Python](https://img.shields.io/badge/python-3.10%2B-orange) [![PyPI Downloads](https://static.pepy.tech/personalized-badge/code-edith?period=total&units=INTERNATIONAL_SYSTEM&left_color=GREY&right_color=ORANGE&left_text=downloads)](https://pepy.tech/projects/code-edith)

---

## Requirements

- Python 3.10 or higher
- An OpenAI-compatible API endpoint (e.g. OpenAI, Anthropic via proxy, Ollama, LM Studio)
- A `.env` file in your home directory (`~/.env`) — see [Configuration](#configuration)

---

## Installation

**From PyPI** (stable):

```bash
pip install code-edith
```

**From GitHub** (latest):

```bash
pip install git+https://github.com/sapirrior/code-edith
```

---

## Configuration

Create a `.env` file in your **home directory** (`~/.env`) with the following variables:

```env
EDITH_API_KEY=your_api_key
EDITH_BASE_URL=https://api.openai.com/v1
EDITH_MODEL_NAME=gpt-4o
```

| Variable | Description |
|---|---|
| `EDITH_API_KEY` | API key from your provider |
| `EDITH_BASE_URL` | Base URL of the OpenAI-compatible endpoint |
| `EDITH_MODEL_NAME` | Model identifier (e.g. `gpt-4o`, `claude-3-5-sonnet`, `llama3`) |

The config is read from `~/.env` at startup. Edith does not touch your project files during configuration.

---

## Usage

Navigate to the folder you want to work in, then launch Edith:

```bash
cd your-project
edith
```

**Trust prompt.** The first time you run Edith in a folder, it will ask whether you trust it. Answering `y` creates a `.edith/TRUST` marker file in the current directory. Subsequent launches in the same folder skip this step. If you answer `n`, Edith exits immediately without doing anything.

Once running, type your request at the `>> ` prompt and press Enter.

---

## Tools

Edith has four built-in tools it can invoke autonomously to complete tasks:

| Tool | What it does | Requires confirmation |
|---|---|---|
| `WebSearch` | Searches the web using DuckDuckGo | No |
| `ReadFile` | Reads a local file and returns its contents | No |
| `WriteFile` | Creates or overwrites a file with new content | **Yes** |
| `ShellCommand` | Runs a bash command in the current directory | **Yes** |

For `WriteFile` and `ShellCommand`, Edith will always pause and show you exactly what it is about to do before asking `Allow? (y/n)`. Typing anything other than `y` or `yes` cancels the action. The model is instructed not to retry a denied action.

---

## Commands

Type these at the prompt at any time:

| Command | Description |
|---|---|
| `/clear` | Clear the terminal and redraw the banner |
| `/copy` | Copy the last response to the clipboard |
| `/reset` | Wipe the conversation history (model forgets the session) |
| `/exit` | Exit Edith cleanly |
| `/help` | Show the command list |

---

## Reporting Issues

Open an issue on the [GitHub repository](https://github.com/sapirrior/code-edith/issues).

---

## License

Apache-2.0. See [LICENSE](LICENSE) for details.
