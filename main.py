import os
from telegram.ext import Updater

updater = Updater(token=os.environ.get("TELEGRAM_BOT_TOKEN"))

# rest of your code

# Your handlers here

port = int(os.environ.get('PORT', '8443'))
updater.start_webhook(listen="0.0.0.0", port=port, url_path=settings.(6548277251:AAG2PMddqTTSRIyCIkxitm2C_Jo8CiIF0hY))
updater.bot.set_webhook("https://zap-corretor-21afd1e16ec3.herokuapp.com/" + settings.6548277251:AAG2PMddqTTSRIyCIkxitm2C_Jo8CiIF0hY)
