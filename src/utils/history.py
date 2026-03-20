class ChatHistory:
    """Manages the conversation history for the AI model."""
    def __init__(self, max_length=None):
        self._history = []
        self.max_length = max_length

    def add(self, message):
        if not isinstance(message, dict):
            raise ValueError("Message must be a dictionary.")
        self._history.append(message)
        
        if self.max_length and len(self._history) > self.max_length:
            self._history.pop(0)

    def get(self):
        return list(self._history)

    def clear(self):
        self._history.clear()

    def __len__(self):
        return len(self._history)


_manager = ChatHistory()

def add_history(message):
    _manager.add(message)

def get_history():
    return _manager.get()

def clear_history():
    _manager.clear()
