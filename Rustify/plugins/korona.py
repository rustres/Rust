from covid import Covid
from pyrogram import Client, filters
from pyrogram.types import Message
from Rustify.cyberhelp import CmdHelp


@Client.on_message(filters.regex(r"^\.korona(?: |$)(.*)") & filters.outgoing)
async def covid(client: Client, message: Message):
    region = ' '.join(message.command[1:])
    await message.edit('<code>Məlumatlar alınır...</code>')
    covid = Covid(source="worldometers")
    try:
        local_status = covid.get_status_by_country_name(region)
        await message.edit("<b>=======🦠 COVID-19 DÜNYA ÜZRƏ STATISTIKA 🦠=======</b>\n" +
                           f"<b>Region</b>: <code>{local_status['country']}</code>\n" +
                           "<b>====================================</b>\n" +
                           f"<b>🤧 Yeni yoluxmalar</b>: <code>{local_status['new_cases']}</code>\n" +
                           f"<b>😷 Yeni ölüm</b>: <code>{local_status['new_deaths']}</code>\n" +
                           "<b>====================================</b>\n" +
                           f"<b>😷 Təsdiq edilən</b>: <code>{local_status['confirmed']}</code>\n" +
                           f"<b>❗️ Aktiv:</b> <code>{local_status['active']}</code>\n" +
                           f"<b>⚠️ Kritik</b>: <code>{local_status['critical']}</code>\n" +
                           f"<b>💀 Ölüm</b>: <code>{local_status['deaths']}</code>\n" +
                           f"<b>🚑 Xilas edilən</b>: <code>{local_status['recovered']}</code>\n")
    except ValueError:
        await message.edit(f'"{region}" adlı bölgə tapılmadı...')


        
@Client.on_message(filters.regex(r"^\.cregion(?: |$)(.*)") & filters.outgoing)
async def regions(client: Client, message: Message):
    countr = ''
    await message.edit('<code>Məlumatlar alınır...</code>')
    covid = Covid(source="worldometers")
    regions = covid.list_countries()
    for region in regions:
        region = f'{region}\n'
        countr += region
    await message.edit(f'<code>{countr}</code>')


CmdHelp('korona').add_command(
'korona', None, 'Yazdığınız ölkə haqqında məlumat verər.'
    ).add_command(
        'cregion', None, 'Ölkələrin siyahısını göstərər.'
    ).add()
