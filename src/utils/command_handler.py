import os
import sys
from helper.banner import show_banner
from utils.history import clear_history
from utils.console import console

def handle_command(query):
    parts = query[1:].lower().split()
    cmd = parts[0] if parts else ""

    if cmd == "clear":
    	show_banner()
        
    elif cmd == "reset":
        clear_history()
        console.print("[orangex]  History reset. Memory wiped.[/orangex]\n")
    
    elif cmd == "exit":
        sys.exit(0)

    elif cmd == "help":
        console.print("\n[orangex]Edith Commands:[/orangex]")
        console.print("[greyx]/clear[/greyx] - Clear the terminal screen")
        console.print("[greyx]/reset[/greyx] - Wipe conversation history")
        console.print("[greyx]/exit [/greyx] - Stop Edith safely")
        console.print("[greyx]/help [/greyx] - Show this menu\n")
    
    else:
        console.print(f"[orangex]Unknown command:[/orangex][greyx]/{cmd}[/greyx]\n")
