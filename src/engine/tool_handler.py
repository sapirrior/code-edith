import shutil
import sys
from rich.markup import escape
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text
from engine.tools import web_search, read_file, write_file, shell_command
from helper.animation import animation
from utils.console import console

# Brand colors (ANSI true color — matches animation.py)
_ORANGE = "\033[38;2;217;119;87m"
_GREY   = "\033[38;2;153;153;153m"
_RESET  = "\033[0m"

TOOL_MAP = {
    "WebSearch":    web_search.execute,
    "ReadFile":     read_file.execute,
    "WriteFile":    write_file.execute,
    "ShellCommand": shell_command.execute,
}

DESTRUCTIVE_TOOLS = {"WriteFile", "ShellCommand"}

TOOL_LABELS = {
    "WebSearch":    "Search",
    "ReadFile":     "Read",
    "WriteFile":    "Write",
    "ShellCommand": "Shell",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _term_width() -> int:
    return shutil.get_terminal_size().columns - 2


def _get_ext(target: str) -> str:
    """Derive a Pygments-safe language identifier from a file path."""
    if "." in target:
        ext = target.rsplit(".", 1)[-1].lower()
        # Guard: a real extension is short and contains no path separators
        if len(ext) <= 6 and "/" not in ext and "\\" not in ext:
            return ext
    return "text"


TITLED_TOOLS = {"ReadFile", "WriteFile"}

def _make_title(name: str, target: str) -> str:
    """Build a Rich markup title. Only Read/Write show the path in the title."""
    label = TOOL_LABELS.get(name, name)
    if name in TITLED_TOOLS:
        safe_target = escape(target)
        return f"[orangex]{label}[/orangex] [greyx]·[/greyx] [greyx]{safe_target}[/greyx]"
    return f"[orangex]{label}[/orangex]"


def _print_panel(name: str, target: str, content: str | None) -> None:
    """Print a consistent bordered panel for every tool call."""
    if content:
        ext  = _get_ext(target)
        body = Syntax(content, ext, theme="monokai", word_wrap=True, background_color="default")
    else:
        body = Text(target, style="greyx")

    console.print(
        Panel(
            body,
            title=_make_title(name, target),
            title_align="left",
            border_style="greyx",
            padding=(0, 2),
            expand=False,
            width=_term_width(),
        )
    )


def _confirm_prompt() -> str:
    """
    Print a colored Allow? prompt and return the raw user input.
    Uses ANSI codes directly so the color renders regardless of
    whether Rich's console.input() strips markup in the prompt.
    """
    sys.stdout.write(f"   {_GREY}Allow?{_RESET} {_ORANGE}(y/n):{_RESET} ")
    sys.stdout.flush()
    return input()


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

def handle_tool_call(name: str, args: dict) -> str:
    func = TOOL_MAP.get(name)
    if not func:
        return f"Error: Tool '{name}' not found."

    target  = args.get("command") or args.get("path") or args.get("query") or "..."
    content = args.get("content")

    # Always stop the spinner and show what's about to happen
    animation(False)
    console.print()
    _print_panel(name, target, content)

    if name in DESTRUCTIVE_TOOLS:
        try:
            raw = _confirm_prompt()
            console.print()

            if raw.strip().lower() not in ("y", "yes"):
                console.print(f"   [greyx]Denied.[/greyx]\n")
                animation(True, "Thinking...")
                return "Tool execution denied by user. Do not retry this action."

        except (KeyboardInterrupt, EOFError):
            console.print()
            console.print(f"   [greyx]Aborted.[/greyx]\n")
            animation(True, "Thinking...")
            return "Tool execution aborted by user. Do not retry this action."

    try:
        animation(True, f"Running {name}...")
        return str(func(**args))
    except Exception as e:
        return f"Error executing {name}: {str(e)}"
    finally:
        animation(True, "Thinking...")
