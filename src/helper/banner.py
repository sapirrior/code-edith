import os
from rich.panel import Panel
from rich.align import Align
from utils.console import console

folder_name = os.path.basename(os.getcwd()) # Reads current folder name
content = f"""
[resetx]Welcome to Code Edith![/resetx]
[orangex] ▛███▜[/orangex]
[orangex]▛█████▜[/orangex]
[orangex] ▘▘ ▝▝[/orangex]
[greyx]Folder: {folder_name}[/greyx]
[greyx]Tip: /help for information[/greyx]
"""

def show_banner():
	try: # try/except block
		console.clear()
		banner_panel = Panel( # Initializes the panel
			Align.left(content.strip()),
			border_style = "orangex",
			width = console.size.width - 2, # terminal-size - 2
			title_align = "left",
			title = "[bold orangex]Code Edith[/bold orangex]",
			padding = (1, 1) # adds padding
			)
		console.print(banner_panel)
	except Exception as e: # Error handle
		console.print("[Error] Loading banner.") # Error message
		exit(1)