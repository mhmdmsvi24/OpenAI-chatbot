class ChatDatabase:
    def __init__(self):
        self.history = []

    def add_message(self, role, content):
        """Append user and assistant messages to chat history."""
        self.history.append({"role": role, "content": content})

    def get_history(self):
        """Return the chat history for sending to the API."""
        return self.history
