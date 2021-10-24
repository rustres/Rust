from CyberPro.cyberhelp import CmdHelp
from time import time
import speedtest
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command(['speedtest'], ['!','.','/']) & filters.me)
async def stest(client:Client, message:Message):
    await message.edit("`Sürət testi başladılır...`")
    basla = time()
    a = speedtest.Speedtest()
    a.get_best_server()
    a.download()
    a.upload()
    son = time()
    ping = round(son - basla, 2)
    b = a.results.share()
    await client.send_photo(message.chat.id,b,caption="**Speedtest** {} saniyə içində tamamlandı.".format(ping))
    await message.delete()

CmdHelp("speedtest").add_command("speedtest", None, "Botunuzun download və upload sürətini ölçər.").add()
