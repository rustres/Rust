import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


import asyncio
import os

try:
    from rustuser import APP_ID, API_HASH
except ModuleNotFoundError:
    APP_ID = int(input("APP ID yazın: "))
    API_HASH = input("API HASH yazın: ")


import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


async def main(APP_ID, API_HASH):
    async with pyrogram.Client(
        ":memory:",
        api_id=APP_ID,
        api_hash=API_HASH
    ) as app:
        print(app.export_session_string())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(APP_ID, API_HASH))
