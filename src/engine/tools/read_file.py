from pathlib import Path

def execute(path: str) -> str:
    p = Path(path).expanduser().resolve()
    if not p.exists(): return f"Error: File not found: {path}"
    if not p.is_file(): return f"Error: Not a file: {path}"
    try:
        return p.read_text(errors="replace")
    except Exception as e:
        return f"Error reading file: {e}"
