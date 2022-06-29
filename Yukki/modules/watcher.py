import re
import time
import asyncio
import random 

from pyrogram import filters
from pyrogram.types import Message

from Yukki import app, botid, botname, botusername
from Yukki.database import add_served_chat
from Yukki.helpers import get_readable_time, put_cleanmode

chat_watcher_group = 1
welcome_group = 2

WELCOME = [
    "https://telegra.ph/file/b67d161998858575f6e1a.jpg",
    "https://telegra.ph/file/0ae0fe261a86bfd61e526.jpg",
    "https://telegra.ph/file/344f4bec8e26def7e723a.mp4",
]

WLMTEXT = [
    "hiii",
    "yooo",
    "Fuck",
]



@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(_, message: Message):
    image = random.choice(WELCOME)
    wtext = random.choice(WLMTEXT)
    await message.reply_photo(photo=image, caption=wtext)





@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(_, message: Message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            if member.id == botid:
                send =  await message.reply_text(
                    f"Thanks for having me in {message.chat.title}\n\n{botname} is alive."
                )
                await put_cleanmode(message.chat.id, send.message_id)
        except:
            return

