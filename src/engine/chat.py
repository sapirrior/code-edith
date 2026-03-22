import json
from pathlib import Path
from engine.tool_handler import handle_tool_call
from utils.history import add_history
from helper.animation import animation
from helper.print_md import print_md

def make_request(client, msgs, model):
    src_dir = Path(__file__).resolve().parent.parent
    system_content = (src_dir / "config" / "system.txt").read_text().strip()

    with open(src_dir / "config" / "tools.json", 'r') as f:
        tools_schema = json.load(f)

    messages = [{"role": "system", "content": system_content}] + msgs

    max_iter = 10
    for _ in range(max_iter):
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools_schema,
            tool_choice="auto"
        )

        msg = response.choices[0].message

        if not msg.tool_calls:
            return msg.content or ""

        if msg.content:
            animation(False)
            print_md(msg.content)

        assistant_msg = msg.model_dump()
        assistant_msg["content"] = assistant_msg.get("content") or ""

        messages.append(assistant_msg)
        add_history(assistant_msg)

        tool_results = []
        for tool_call in msg.tool_calls:
            name = tool_call.function.name
            try:
                args = json.loads(tool_call.function.arguments)
            except (json.JSONDecodeError, TypeError):
                args = {}

            result = handle_tool_call(name, args)

            tool_msg = {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": name,
                "content": str(result)
            }
            tool_results.append(tool_msg)
            add_history(tool_msg)

        messages.extend(tool_results)
        animation(True, "Reasoning...")

    return ""