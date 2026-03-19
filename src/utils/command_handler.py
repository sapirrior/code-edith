from utils.console import console
from utils.commands.clear import cmd_clear
from utils.commands.copy import cmd_copy
from utils.commands.reset import cmd_reset
from utils.commands.exit import cmd_exit
from utils.commands.help import cmd_help

def handle_command(query):
	parts = query[1:].lower().split()
	cmd = parts[0] if parts else ""
	
	if cmd == "clear":
		cmd_clear()
	elif cmd == "copy":
		cmd_copy()
	elif cmd == "reset":
		cmd_reset()
	elif cmd == "exit":
		cmd_exit()
	elif cmd == "help":
		cmd_help()
	else:
		console.print(f"[orangex]Unknown command:[/orangex][greyx]/{cmd}[/greyx]\n")