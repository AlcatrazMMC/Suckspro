import asyncio
import importlib

from pyrogram import idle

from Yukki.modules import ALL_MODULES




async def initiate_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("Yukki.modules." + all_module)
    print("Started atena AFK Bot.")
    await idle()
    print("GoodBye! Stopping Bot")


if __name__ == "__main__":
    loop.run_until_complete(initiate_bot())
    loop = asyncio.get_event_loop()
