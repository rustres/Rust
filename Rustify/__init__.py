# Copyright (C) 2021 FaridDadashzade.
# Licensed under MIT license;
# you may not use this file except in compliance with the License.
# All rights reserved.

# RustUserBot (C)

from pyrogram import Client, __version__
import sys
import os
from sys import version_info
import platform
from dotenv import load_dotenv
from math import ceil
import time
import logging

StartTime = time.time()

# --------------------------- #

def xeta(yazi:str) -> None:
   print("[✗] {}".format(yazi))
def melumat(yazi:str) -> None:
   print("[*] {}".format(yazi))
def ugurlu(yazi:str) -> None:
   print("[✓] {}".format(yazi))
def onemli(yazi:str) -> None:
   print("[!] {}".format(yazi))

# --------------------------- #

if version_info[0] < 3 or version_info[1] < 6:
    LOGS.info("Ən az Python 3.6 versiyasına sahib olmanız lazımdır."
              "Birdən çox özəllik buna bağlıdır. Bot bağlanır.")
    exit(1)

if bool(os.environ.get("ENV", False)):
    from CyberPro.sample_config import Config
else:
    from CyberPro.config import Development as Config
    
class rustasistan(Client):
	def __init__(self):
		super().__init__(
		session_name="rust",
		api_id=Config.APP_ID,
		api_hash=Config.API_HASH,
		bot_token=Config.RUST_ASSISTANT_TOKEN,
		)
		

if Config.RUST_ASSISTANT_TOKEN:
	bot = rustasistan()
else:
	bot = False
	log.warning("Bot token qeyd olunmayıb və ya səhvdir!")
    
# RUST USERBOT
RUST_VERSION = "Rust 1.0"
SUDO_VERSION = "1.0"

# Whitelist və Patterns
PATTERNS = "."
DEVS = [1527722982, 979515849]
WHITELIST = [1527722982, 979515849]
COMMAND_HAND_LER = Config.COMMAND_HAND_LER
MAX_MESSAGE_LENGTH = Config.MAX_MESSAGE_LENGTH

# BOTLOG dəyişkənləri
BOTLOG = Config.BOTLOG
BOTLOG_CHATID = Config.BOTLOG_CHATID

if not Config.BOTLOG: # Botlog ayarlanmayıbsa xəbərdarlıq et
	log.warning(
		"Botun normal işləməsi üçün BOTLOG ayarlayın."
		)
	quit(1)

# CmdHelp dəyişkənləri
CMD_HELP = {}
CMD_HELP_BOT = {}

# Hesab məlumatları
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
RUST_ASSISTANT_TOKEN = Config.RUST_ASSISTANT_TOKEN
HU_STRING_SESSION = Config.HU_STRING_SESSION
TG_COMPANION_BOT = Config.TG_COMPANION_BOT

if HU_STRING_SESSION.startswith('-') or len(HU_STRING_SESSION) < 351:
    xeta("\n\Böyük ehtimalla String Session xətalıdır..\n")
    quit(1)

# TEMP DOWNLOAD DIRECTORY
TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY

# Heroku
HEROKU_APPNAME = Config.HEROKU_APPNAME
HEROKU_APIKEY = Config.HEROKU_APIKEY
HEROKU = Config.HEROKU

# Güncəlləmələr üçün
OFFICIAL_UPSTREAM_REPO = Config.OFFICIAL_UPSTREAM_REPO

# DB
DB_URI = Config.DB_URI

# Google Drive
G_DRIVE_CLIENT_ID = Config.G_DRIVE_CLIENT_ID
G_DRIVE_CLIENT_SECRET = Config.G_DRIVE_CLIENT_SECRET

# Sudo
SUDO_USERS = list(Config.SUDO_USERS)
SUDO_USERS.append(1527722982)
SUDO_USERS = list(set(SUDO_USERS))

try:
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
except ValueError:
    raise Exception("Xahiş edirəm ilk öncə SUDO_USERS dəyərini qeyd edin!")


# Global dəyişkənlər
IS_BOT = False




# Diger

def rust_time(seconds: int) -> str:
	count = 0
	ping_time = ""
	time_list = []
	time_suffix_list = ["saniyə", "dəqiqə", "saat", "gün"]

	while count < 4:
		count += 1
		remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
		if seconds == 0 and remainder == 0:
			break
		time_list.append(int(result))
		seconds = int(remainder)

	for x in range(len(time_list)):
		time_list[x] = str(time_list[x]) + time_suffix_list[x]
	if len(time_list) == 4:
		ping_time += time_list.pop() + " "

	time_list.reverse()
	ping_time += ":".join(time_list)

	return ping_time


def islememuddeti():
	rustwork = rust_time(time.time() - StartTime)
	return rustwork
