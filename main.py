from telegram.ext import Updater, CommandHandler
import settings

updater = Updater(token=settings.TELEGRAM_API_KEY)

# Add handlers and other functionalities here

updater.start_polling()
