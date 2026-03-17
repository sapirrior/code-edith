import subprocess
import sys

def copy(text):
    """Copy text to clipboard. Returns True on success, False otherwise."""
    if not text:
        return False
    
    # Platform-specific and fallback clipboard tools
    cmds = {
        'darwin': [['pbcopy']],
        'win32': [['clip']],
    }.get(sys.platform, [['xclip', '-selection', 'clipboard'], ['wl-copy'], ['termux-clipboard-set']])
    
    content = str(text).encode('utf-8')
    
    for cmd in cmds:
        try:
            subprocess.run(cmd, input=content, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, check=True, timeout=5)
            return True
        except (FileNotFoundError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
            continue
    
    return False
