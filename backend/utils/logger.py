import logging

# Set up logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("chatbot")


def log_message(message):
    logger.info(message)
