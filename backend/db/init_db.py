class ChatHistory:
    def __init__(self):
        self.history = []

    def append_message(self, role, content):
        """Append a new message to the conversation history."""
        self.history.append({"role": role, "content": content})

    def get_history(self):
        """Return the full conversation history."""
        return self.history


# Global instance of ChatHistory
chat_history = ChatHistory()
