import signal

_UNCATCHABLE = {signal.SIGKILL, signal.SIGSTOP}

for sig in signal.valid_signals() - _UNCATCHABLE:
    try:
        signal.signal(sig, signal.SIG_IGN)
    except (ValueError, OSError, RuntimeError):
        continue