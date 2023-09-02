from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Hello, welcome to zapCORRETOR!')

updater = Updater(token="6548277251:AAG2PMddqTTSRIyCIkxitm2C_Jo8CiIF0hY", use_context=True)

dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
