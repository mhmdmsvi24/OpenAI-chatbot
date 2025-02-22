def print_chat(role, message):
    """Format and print chat messages clearly."""
    prefix = "User: " if role == "user" else "Assistant: "
    print(f"\033[1;32m{prefix}\033[0m{message}\n")  # Green color for clarity
