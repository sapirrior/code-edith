import os
import time
import utils.signals
from utils.trust_folder import trust_folder
from utils.command_handler import handle_command
from utils.history import add_history, get_history, clear_history
from engine.chat import make_request
from engine.client import load_client
from helper.print_md import print_md
from helper.input import get_input
from helper.animation import animation
from utils.console import console
from helper.banner import show_banner
from utils.env import load_home_env, load_env

def load_all_envs_one_by_one():
    api_key = load_env("EDITH_API_KEY")
    base_url = load_env("EDITH_BASE_URL")
    model_name = load_env("EDITH_MODEL_NAME") or "gpt-4o"
    return api_key, base_url, model_name

def main():
    try:
        trust_folder()
        show_banner()
        api_key, base_url, model_name = load_all_envs_one_by_one()
        
        animation(True, "Connecting...")
        client = load_client(api_key, base_url)
        animation(False)

        while True:
            query = get_input().strip()
            if not query: continue
            if query.startswith("/"): handle_command(query); continue

            add_history({"role": "user", "content": query})
            animation(True, "Thinking...")

            response = make_request(client, get_history(), model_name)
            animation(False)

            print_md(response)
            add_history({"role": "assistant", "content": response})
            console.print("\n")

    except EOFError:
        pass
    except KeyboardInterrupt:
        pass
    except Exception as e:
        animation(False)
        console.print(f"\n[orangex]Engine Error:[/orangex] [greyx]{str(e)}[/greyx]")
    finally:
        animation(False)
        console.print("[greyx]Goodbye![/greyx]")
        exit(0)