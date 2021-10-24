import logging
import os

def xeta(yazi:str) -> None:
   print("[✗] {}".format(yazi))
def melumat(yazi:str) -> None:
   print("[*] {}".format(yazi))
def ugurlu(yazi:str) -> None:
   print("[✓] {}".format(yazi))
def onemli(yazi:str) -> None:
   print("[!] {}".format(yazi))


from Rustify import (
    HU_STRING_SESSION,
    TG_COMPANION_BOT,
    APP_ID, 
    API_HASH, 
    DB_URI,
    IS_BOT,
    RUST_VERSION
)    

import asyncio
import pyrogram



def main():
    plugins = dict(
        root="Rustify/plugins",
    )
    
    if HU_STRING_SESSION is None:
    	app = pyrogram.Client(
            "TG_COMPANION_BOT",
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=TG_COMPANION_BOT,
            plugins=plugins
        )
    else:
    	app = pyrogram.Client(
            HU_STRING_SESSION,
            api_id=APP_ID,
            api_hash=API_HASH,
            plugins=plugins
        )
    
    app.run()


pluginler = []  

for fayl in os.listdir("./Rustify/plugins/"):
    if not fayl.endswith(".py") or fayl.startswith("_"):
        continue
    pluginler.append(fayl.replace('.py',''))

onemli("Rust UserBot hazırlanır...")
ugurlu(f"Yüklənən modul sayı: {len(pluginler)}\n")
print()
ugurlu(f"Version: {RUST_VERSION}")

if __name__ == "__main__":
	main()
