----

<p align="center"><a href="https://t.me/RustUserBot"><img src="https://telegra.ph/file/078b999cbfbb19948e18d.jpg" width="400"></a></p> 
<h1 align="center"><b>RUST USERBOT 🇦🇿</b></h1>
</div>
<p align="center">
    Rust UserBot, Telegram istifadəsini asanlaşdıran bir proyektdir.
    
</p>

----

## Qurulum


#### Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/rustres/Rust)


#### Serverə qurulum

```sh
git clone https://github.com/rustres/Rust.git
cd Rustify
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
python3 -m Rustify
```


#### Nümunə plugin:

```from pyrogram import Client, filters
from Rustify.cyberhelp import CmdHelp
from pyrogram.types import Message

@Client.on_message(filters.command(['əmr'], ['!','.','/']) & filters.me)
async def cyberalive(client:Client, message:Message):
    await message.edit("Rust UserBot")
    

CmdHelp("fayladı").add_command("əmr", None, "Açıqlama yazaq.").add()
```


## Devs:

[All rust admins](https://github.com/rustres)

[Wertin](https://t.me/wertinium)

[Farid](https://t.me/Fvreed)

[Aisha](https://t.me/TheAisa)


## Credits:

Thanks all modules for help or credits and idea

[Kursad](https://github.com/KursadHD)
[Yusuf Usta](https://github.com/yusufusta)
[Dan (Pyrogram)](https://github.com/pyrogram)
[Lonami (Telethon rist)](https://github.com/telethon)
[Aditya](http://github.com/xditya)

