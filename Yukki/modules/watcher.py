import re
import time
import asyncio
import random
from random import choice

import logging

from telethon import TelegramClient

from pyrogram import filters
from pyrogram.types import Message, Chat
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
    "https://telegra.ph/file/257f6ac0c2a892757425b.mp4",
    "https://telegra.ph/file/d17beb37bfcf1fe07832d.mp4",



]

TEXT = [
    "Welcome !! {} 💕\n     🎋Kindly read Group's Description~ \n         🦊 Follow /rules \n            🥂Enjoy your stay.\n                                @{}",
    "Welcome !! {} ❤️\n     📜Kindly read Group's Description~ \n         🦋 Follow /rules \n            🎗️Enjoy your stay.\n                                @{}",
    "Welcome {} 🎋\n        🖥️Hope you're not a bot & crypto seller...\n        🍒Read /rules and enjoy your stay.\n                                @{}",
]

api_id = "16521270"
api_hash = "dba0d7bb9846296c9af84be2edc1d9ab"
session = "1AZWarzYBu02kybmnlGR0ed6ef21Vf2GhSGOjOP0MDjYlxQnmRhMlA59ik0QUW6OOOC5T3AMcrpZcxw_KNK7ziNSQmd2ao23OzZVLsIJjDd2LFJuc1b7QiRnaON9rZliwWOfeOnCc-g-NOIIo5kHV7tWZ5Y1_u0ljCysUiAJVooAShtEMQFzSPd3e0psDd5wMZA0pIcJ7yqXHhZl2NgJOkQIunAqfcvwOCyLiC5bPIDb7OdSDc4kk_hsPzKiapqa08zNzRm7abrEpsDsR6cLeg81_eHKHVdWti-tsbBrfQvSwTkCeDt9LqBdeW2ETJV2tU1VJlH3RKixWswbO2yXSwtErFVd9YYQ="

userbot = TelegramClient('session', api_id, api_hash)

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
    


@userbot.on(event.filters.regex(pattern="kek that doesn't look right. Reply to someone like this:"))
async def kek(userbot, message: Message):
    await asyncio.sleep(3)
    await message.delete()
    


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

