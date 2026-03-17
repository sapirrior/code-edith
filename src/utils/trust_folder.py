from pathlib import Path
from utils.console import console

def trust_folder():
	
	trust_dir = Path(".edith")
	trust_file = trust_dir / "TRUST"
	
	if trust_file.exists():
		return True
	else:
		console.clear()
		console.print(f"[orangex]Folder:[/orangex] [greyx]{Path.cwd().name}.[/greyx]")
		console.print("[orangex]This folder is not trusted.[/orangex]")
		
		choice = console.input("Do you trust this folder (y/n): ").strip().lower()
		
		if choice != 'y':
			exit(0)
		else:
			try:
				trust_dir.mkdir(parents=True, exist_ok=True)
				trust_file.touch()
				console.print("[orangex]Starting...[/orangex]")
				return True
			except Exception as e:
				console.print("[Error] Checking Trust Folder.")
				exit(1)