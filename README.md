# Code Edith

**Code Edith** (`code-edith`) is a lightweight, terminal-based AI coding assistant. It connects to any AI model that implements the OpenAI-compatible response structure, giving you flexibility over your choice of provider or self-hosted model.

> **Note:** This project is under active development. Features such as tool-calling are not yet available.

---

## Installation

Install directly from GitHub using `pip`:

```bash
pip install git+https://github.com/sapirrior/code-edith
```

---

## Configuration

After installation, create a `.env` file in your **home directory** (`~/.env`) and define the following environment variables:

```env
EDITH_API_KEY=your_api_key
EDITH_MODEL_NAME=your_model_name
EDITH_BASE_URL=base_url_for_the_model
```

| Variable | Description |
|---|---|
| `EDITH_API_KEY` | API key for your chosen provider |
| `EDITH_MODEL_NAME` | Model identifier (e.g. `gpt-4o`, `claude-3-5-sonnet`) |
| `EDITH_BASE_URL` | Base URL of the OpenAI-compatible endpoint |

---

## Usage

Once configured, launch Edith from any terminal:

```bash
edith
```

---

## Reporting Issues

If you encounter a bug or unexpected behavior, please open an issue on the [GitHub repository](https://github.com/sapirrior/code-edith/issues).

---

## License
This project is licensed under a custom license. See the [LICENSE](LICENSE) file for details regarding personal and commercial use.

---

***Happy Coding!***

*by Nolan Stark.*
