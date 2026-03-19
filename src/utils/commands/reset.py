from utils.console import console
from utils.history import clear_history

def cmd_reset():
	clear_history()
	console.print("[orangex]History reset. Memory wiped.[/orangex]\n")