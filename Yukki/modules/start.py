import time
import asyncio

from pyrogram import Client
import os
import random
from random import choice

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import MessageNotModified

from Yukki import app, boot, botname, botusername
from Yukki.database.cleanmode import cleanmode_off, cleanmode_on, is_cleanmode_on
from Yukki.helpers import get_readable_time, put_cleanmode, RANDOM, HELP_TEXT

@app.on_callback_query(filters.regex("CLEANMODE"))
async def on_cleanmode_change(client, CallbackQuery):
    admin = await app.get_chat_member(CallbackQuery.message.chat.id, CallbackQuery.from_user.id)
    if admin.status in ["creator", "administrator"]:
        pass
    else:
        return await CallbackQuery.answer("Only Admins can perform this action.", show_alert=True)
    await CallbackQuery.answer()
    status = None
    if await is_cleanmode_on(CallbackQuery.message.chat.id):
        await cleanmode_off(CallbackQuery.message.chat.id)
    else:
        await cleanmode_on(CallbackQuery.message.chat.id)
        status = True
    buttons = settings_markup(status)
    try:
        return await CallbackQuery.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    except MessageNotModified:
        return

@app.on_message(filters.command(["dsp"]))
async def on_private_help(_, message: Message):
    return await message.reply_text(f"✅ ALIVE.)

@app.on_message(filters.command(["protecc","protecc@Collect_yours_waifus_bot","protecc@Collect_your_husbando_bot","protecc@loli_harem_bot" ]))
async def sex(_, message: Message):
    await asyncio.sleep(5)
    await message.delete()


