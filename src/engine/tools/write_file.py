from pathlib import Path

def execute(path: str, content: str) -> str:
    p = Path(path).expanduser().resolve()
    try:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
        return f"Successfully wrote {len(content)} characters to {path}"
    except Exception as e:
        return f"Error writing file: {e}"
