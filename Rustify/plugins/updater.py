from CyberPro.cyberhelp import CmdHelp

from os import path, environ, remove, execle
import sys
import asyncio
from git import Repo
import os
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from CyberPro import HEROKU_APIKEY, HEROKU_APPNAME
from CyberPro.helper_functions.cyber import cyber

from pyrogram import Client, filters, idle
from pyrogram.types import Message

requirements_path = path.join(path.dirname(path.dirname(path.dirname(__file__))), 'requirements.txt')

async def gen_chlog(repo, diff):
    ch_log = ''
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff):
        ch_log += f'•[{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n'
    return ch_log
  
async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            ' '.join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)
    
    
    
async def restart(message: Message, restart_type):
    if restart_type == 'update': text = '1'
    else: text = '2'
    await os.execvp("python3", ["python3", "cyber.py", f"{message.chat.id}",  f" {message.message_id}", f"{text}"])

    

@Client.on_message(filters.regex(r"^\.restart(?: |$)(.*)") & filters.outgoing)
async def restart_comand(client: Client, message: Message):
    await message.edit('<code>Bot yenidən başladılır...</code>')
    await restart(message, restart_type='restart')

    
    
@Client.on_message(filters.regex(r"^\.update(?: |$)(.*)") & filters.outgoing)
async def ustream(client:Client, message:Message):
    "CYBER PRO güncelleme modulu"

    await message.edit("`Güncəlləmələr yoxlanılır...`")
    conF = message.text.split(" ")
    if len(conF) == 1:
        conf = ""
    elif len(conF) == 2:
        if conF[1] == "now":
            conf = "now"
        if conF[1] == "force":
            conf = "force"
    else:
        conf = ""
    off_repo = "https://github.com/FaridDadashzade/CyberPro"
    if conf == "force":
        force_update = True
    else:
        force_update = False

    try:
        txt = "`Güncəlləmə zamanı bəzi xətalarla qarşılaşdım.`\n\n**LOG:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        repo = Repo()
        await message.edit(f'{txt}\n`{error} faylı tapılmadı.`')
        repo.__del__()
        return
    except GitCommandError as error:
        await message.edit(f'{txt}\n`github xətası {error}`')
        repo = Repo()
        repo.__del__()
        return
    except InvalidGitRepositoryError as error:
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        repo.create_head("main", origin.refs.main)
        repo.heads.main.set_tracking_branch(origin.refs.main)
        repo.heads.main.checkout(True)

    ac_br = repo.active_branch.name
    if ac_br != 'main':
        await message.edit("Branch doğru deyil!")
        repo.__del__()
        return

    try:
        repo.create_remote('upstream', off_repo)
    except BaseException:
        pass

    ups_rem = repo.remote('upstream')
    ups_rem.fetch(ac_br)

    changelog = await gen_chlog(repo, f'HEAD..upstream/{ac_br}')

    if not changelog and not force_update:
        await message.edit("`RustUserBot ən son versiyadadır!` \n\n** Branch:** `{}`".format(ac_br))
        repo.__del__()
        return

    if conf != "now" and not force_update:
        changelog_str = "`{}` üçün yeni güncəlləmə mövcuddur!\n\nDəyişikliklər:**\n`{}`".format(ac_br, changelog)
        if len(changelog_str) > 4096:
            await message.edit("`Dəyişikliklər siyahısı çox böyükdür fayl şəklində görməlisən..`")
            file = open("deyisiklikler.txt", "w+")
            file.write(changelog_str)
            file.close()
            await client.send_document(
                message.chat_id,
                "deyisiklikler.txt",
                reply_to_message_id=message.id,
            )
            remove("deyisiklikler.txt")
        else:
            await message.edit(changelog_str)
        await client.send_message(message.chat.id, "`Güncəlləməni etmək üçün \".update now\" əmrini istifadə edin.`")
        return

    if force_update:
        await message.edit("`Zorla güncəllənir...`")
        try:
            ups_rem.pull(ac_br)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        await update_requirements()
        await message.edit("`Zorla güncəlləmə sona çatdı..`")
        args = [sys.executable, "cyber.py"]
        execle(sys.executable, *args, environ)
        return
    await message.edit("`RustUserBot`\n**Status:**\n`Güncəllənir...`")
    try:
        ups_rem.pull(ac_br)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    await update_requirements()
    await message.edit("`RustUserBot`\n**Status:**\n`Yenidən başladılır...`")
    args = [sys.executable, "cyber.py"]
    execle(sys.executable, *args, environ)
    return

CmdHelp('updater').add_command(
'update', None, 'Rust UserBot da güncəlləmə olub olmadığını yoxlayar.'
    ).add_command(
        'update now', None, 'Botunuzu ən son versiyaya güncəlləyər.'
    ).add_command(
        'update force', None, 'Botda güncəlləmə olmasa belə botu güncəlləyər.'
    ).add()
