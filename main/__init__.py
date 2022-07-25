from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=17797968, cast=int)
API_HASH = config("API_HASH", default="33278a72c628c758e0c8aad138f1f1b5")
BOT_TOKEN = config("BOT_TOKEN", default="5480292967:AAEl8s3ZcmJE2srVJrOYF6P2yVhLao3UN_o")
BOT_UN = config("BOT_UN", default="Dani_JensenBot")
AUTH_USERS = config("AUTH_USERS", default=2129323324, cast=int)
LOG_CHANNEL = config("LOG_CHANNEL", default="Comp_Logs")
LOG_ID = config("LOG_ID", default="-1001667784784")
FORCESUB = config("FORCESUB", default="1667784784")
FORCESUB_UN = config("FORCESUB_UN", default="Comp_Logs")
ACCESS_CHANNEL = config("ACCESS_CHANNEL", default="-1001616744957")
MONGODB_URI = config("MONGODB_URI", default="mongodb+srv://CompressBot:CompressBot@cluster0.ygssibg.mongodb.net/?retryWrites=true&w=majority")

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
