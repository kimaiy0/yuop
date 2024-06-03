import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define the command handler for the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a link remover bot. Send me a message with links and I will remove them for you!")

# Define the message handler to remove links
def remove_links(update, context):
    message = update.message.text
    # Check if the message contains any link
    if "http" in message or "www." in message:
        # Remove the links from the message
        clean_message = " ".join(filter(lambda word: "http" not in word and "www." not in word, message.split()))
        # Send the cleaned message back to the user
        context.bot.send_message(chat_id=update.effective_chat.id, text=clean_message)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="No links found in the message!")

def main():
    # Create an instance of the Updater class and pass in your bot token
    updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    # Register the command handler for the /start command
    dispatcher.add_handler(CommandHandler('start', start))
    # Register the message handler to remove links
    dispatcher.add_handler(MessageHandler(Filters.text, remove_links))

    # Start the bot
    updater.start_polling()
    logger.info("Bot started!")

    # Run the bot until Ctrl-C is pressed or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
