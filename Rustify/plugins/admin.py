# Copyright (C) 2021 FaridDadashzade.
# Licensed under MIT license;
# you may not use this file except in compliance with the License.
# All rights reserved.

# RustUserBot (C)


import asyncio
from datetime import datetime
from CyberPro.cyberhelp import CmdHelp
from pyrogram.types import Message
from pyrogram import Client, filters
from CyberPro import COMMAND_HAND_LER
from CyberPro.helper_functions.admin_check import admin_check
from CyberPro.helper_functions.extract_user import extract_user
from CyberPro.helper_functions.string_handling import extract_time


@Client.on_message(filters.command(['purge'], ['!','.','/']) & filters.me)
async def purge(client, message):
    if message.reply_to_message:
        start_t = datetime.now()
        recvd_commands = message.text.split(" ")
        from_user = None
        if len(recvd_commands) > 1:
            user_id = recvd_commands[1]
            from_user = await client.get_users(user_id)
        start_message = message.reply_to_message.message_id
        end_message = message.message_id
        list_of_messages = await client.get_messages(
            chat_id=message.chat.id,
            message_ids=range(start_message, end_message),
            replies=0
        )
        list_of_messages_to_delete = []
        purged_messages_count = 0
        for a_message in list_of_messages:
            if len(list_of_messages_to_delete) == 100:
                await client.delete_messages(
                    chat_id=message.chat.id,
                    message_ids=list_of_messages_to_delete,
                    revoke=True
                )
                purged_messages_count += len(list_of_messages_to_delete)
                list_of_messages_to_delete = []
            if from_user is not None:
                if a_message.from_user == from_user:
                    list_of_messages_to_delete.append(a_message.message_id)
            else:
                list_of_messages_to_delete.append(a_message.message_id)
        print(list_of_messages_to_delete)
        await client.delete_messages(
            chat_id=message.chat.id,
            message_ids=list_of_messages_to_delete,
            revoke=True
        )
        purged_messages_count += len(list_of_messages_to_delete)
        list_of_messages_to_delete = []
        end_t = datetime.now()
        time_taken_s = (end_t - start_t).seconds
        await message.edit(
            f"<u>Təmizləmə tamamlandı</u> {purged_messages_count} mesaj {time_taken_s} saniyə içində təmizləndi."
        )
        await asyncio.sleep(5)
        await message.delete()
    else:
        await message.edit("`Mesajları silməyim üçün bir istifadəçinin mesajına cavab ver.`")
        
        
@Client.on_message(filters.command(['ban'], ['!','.','/']) & filters.me)
async def ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return

    user_id, user_first_name = extract_user(message)

    try:
        await message.chat.kick_member(
            user_id=user_id
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Rust: #BAN"
                f"{user_first_name}"
                " Qadağan edildi."
            )
        else:
            await message.reply_text(
                "Rust: #BAN "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a>"
                " Qadağan edildi."
            )
        
        
CmdHelp('admin').add_command(
'purge', None, 'Cavab verdiyiniz mesajları silər..'
    ).add_command(
        'ban', None, 'Cavab verdiyiniz istifadəçini ban edər.'
    ).add()
