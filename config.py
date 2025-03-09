import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", ""))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/eb80582fa42f9bd412085.jpg")
