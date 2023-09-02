import os

from telegram.ext import Updater
import settings

updater = Updater(token=settings.6372799289:AAHNFkVjfCBvllvQE7p8U4sdHpSl2wgge2I)

# Your handlers here

port = int(os.environ.get('PORT', '8443'))
updater.start_webhook(listen="0.0.0.0",
                      port=port,
                      url_path=settings.6372799289:AAHNFkVjfCBvllvQE7p8U4sdHpSl2wgge2I)
updater.bot.set_webhook("https://zap-corretor-21afd1e16ec3.herokuapp.com/" + settings.6372799289:AAHNFkVjfCBvllvQE7p8U4sdHpSl2wgge2I)
