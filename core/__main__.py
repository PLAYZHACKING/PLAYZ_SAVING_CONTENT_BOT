# Copyrighted by PLAY-Z 90 | 2025
# Please do not modify any file if you don't know what you're doing.
# --------------------------------------Credits---------------------------------#
# PLAY-Z 90 -> For ideas and making it short.
# Support Channel --> @PLAYZ_HACKING
# Support Group --> @PLAY_Z_HACKING_DISCUSSION
# Please give credits if you fork or modify.

import asyncio, config
from config import LOGGER_GROUP
from pyrogram import idle
from core import app, userbot

async def init():
    await app.start()
    try:
        print("ASSISTANT STARTING")
        with await userbot.start():
            print("ASSISTANT STARTED")
            try:
                await userbot.join_chat("PLAYZ_HACKING")
                await userbot.join_chat("PLAY_Z_HACKING_DISCUSSION")
                await userbot.send_message(LOGGER_GROUP, "Assistant is started!")
            except:
                pass
    except Exception as err:
        print(err)
    await idle()
    await app.stop()
    try:
        await userbot.stop()
    except:
        pass
    print("Bot has been stopped!")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())