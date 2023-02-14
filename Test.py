import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm the File Extension Rename Bot. Send me a file extension and a new extension to rename all files with the old extension to the new extension.")

# Define a function to handle the /rename command
def rename(update, context):
    if len(context.args) < 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please specify the old extension and new extension separated by a space.")
        return
    old_extension = context.args[0]
    new_extension = context.args[1]
    for file_name in os.listdir('.'):
        if file_name.endswith(old_extension):
            old_name = file_name
            new_name = os.path.splitext(file_name)[0] + new_extension
            os.rename(old_name, new_name)
            context.bot.send_message(chat_id=update.effective_chat.id, text="The file has been renamed from {} to {}.".format(old_name, new_name))

# Define a function to handle all other messages
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Send me a file extension and a new extension to rename all files with the old extension to the new extension.")

# Set up the updater and dispatcher
updater = Updater(token='5703066773:AAFHwa56RRcA5UeJ7FfN29GFw8lV6kERo3E', use_context=True)
dispatcher = updater.dispatcher

# Add command handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('rename', rename, pass_args=True))

# Add message handler
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))

# Start the bot
updater.start_polling()
