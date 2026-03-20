import shutil
from engine.tools import web_search, read_file, write_file, shell_command
from helper.animation import animation
from utils.console import console
from rich.panel import Panel
from rich.syntax import Syntax

TOOL_MAP = {
    "WebSearch":  web_search.execute,
    "ReadFile":   read_file.execute,
    "WriteFile":  write_file.execute,
    "ShellCommand": shell_command.execute,
}

DESTRUCTIVE_TOOLS = {"WriteFile", "ShellCommand"}

def handle_tool_call(name, args):
    func = TOOL_MAP.get(name)
    if not func:
        return f"Error: Tool '{name}' not found."

    target = args.get("command") or args.get("path") or args.get("query") or "..."
    content = args.get("content")

    if name in DESTRUCTIVE_TOOLS:
        animation(False)
        console.print()
        
        if content:
            ext = target.split('.')[-1] if '.' in target else 'text'
            syntax_content = Syntax(content, ext, theme="monokai", word_wrap=True, background_color="default")
            preview_panel = Panel(
                syntax_content,
                # Tightly packed title: Action in orange, tool name in grey, target in grey
                title=f"[orangex]Action:[/orangex] [greyx]{name}[/greyx] [orangex]|[/orangex] [greyx]{target}[/greyx]",
                title_align="left",
                border_style="greyx",
                padding=(0, 2),
                expand=False,
                # Dynamically calculate exact terminal width minus 2
                width=shutil.get_terminal_size().columns - 2
            )
            console.print(preview_panel)
        else:
            if name == "ShellCommand":
                console.print(f"   [orangex]Action:[/orangex] [greyx]{name}[/greyx]\n   [orangex]Argument:[/orangex] [greyx]{target}[/greyx]", soft_wrap=True)
            else:
                console.print(f"   [orangex]Action:[/orangex] [greyx]{name} | {target}[/greyx]", soft_wrap=True)

        try:
            choice = input("   Allow? (y/n): ").strip().lower()
            console.print()
            if choice not in ('y', 'yes'):
                animation(True, "Thinking...")
                return "Error: User denied permission to execute this tool."
        except (KeyboardInterrupt, EOFError):
            console.print()
            animation(True, "Thinking...")
            return "Error: User aborted tool execution."

    try:
        animation(True, f"Running {name}...")
        return str(func(**args))
    except Exception as e:
        return f"Error executing {name}: {str(e)}"
    finally:
        animation(True, "Thinking...")
