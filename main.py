from telegram.ext import Updater, CommandHandler
import os
import settings

# Read port from environment variables
port = int(os.environ.get('PORT', 5000))

updater = Updater(token=settings.TELEGRAM_API_KEY)

# Add handlers and other functionalities here

# For Heroku Deployment
updater.start_webhook(listen="0.0.0.0",
                      port=port,
                      url_path=settings.TELEGRAM_API_KEY)
updater.bot.set_webhook("https://https://zap-corretor-21afd1e16ec3.herokuapp.com/.herokuapp.com/" + settings.TELEGRAM_API_KEY)
