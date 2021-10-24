from pyrogram import Client, filters
from Rustify.rusthelp import CmdHelp
from pyrogram.types import Message
from random import choice
    
ALIVE_STR = [
    "`Rust is working...`",
    "`Rust is working on: docker ...`",
]


@Client.on_message(filters.command(['alive'], ['!','.','/']) & filters.me)
async def cyberalive(client:Client, message:Message):
    await message.edit(choice(ALIVE_STR))
    

CmdHelp("alive").add_command("alive", None, "Rust UserBotun aktiv olub olmadığını yoxlayar.").add()
