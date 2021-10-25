import os

class Config(object):
    LOGGER = True
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", None)
    BOTLOG = os.environ.get("BOTLOG", False)
    HEROKU = os.environ.get("HEROKU", True)
    BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID", None)
    HU_STRING_SESSION = os.environ.get("HU_STRING_SESSION", None)
    RUST_ASSISTANT_TOKEN = os.environ.get("HU_STRING_SESSION", None)
    TG_COMPANION_BOT = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    MAX_MESSAGE_LENGTH = 4096
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", ".")
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
    HEROKU_APIKEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APPNAME = os.environ.get("HEROKU_APPNAME", None)
    OFFICIAL_UPSTREAM_REPO = os.environ.get("OFFICIAL_UPSTREAM_REPO", "https://github.com/rustres/Rust")
    DB_URI = os.environ.get("DATABASE_URL", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
