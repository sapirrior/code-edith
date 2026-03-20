from utils.history import get_history
from utils.console import console
from utils.commands.helper.clipboard import copy

def cmd_copy():
    history = get_history()
    
    # FIX: Use without a "content" key
    assistant_msgs = [m.get("content", "") for m in history if m.get("role") == "assistant"]
    
    if assistant_msgs and assistant_msgs[-1]:
        if copy(str(assistant_msgs[-1])):
            console.print("[orangex]Latest response copied to clipboard![/orangex]\n")
        else:
            console.print("[orangex]No clipboard tool found\n[/orangex]")
    else:
        console.print("[orangex]Nothing to copy yet.[/orangex]\n")
