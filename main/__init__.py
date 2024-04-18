#Github.com/

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "24665357" #config("API_ID", default=None, cast=int)
API_HASH = "beb7e4b83ada668fa85f9a9b56338f1d" #config("API_HASH", default=None)
BOT_TOKEN = "6922908824:AAGwHG7FlOIamxiRGy4V3mD4MUIlH4pI-6E" #config("BOT_TOKEN", default=None)
SESSION = "1BVtsOKwBuzNY68Wkk0mCeRM9uZVztE-9z7YQACOCtNVVpLSxOcxkiZoSWwwxqtGwpU_9ccRCHJmctj_QTXTleenvPiJ9MTpVfQm0-crg-Qwxc5gCAOfCKtJJr-Yq19JriTQ6wSIikxtKanDF3PYP8wbnd27d6Q0z_C-dd3-ZRdoVsjD4nqLjGFuv5OnlSTMW7hqqBef7sAGoNhTi9ZxRXfIMw-chD1uSqb2Ueng_COAw5rwZVn6-JQw6ui4R1f_SDjFy92a1TmDNCnSi7W4Yq3HPkRF3zZOIZGd6qdlSDFl5Vf8ccA3F2AfjCgsACZLN7sM6EQMCHN9dNl39IFg0M1q4BLJ_hAY=" #config("SESSION", default=None)
FORCESUB = "1002137417670" #config("FORCESUB", default=None)
AUTH = "1717511106" #config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
