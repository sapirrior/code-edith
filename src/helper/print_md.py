from utils.console import console
from rich.markdown import Markdown
from rich.padding import Padding

# Brand Colors
ORANGEX = "\033[38;2;217;119;87m"
GREYX = "\033[38;2;153;153;153m"
RESET = "\033[0m"

def print_md(text):
	try:
		txt_md = Markdown(text.strip())
		padded_md = Padding(txt_md, (0, 2, 0, 3))
		console.print(padded_md)
	except Exception as e:
		console.print("[Error] prompt request.")
		exit(1)