from rich.console import Console
from rich.theme import Theme
from rich.markdown import Markdown

theme_custom = Theme({ # Adds custom themes
    "orangex": "rgb(217,119,87)", # orange color
    "greyx": "rgb(128,128,128)", # grey color
    "resetx": "default" # white color
})

try:
	console = Console(theme=theme_custom) # installs console with custom themes
	console.width = console.size.width # sets width
except Exception as e:
	console.print("[Error] Starting the console.")
	exit(1) # exits if error occurs