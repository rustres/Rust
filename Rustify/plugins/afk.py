from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
import datetime
import asyncio
from Rustify.rusthelp import CmdHelp


async def afk_handler(client, message):
    try:
        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = (end - start)
        if message.from_user.is_bot is False:
            await message.reply_text(f"<b>Artıq AFK-yam.</b>\n</b>{afk_time}</b>\n"
                                     f"<b>Səbəb:</b> <i>{reason}</i>")
    except NameError:
        pass
      
      
@Client.on_message(filters.regex(r"^\.afk(?: |$)(.*)") & filters.outgoing)
async def afk(client, message):
    global start, end, handler, reason
    start = datetime.datetime.now().replace(microsecond=0)
    handler = client.add_handler(MessageHandler(afk_handler, (filters.private & ~filters.me)))
    if len(message.text.split()) >= 2:
        reason = message.text.split(" ", maxsplit=1)[1]
    else:
        reason = "Yoxdur"
    await message.edit("</code>Artıq AFK-yam.</code>")
    
    
@Client.on_message(filters.regex(r"^\.unafk(?: |$)(.*)") & filters.outgoing)
async def unafk(client, message):
    try:
        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = (end - start)
        await message.edit(f"<b>Artıq AFK deyiləm\nAFK olduğum müddət: {afk_time}</b>")
        client.remove_handler(*handler)
    except NameError:
        await message.edit("<b>Sən onsuzda AFK deyildin!</b>")
        await asyncio.sleep(3)
        await message.delete() 
        
        
CmdHelp('afk').add_command(
'afk', None, 'Sizi AFK edər.'
    ).add_command(
        'unafk', None, 'AFK modulunu deaktiv edər.'
    ).add()
