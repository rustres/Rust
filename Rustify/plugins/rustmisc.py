# Copyright (C) 2021 RustAdmins.
# Licensed under MIT license;
# you may not use this file except in compliance with the License.
# All rights reserved.

# RustUserBot (C)

from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from Rustify.rusthelp import CmdHelp

@Client.on_message(filters.regex(r"^\.kickme(?: |$)(.*)") & filters.outgoing)
async def kickme(client: Client, message: Message):
    m = await message.edit('<code>Görüşənədək...</code>')
    await asyncio.sleep(3)
    await client.leave_chat(chat_id=message.chat.id)

    
@Client.on_message(filters.command(['pin'], ['!','.','/']) & filters.me)
async def sabitle(client: Client, message: Message):
    try:
        message_id = message.reply_to_message.message_id
        await client.pin_chat_message(message.chat.id, message_id)
        await message.edit('<code>Uğurla sabitləndi! </code>')
    except:
        await message.edit('</code>Xəta:\nBöyük ehtimalla bir mesaja cavab vermirsən, və ya bu əmri şəxsidə yazmısan.</code>')


        
@Client.on_message(filters.command(['save'], ['!','.','/']) & filters.me)
async def save(client: Client, message: Message):
    await message.delete()
    await message.reply_to_message.forward('self')
    
    
@Client.on_message(filters.command(['q'], ['!','.','/']) & filters.me)  
async def quotly(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit("`Stiker edə bilməyim üçün bir mesaja cavab ver!`")
        return
    await message.edit("`Stiker edilir...`")
    await message.reply_to_message.forward("@QuotLyBot")
    is_sticker = False
    progress = 0
    while not is_sticker:
        try:
            msg = await client.get_history("@QuotLyBot", 1)
            check = msg[0]["sticker"]["file_id"]
            is_sticker = True
        except:
            await sleep(0.5)
            progress += random.randint(0, 10)
            try:
                await message.edit("`Stiker edilir..`\nHazırlanır {}%".format(progress))
            except:
                await message.edit("`Botdan cavab ala bilmədim.`")
    if msg_id := msg[0]['message_id']:
        await asyncio.gather(
            message.delete(),
            client.forward_messages(message.chat.id,"@QuotLyBot", msg_id)
        )
    

CmdHelp('rustmisc').add_command(
'kickme', None, 'Qrupu tərk etmək üçün.'
    ).add_command(
        'pin', None, 'Cavab verdiyiniz mesajı sabitləyər.'
    ).add_command(
        'save', None, 'Cavab verdiyiniz mesajı kayıtlı mesajlara göndərər.'
    ).add_command(
        'q', None, 'Cavab verdiyiniz mesajı stikerə çevirər.'
    ).add()
