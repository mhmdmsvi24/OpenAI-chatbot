from api import send_request
from db import ChatDatabase
from utils import print_chat

# Initialize chat history database
db = ChatDatabase()

# Start the chat
print("Welcome to the chatbot! Type 'exit' to quit.\n")

while True:
    user_input = input("\033[1;34mYou: \033[0m")  # Blue color for user input
    if user_input.lower() == "exit":
        print("\nGoodbye!")
        break

    # Add user message to history
    db.add_message("user", user_input)

    # Get assistant response
    bot_response = send_request(db.get_history())

    if bot_response:
        # Add assistant response to history
        db.add_message("assistant", bot_response)

        # Print response
        print_chat("assistant", bot_response)
