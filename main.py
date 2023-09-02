import os

from telegram.ext import Updater
import settings

updater = Updater(token=settings.TELEGRAM_API_KEY)

# Your handlers here

port = int(os.environ.get('PORT', '8443'))
updater.start_webhook(listen="0.0.0.0",
                      port=port,
                      url_path=settings.TELEGRAM_API_KEY)
updater.bot.set_webhook("https://your-heroku-app-name.herokuapp.com/" + settings.TELEGRAM_API_KEY)
