import logging

from api.chatbot import send_request
from config import load_dotenv
from db.history import chat_history
from utils.helpers import print_chat_history, print_colored

# Load environment variables
load_dotenv()


def start_chat():
    print_colored(
        "Welcome to the chatbot! Type 'exit' to end the conversation.", Fore.YELLOW
    )

    while True:
        # Print the current chat history
        print_chat_history(chat_history.get_history())

        # Get user input
        user_input = input(Fore.GREEN + "You: " + Style.RESET_ALL)

        if user_input.lower() == "exit":
            print_colored("Goodbye! Chatbot session ended.", Fore.RED)
            break

        # Append user input to history
        chat_history.append_message("user", user_input)

        # Get the bot's response
        messages = (
            chat_history.get_history()
        )  # Send entire chat history for multi-turn context
        bot_response = send_request(messages)

        if bot_response:
            response_content = bot_response["choices"][0]["message"]["content"]
            print_colored(f"Assistant: {response_content}", Fore.CYAN)

            # Append assistant's response to history
            chat_history.append_message("assistant", response_content)
        else:
            print_colored(
                "Error: Unable to get a response from the assistant.", Fore.RED
            )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start_chat()
