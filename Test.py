from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm the Rename Bot. Send me a new name for yourself by typing /rename followed by your new name.")

# Define a function to handle the /rename command
def rename(update, context):
    new_name = context.args[0]
    context.user_data['old_name'] = update.message.chat.first_name
    context.user_data['new_name'] = new_name
    message = "Your name has been changed from {} to {}.".format(context.user_data['old_name'], context.user_data['new_name'])
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Define a function to handle all other messages
def echo(update, context):
    message = update.message.text
    if 'old_name' in context.user_data and message.lower() == 'undo':
        old_name = context.user_data['old_name']
        context.bot.send_message(chat_id=update.effective_chat.id, text="Your name has been changed back to {}.".format(old_name))
        context.user_data.pop('old_name')
        context.user_data.pop('new_name')
    elif 'new_name' in context.user_data:
        new_name = context.user_data['new_name']
        context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, {}!".format(new_name))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Send me a new name for yourself by typing /rename followed by your new name.")

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
