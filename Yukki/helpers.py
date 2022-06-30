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
    "https://telegra.ph/file/0ae0fe261a86bfd61e526.jpg",
    "https://telegra.ph/file/62e2916b2644ca8c6d970.jpg",
    "https://telegra.ph/file/e0298dbe967d8631a304e.jpg",
    "https://telegra.ph/file/bebac0f849b8dc1a5b05d.jpg",
    "https://telegra.ph/file/cb48da33d241e6eba4fcf.jpg",
    "https://telegra.ph/file/c35e402c456622ae6031d.jpg",
    "https://telegra.ph/file/7ab8a0e990b32c82ed1bd.jpg",
    "https://telegra.ph/file/06707dbcf18b472660f81.jpg",
    "https://telegra.ph/file/cfa9c4976eefc0419715c.jpg",
    "https://telegra.ph/file/46e336e599be7e183f5b8.jpg",
    "https://telegra.ph/file/df9410a66d2f4f8c48ec9.jpg",
    "https://telegra.ph/file/65b9da65fc30f3e7b7356.jpg",
    "https://telegra.ph/file/ccdb557e16a4e424bb62b.jpg",
    "https://telegra.ph/file/f2604884da441ceecf010.jpg",
    "https://telegra.ph/file/67dceee4977fd62ee88d7.jpg",
    "https://telegra.ph/file/c92477beb1a36fd72bb82.jpg",
    "https://telegra.ph/file/33669bf37d9c1419537bd.jpg",
    "https://telegra.ph/file/ac565da01c09f66787753.jpg",
    "https://telegra.ph/file/4400ba49e8c4efe4ac79e.jpg",
    "https://telegra.ph/file/1c16f2e92690b2b7fc3fd.jpg",
    "https://telegra.ph/file/9fa40e56ee30b280229ae.jpg",
    "https://telegra.ph/file/4c2d5b93a7d4a83d4b05c.jpg",
    "https://telegra.ph/file/4c2d5b93a7d4a83d4b05c.jpg",
    "https://telegra.ph/file/7f4944e2f4918e2be4ca2.jpg",
    "https://telegra.ph/file/a25a5b416c23254e76cd6.jpg",
    "https://telegra.ph/file/2baec11bdc351a3242ec7.jpg",
    "https://telegra.ph/file/1e4a0db7d115f68c67c2d.jpg",
    "https://telegra.ph/file/daebcbcbcaf6965fba555.jpg",
    "https://telegra.ph/file/0ae0fe261a86bfd61e526.jpg",
    "https://telegra.ph/file/6fa047d5a19ee85efe3d2.jpg",
    "https://telegra.ph/file/78af05493d5619ac5c04a.jpg",
    "https://telegra.ph/file/9385d9c7cd30a658741b4.jpg",
    "https://telegra.ph/file/2637397252b8cb407e4f5.jpg",
    "https://telegra.ph/file/6bb8d8bb036f123a089b6.jpg",
    "https://telegra.ph/file/0ae0fe261a86bfd61e526.jpg",
    "https://telegra.ph/file/2e95e06050fafb9c774cd.jpg",
    "https://telegra.ph/file/fb5a6dad800340cdb1e53.jpg",
    "https://telegra.ph/file/6efeadc5461bdb705614c.jpg",
    "https://telegra.ph/file/7a9319b1726175660f539.jpg",
    "https://telegra.ph/file/c4852d75ab288e7b39dd6.jpg",
    "https://telegra.ph/file/ab8265ceab6c2a9b310db.jpg",
    "https://telegra.ph/file/a09787da1386efda688f3.jpg",
    "https://telegra.ph/file/a09787da1386efda688f3.jpg",
    "https://telegra.ph/file/f6159f1073f9df5240ff7.jpg",
    "https://telegra.ph/file/45333aa40e2d09920e3c4.jpg",
    "https://telegra.ph/file/74e39b66613673377c3f6.jpg",
    "https://telegra.ph/file/9dbbd2746a0a4fcb5e96a.jpg",
    "https://telegra.ph/file/0ae0fe261a86bfd61e526.jpg",
    "https://telegra.ph/file/9dbbd2746a0a4fcb5e96a.jpg",
    "https://telegra.ph/file/64584e3ca7cd973689c23.jpg",
    "https://telegra.ph/file/4ed524de8ead9e39d66cc.jpg",
    "https://telegra.ph/file/787b19cb6522d467a51f1.jpg",
    "https://telegra.ph/file/16c574f74e9488a820df5.jpg",
    "https://telegra.ph/file/24d22369a7cd62d0efb71.jpg",
    "https://telegra.ph/file/1fe7fc13a31adc3933fb0.jpg",
    "https://telegra.ph/file/8de2d8454b20e1ba394cd.jpg",
    "https://telegra.ph/file/e69c8eda21230b7cfdfe0.jpg",
    "https://telegra.ph/file/c0ec9bf541de1a099b560.jpg",
    "https://telegra.ph/file/45108112a378b48b37c48.jpg",
    "https://telegra.ph/file/62c946d20a14d9d52be10.jpg",
    "https://telegra.ph/file/1c0593e76f7d1b0af0547.jpg",
]


HELP_TEXT = f"""
𓆩⌬𓆪 UCO Project
"""
