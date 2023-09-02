from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Hello, welcome to zapCORRETOR!')

updater = Updater(token='6372799289:AAHNFkVjfCBvllvQE7p8U4sdHpSl2wgge2I', use_context=True)

dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
