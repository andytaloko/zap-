def start(update, context):
    update.message.reply_text('Welcome to zapCORRETOR!')

def list_property(update, context):
    update.message.reply_text('Listing properties...')

class Property:
    def __init__(self, id, location, features):
        self.id = id
        self.location = location
        self.features = features

from telegram.ext import Updater, CommandHandler
import settings

updater = Updater(token=settings.TELEGRAM_API_KEY)

# Add handlers and other functionalities here

updater.start_polling()
