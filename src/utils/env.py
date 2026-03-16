import os
from pathlib import Path
from dotenv import load_dotenv
from utils.console import console

def load_home_env():
	try:
		home_path = Path.home() / ".env"
		
		if home_path.exists():
			load_dotenv(dotenv_path=home_path)
	except Exception as e:
		console.print("[Error] Loading environmental variables.")
		exit(1)

load_home_env()

def load_env(var):
		val = os.environ.get(var)
		if val is None:
			console.print(f"[Error] Loading {var} environmental variable.")
			exit(1)
		else:
			return val