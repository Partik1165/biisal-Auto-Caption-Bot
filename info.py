from os import getenv
import re

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "6727691050"))
API_ID = int(getenv("API_ID", "29101731"))
API_HASH = str(getenv("API_HASH", "a89da29d52632d195c9912067d1947f5"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "7915896160:AAFk3iNfFqUfAASG0KNZaIVxI766QUXJiCU"))
MONGO_DB = str(
    getenv(
        "MONGO_DB",
        "mongodb+srv://rename1215:dbrename1215@cluster0.vch58.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    )
)
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b><a href='https://t.me/+Zw_zIhwCMHk2MTk9'>{file_name} Telegram : @BotZ_Umesh\n\nForward the file before Downloading.</a></b>",
    )
)
