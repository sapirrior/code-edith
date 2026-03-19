import shutil
from utils.console import console
from helper.banner import show_banner

def cmd_clear():
	console.width = shutil.get_terminal_size().columns - 2
	show_banner()