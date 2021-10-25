import importlib
from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio, os, sys
from Rustify.rusthelp import CmdHelp
from Rustify.helper_functions.rusthelp import pluginlerim
from Rustify.helper_functions.rustmisc import cavablananmsj
from Rustify.helper_functions.rust import rust


@Client.on_message(filters.command(['plist'], ['!','.','/']) & filters.me)
async def pluginsiyahisi(client:Client, message:Message):
    msj = "**Hazırda yüklədiyiniz pluginlər:**\n"
    msj += pluginlerim()

    
    try:
        await message.edit(msj)
    except Exception as rustxeta3:
        print(str(rustxeta3))
        

@Client.on_message(filters.command(['pinstall'], ['!','.','/']) & filters.me)
async def pluginyukle(client:Client, message:Message):

    cavablanan_msj = message.reply_to_message
    if not message.reply_to_message:
        await message.edit("`Xahiş edirəm bir plugin faylına cavab verin!`")
        return
    if len(message.command) == 1 and cavablanan_msj.document:
        if cavablanan_msj.document.file_name.split(".")[-1] != "py":
            await message.edit("`Yalnız Python faylı yükləyə bilirəm :(`")
            return
        rust_directory = f"./CyberPro/plugins/{cavablanan_msj.document.file_name}"
        await message.edit("`Plugin yüklənir...`")

        if os.path.exists(rust_directory):
            await message.edit(f"`{cavablanan_msj.document.file_name}` **plugini onsuzda mövcuddur!**")
            return

        try:
            await client.download_media(message=cavablanan_msj, file_name=rust_directory)
            await asyncio.sleep(2)
            try:
              spec = importlib.util.spec_from_file_location(rust_directory, rust_directory)
              mod = importlib.util.module_from_spec(spec)
              spec.loader.exec_module(mod)
            except Exception as rustxeta:
              await message.edit(f"**Yükləmə uğursuzdur!**\n\n`Plugin xətalıdır. ❌`\n\nXəta: {rustxeta}")
              os.remove(rust_directory)
              return
            await message.edit(f"**Plugin uğurla yükləndi:** `{cavablanan_msj.document.file_name}`\nBot yenidən başladılır...")
            try:
                await cyber.stop()
            except:
                pass
            os.execl(sys.executable, sys.executable, *sys.argv)
            return

        except Exception as rustxeta2:
            print(str(rustxeta2))
            return

    await message.edit('`Python skriptinə cavab verməlisiniz!`')
    
    
    
@Client.on_message(filters.command(['premove'], ['!','.','/']) & filters.me)
async def premove(client:Client, message:Message):

    rustmodules = ["updater","speedtest","alive","ping","heroku","covid","rustmisc","rust", "afk", "spammer","admin","whois"]
        
    if len(message.command) == 2:
        config = message.command[1]
        if config in rustmodules:
            await message.edit("**Bu Rust UserBot moduludur bunu silə bilməzsən!**")
            return
        rust_directory = f"./Rustify/plugins/{message.command[1]}.py"
        
        if os.path.exists(rust_directory):
            os.remove(rust_directory)
            await asyncio.sleep(2)
            await message.edit(f"**Plugin silindi:** `{message.command[1]}`\n__Bot yenidən başladılır...__")
            try:
                await cyber.stop()
            except:
                pass
            os.execl(sys.executable, sys.executable, *sys.argv)
            return

        await message.edit("`Belə bir plugin yoxdur!`")
        return

    await message.edit("`Düzgün bir plugin adı qeyd edin!`")
    
    
CmdHelp('plugin').add_command(
'plist', None, 'Yüklədiyiniz pluginlərin siyahısını göndərər..'
    ).add_command(
        'pinstall', None, 'Cavab verdiyiniz plugini yükləyər.'
    ).add_command(
        'premove', None, 'Plugin faylını botunuzdan silər.'
    ).add()
