from utils.console import console
from pathlib import Path

def make_request(client, msgs, model):
    try:
        # 1. Get the absolute path to THIS specific file (chat.py)
        current_file = Path(__file__).resolve()
        src_dir = current_file.parent.parent
        path = src_dir / "config" / "system.txt"
        
        content = path.read_text().strip()
        system = [{"role": "system", "content": content}]
        messages = system + msgs
        
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=None
        )
        return response.choices[0].message.content
    except Exception as e:
        console.print(f"[Error] Making message request to the model.")
        exit(1)