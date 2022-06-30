import asyncio

from typing import Union
from datetime import datetime, timedelta
from Yukki import cleanmode, app, botname
from Yukki.database import is_cleanmode_on
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time


async def put_cleanmode(chat_id, message_id):
    if chat_id not in cleanmode:
        cleanmode[chat_id] = []
    time_now = datetime.now()
    put = {
        "msg_id": message_id,
        "timer_after": time_now + timedelta(minutes=1),
    }
    cleanmode[chat_id].append(put)


async def auto_clean():
    while not await asyncio.sleep(30):
        try:
            for chat_id in cleanmode:
                if not await is_cleanmode_on(chat_id):
                    continue
                for x in cleanmode[chat_id]:
                    if datetime.now() > x["timer_after"]:
                        try:
                            await app.delete_messages(chat_id, x["msg_id"])
                        except FloodWait as e:
                            await asyncio.sleep(e.x)
                        except:
                            continue
                    else:
                        continue
        except:
            continue


asyncio.create_task(auto_clean())


RANDOM = [
    "https://telegra.ph/file/b5860f56ae4f45a455f13.jpg",
    "https://telegra.ph/file/0c9e04c36f7d2dd28b844.jpg",
    "https://telegra.ph/file/0fe7cd1790954124a7b3b.jpg",
    "https://telegra.ph/file/b5860f56ae4f45a455f13.jpg",
]


HELP_TEXT = f"""
𓆩⌬𓆪 UCO Project
"""
