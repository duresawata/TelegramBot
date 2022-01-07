from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, dispatcher
import logging


logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    user = update.message.from_user
    logging.info(f"User {user.first_name} start Conversation.")

    text = "Welcome to The Bot!\nType /help to get help."
    context.bot.send_message(chat_id = update.message.chat_id, text = text)

def help(update, context):
    text = """
    use the following commands\n
        /start - to start a bot
        /help - to get help
    """
    context.bot.send_message(chat_id = update.message.chat_id, text = text)

def handle_text(update, context):
    text = update.message.text
    context.bot.send_message(chat_id = update.message.chat_id, text = "you said: " + text)

def error(update, context):
    context.bot.send_message(chat_id = update.message.chat_id, text = "some went wrong")

def main():
    updater = Updater("TOKEN")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_text))

    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()






