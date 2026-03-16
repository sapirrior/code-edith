import os
import sys
import shutil
from utils.clipboard import copy
from helper.banner import show_banner
from utils.history import clear_history, get_history # Added get_history
from utils.console import console

def handle_command(query):
    parts = query[1:].lower().split()
    cmd = parts[0] if parts else ""

    if cmd == "clear":
        console.width = shutil.get_terminal_size().columns - 2
        show_banner()
    
    elif cmd == "copy":
        history = get_history()
        assistant_msgs = [m["content"] for m in history if m["role"] == "assistant"]
        if assistant_msgs and assistant_msgs[-1]:
            if copy(str(assistant_msgs[-1])):
            	console.print("[orangex]Latest response copied to clipboard![/orangex]\n")
            else:
            	console.print("[orangex]No clipboard tool found\n[/orangex]")
        else:
            console.print("[orangex]Nothing to copy yet.[/orangex]\n")
        
    elif cmd == "reset":
        clear_history()
        console.print("[orangex]History reset. Memory wiped.[/orangex]\n")
    
    elif cmd == "exit":
        sys.exit(0)

    elif cmd == "help":
        console.print("[orangex]Edith Commands:[/orangex]")
        console.print("[greyx]/clear[/greyx] - Clear the terminal screen")
        console.print("[greyx]/copy [/greyx] - Copy last response to clipboard") # FIXED: Added to help menu
        console.print("[greyx]/reset[/greyx] - Wipe conversation history")
        console.print("[greyx]/exit [/greyx] - Stop Edith safely")
        console.print("[greyx]/help [/greyx] - Show this menu\n")
    
    else:
        console.print(f"[orangex]Unknown command:[/orangex][greyx]/{cmd}[/greyx]\n")
