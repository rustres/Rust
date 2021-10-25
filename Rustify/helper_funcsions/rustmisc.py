from typing import Any
from pyrogram import Client
from pyrogram.types import Message

# ------------------------------------------------------------ #

async def cavablananmsj(message:Message) -> Any:
    cavab_id = None

    if message.reply_to_message:
        cavab_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        cavab_id = message.message_id

    return cavab_id

# ------------------------------------------------------------ #

async def istifadeci(message:Message) -> Any:
    cavablanan_mesaj = message.reply_to_message

    if cavablanan_mesaj:
        istifadeci = cavablanan_mesaj.from_user
    else:
        istifadeci = message.from_user

    istifadeci_id = istifadeci.id
    istifadeci_adi = f"@{istifadeci.username}" if istifadeci.username else f"[{istifadeci.first_name}](tg://user?id={istifadeci_id})"

    return istifadeci_adi, istifadeci_id
  
# ------------------------------------------------------------ #

async def istifadeci_foto(client:Client, message:Message) -> Any:
    cavablanan_mesaj = message.reply_to_message

    if cavablanan_mesaj:
        rust = await client.get_users(message.reply_to_message.from_user.id)
        return await client.download_media(rust.photo.big_file_id)
    return None
