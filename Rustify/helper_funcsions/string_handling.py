import re
import time
from typing import List
from pyrogram.types import Message
from Rustify import COMMAND_HAND_LER

def extract_time(time_val):
    if any(time_val.endswith(unit) for unit in ('s', 'm', 'h', 'd')):
        unit = time_val[-1]
        time_num = time_val[:-1]  
        if not time_num.isdigit():
            return None

        if unit == 's':
            bantime = int(time.time() + int(time_num))
        elif unit == 'm':
            bantime = int(time.time() + int(time_num) * 60)
        elif unit == 'saat':
            bantime = int(time.time() + int(time_num) * 60 * 60)
        elif unit == 'd':
            bantime = int(time.time() + int(time_num) * 24 * 60 * 60)
        else:
            return None
        return bantime
    else:
        return None
