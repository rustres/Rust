import asyncio
from pyrogram import filters
from CyberPro import (
    SUDO_USERS
)
from CyberPro.helper_functions.admin_check import AdminCheck


async def admin_check(_, message):
    admin_status = await AdminCheck(
        message._client,
        message.chat.id,
        message.from_user.id
	)
    print(admin_status)
    return bool(admin_status)


def f_admin_check(f, m):
    vupool = asyncio.get_event_loop()
    tsk = vupool.run_until_complete(
        admin_check(f, m)
    )
    print(tsk)
    return tsk
    
  
admin_filter = filters.create(
    func=f_admin_check,
    name="AdminFilter"
)


def f_sudo_filter(f, m):
    return bool(
        m.from_user.id in SUDO_USERS
    )


sudo_filter = filters.create(
    func=f_sudo_filter,
    name="SudoFilter"
)
