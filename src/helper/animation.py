import sys
from halo import Halo

# Brand Colors
ORANGEX = "\033[38;2;217;119;87m"
GREYX = "\033[38;2;153;153;153m"
RESET = "\033[0m"

# Global instance initialization
_sp = Halo(
    spinner={
        "interval": 200,
        "frames": [f"{ORANGEX}{c}{RESET}" for c in "✲✱❖"]
    }
)

def animation(run: bool, text="Reasoning..."):
    """
    run: True to start/update, False to stop.
    text: The message to display in Greyx.
    """
    if run:
        # Update text dynamically (works even if already spinning)
        _sp.text = f"{GREYX}{text}{RESET}"
        _sp.start()
    else:
        # Stop the Halo spinner
        _sp.stop()
        
        # The Fix: Move cursor to start (\r) and erase the entire line (\033[K)
        # This gives print_md a completely blank canvas.
        sys.stdout.write("\r\033[K")
        sys.stdout.flush()