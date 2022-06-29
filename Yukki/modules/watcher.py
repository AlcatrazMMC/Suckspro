import re
import time
import asyncio

from pyrogram import filters
from pyrogram.types import Message

from Yukki import app, botid, botname, botusername
from Yukki.database import add_served_chat,
from Yukki.helpers import get_readable_time, put_cleanmode

chat_watcher_group = 1

@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(_, message: Message):
    await app.send_sticker(message.chat.id,"CAACAgUAAx0Cak5fVgABBiutYnzuLoHovOpsydapxzdpeGPn4kEAAqcFAALvw7lUqFiXebelCpskBA")





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

