# Copyrighted by PLAY-Z 90 (2025)
# Unauthorized modifications are not allowed.
# --------------------------------------Credits---------------------------------#
# PLAY-Z 90 -> For coding, optimizing, and enhancing features.
# Special Thanks to Sentric Nova & Aresona for initial ideas.
# Official Support:
# - Channel: @PLAYZ_HACKING
# - Group: @PLAY_Z_HACKING_DISCUSSION
# - Owner: @PLAYZ_90
# If you use or modify this bot, give proper credits & join our support channel.

import os
import asyncio
from pyrogram import filters
from core import userbot, app
from pyrogram.types import Message
from config import OWNER_ID, SUDO_USERS, LOGGER_GROUP
from pyrogram.errors import FloodWait
from pyrogram.enums import ChatType


is_busy = False


@app.on_message(filters.command("save") & filters.user(SUDO_USERS))
async def save(client, message, ub=userbot):
    global is_busy
    if is_busy:
        return await message.reply_text("Bot is already busy, please wait.")

    saved, failed = 0, 0
    msg_splited = message.text.split(" ")
    if len(msg_splited) == 3:
        msgs_ids = []
        start_from, end_here = int(msg_splited[1]), int(msg_splited[2])
        chat_id = message.chat.id

        if start_from > end_here:
            start_from, end_here = end_here, start_from

        try:
            info = await message.reply_text("⏳ **Loading messages...**")
            async for msg in ub.get_chat_history(chat_id=chat_id, min_id=start_from, max_id=end_here):
                if msg.media:
                    msgs_ids.append(msg.id)

            await info.edit_text(f"⌛ **Saving {len(msgs_ids)} messages...**")
            is_busy = True

            for save_msg_id in msgs_ids:
                try:
                    await app.copy_message(chat_id, chat_id, save_msg_id)
                    saved += 1
                except FloodWait as t:
                    await asyncio.sleep(t.value)
                    await app.copy_message(chat_id, chat_id, save_msg_id)
                    saved += 1
                except:
                    failed += 1
                    continue

            await message.reply_text(f"{saved} messages saved successfully. {failed} failed.")
            is_busy = False
        except Exception as err:
            await message.reply_text(f"Error: {err}")
            try:
                await info.delete()
            except:
                pass
            return
    else:
        is_busy = False
        return await message.reply_text("Wrong command format!\n\n**Example:**\n/save 234234 2342387")


@app.on_message(filters.command("free") & filters.user(SUDO_USERS))
async def free_bot(client, message):
    global is_busy
    if not is_busy:
        return await message.reply_text("Bot is not in busy mode.")
    else:
        is_busy = False
        return await message.reply_text(f"Busy status reset by {message.from_user.mention}")