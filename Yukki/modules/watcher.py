import re
import time
import asyncio
import random
from random import choice

from pyrogram import filters
from pyrogram.types import Message
from Yukki.database.cleanmode import cleanmode_off, cleanmode_on, is_cleanmode_on
from Yukki import app, botid, botname, botusername
from Yukki.database import add_served_chat
from Yukki.helpers import get_readable_time, put_cleanmode

chat_watcher_group = 1
welcome_group = 2

MEDIA = [
    "https://telegra.ph/file/b3f1436554fb96a11f72c.mp4",
    "https://telegra.ph/file/b388ae18f088edae90128.mp4",
    "https://telegra.ph/file/344f4bec8e26def7e723a.mp4",
]

TEXT = [
    "Welcome !! {} 💕\n     🎋Kindly read Group's Description~ \n         🦊 Follow /rules \n            🥂Enjoy your stay.\n                                @{}",
    "Welcome !! {} ❤️\n     📜Kindly read Group's Description~ \n         🦋 Follow /rules \n            🎗️Enjoy your stay.\n                                @{}",
]



@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(_, message: Message):
    vedia = random.choice(MEDIA)
    notes = random.choice(TEXT)
    name1 = message.from_user.mention
    name2 = message.from_user.username
    chat_id = message.chat.id
    await add_served_chat(chat_id)
    send = await message.reply_video(vedia, caption=notes.format(name1, name2))
    await put_cleanmode(message.chat.id, send.message_id)
    




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

