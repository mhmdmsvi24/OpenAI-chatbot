from colorama import Fore, Style


def print_colored(text: str, color: str):
    """
    Print the given text in the specified color in the terminal.
    """
    print(f"{color}{text}{Style.RESET_ALL}")


def print_chat_history(history: list):
    """
    Print the chat history in a user-friendly manner.
    """
    for message in history:
        role = message["role"].capitalize()
        content = message["content"]

        if role == "User":
            print_colored(f"{role}: {content}", Fore.GREEN)
        elif role == "Assistant":
            print_colored(f"{role}: {content}", Fore.CYAN)
        else:
            print(f"{role}: {content}")
