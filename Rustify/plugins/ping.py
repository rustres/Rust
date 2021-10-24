from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio, datetime
from CyberPro.cyberhelp import CmdHelp


@Client.on_message(filters.command(['ping'], ['!','.','/']) & filters.me)
async def ping(client:Client, message:Message):
  
    rust = datetime.datetime.now()
    msj = "__Pinginiz hesablanır...__"

    son = datetime.datetime.now()
    vaxt = (son - rust).microseconds
    msj += f"\n\n**Pinginiz:** `{vaxt} ms`"

    await message.edit(msj)


CmdHelp("ping").add_command("ping", None, "Pinginizi göstərər.").add()
