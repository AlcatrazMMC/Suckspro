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
    "Okaerinasai {} !!!\n\n Hope you'll stay Long with us!💙💚❤️💛\n      ★ @{} read /rules to make yourself at home★ 

]

api_id = "16521270"
api_hash = "dba0d7bb9846296c9af84be2edc1d9ab"

userbot = TelegramClient('session', apu_id , api_hash))

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
    


@userbot.on_message(filters.regex(pattern="kek that doesn't look right. Reply to someone like this:") & filters.chat(Var.GROUPS))
async def kek(ub, message):
    await asyncio.sleep(7)
    await message.delete()
    
@userbot.on_message(filters.regex(pattern="You've been offered a waifu trade!") & filters.chat(Var.GROUPS))
async def trade(ub, message):
    await asyncio.sleep(30)
    await message.delete()
    
@userbot.on_message(filters.regex(pattern="rip, the waifu has run away already...") & filters.chat(Var.GROUPS))
async def ran(ub, message):
    await asyncio.sleep(4)
    async for m in ub.search_messages(message.chat.id, query='A qt waifu appeared!', limit=1):
        await m.delete()
    await asyncio.sleep(20)
    await message.delete()
    
@userbot.on_message(filters.regex(pattern="rip, that's not quite right...") & filters.chat(Var.GROUPS))
async def rip(ub, message):
    await asyncio.sleep(3)
    await message.delete()
    
@userbot.on_message(filters.regex(pattern="OwO you protecc'd") & filters.chat(Var.GROUPS))
async def done(ub, message):
    await asyncio.sleep(4)
    async for m in ub.search_messages(message.chat.id, query='A qt waifu appeared!', limit=1):
        await m.delete()
    await asyncio.sleep(6)
    await message.delete()
    
@userbot.on_message(filters.regex(pattern="Top harems in") & filters.chat(Var.GROUPS))
async def top(ub, message):
    await asyncio.sleep(60)
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

