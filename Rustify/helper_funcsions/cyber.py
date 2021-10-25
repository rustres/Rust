from pyrogram import Client, __version__
import os, sys, platform
from dotenv import load_dotenv
from math import ceil
import time
from CyberPro import HU_STRING_SESSION, TG_COMPANION_BOT, APP_ID, API_HASH, DB_URI, IS_BOT


try:
    cyber        = Client(
HU_STRING_SESSION,
api_id          = APP_ID,
api_hash        = API_HASH,
plugins         = dict(root="CyberPro/plugins")
)
except ValueError:
    print("Yazdığınız dəyərlərdən biri yanlışdır!")
