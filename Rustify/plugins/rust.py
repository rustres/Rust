from CyberPro import APP_ID, API_HASH, HU_STRING_SESSION, CMD_HELP
from CyberPro.helper_functions.cyberhelp import pluginlerim

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command(['rust'], ['!','.','/']) & filters.me)
async def rusthelp(client:Client, message:Message):

    yazi = message.text.split()

    if len(yazi) == 1:
        msj = "**Xahiş edirəm bir Rust modulu adı qeyd edin!**\nNümunə: `.rust alive`\n\n"

        msj += "**Yüklənən modullar:**\n"
        msj += pluginlerim()

        await message.edit(msj)
        return

    await message.edit(CMD_HELP[yazi[1]])
