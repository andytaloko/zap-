import os
from telegram.ext import Updater, CommandHandler

# Initialize the Updater
token = os.environ.get("TELEGRAM_BOT_TOKEN")  # Make sure to set this env variable in Heroku

# Debugging line to print the token, remove it later
print(f"Token: {token}")

if token is None:
    print("Token is not set!")
else:
    updater = Updater(token=token, use_context=True)

    # Your other code here...

    # Start the Bot
    port = int(os.environ.get("PORT", 8443))  # Also set the PORT env variable in Heroku
    updater.start_webhook(listen="0.0.0.0", port=port, url_path=token)
