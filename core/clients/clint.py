# Copyrighted by PLAY-Z 90 | 2024-2025
# Please do not modify any file if you don't know what you are doing.
# --------------------------------------Credits---------------------------------#
# PLAY-Z 90 -> For customizing and improving the bot.
# Original Credits -> Aresona & Sentric Nova for base code.
# Support Channel --> @PLAYZ_HACKING
# Support Group --> @PLAY_Z_HACKING_DISCUSSION
# Please give credits if you fork or modify this bot. Also, join our support channels.

from pyrogram import filters
from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus
from config import API_ID, API_HASH, BOT_TOKEN, LOGGER_GROUP, PHONE_NUMBER

Plugins = dict(root="core.pluiginsx")

# PLAY-Z RESTRICTED SAVING CONTENT BOT Client
class botclient(Client):
        def __init__(self):
                print("Starting PLAY-Z RESTRICTED SAVING CONTENT BOT...")
                super().__init__(
                        name="PLAY-Z_RESTRICTED_BOT",
                        api_id=API_ID,
                        api_hash=API_HASH,
                        bot_token=BOT_TOKEN,
                        in_memory=True,
                        max_concurrent_transmissions=7,
                        plugins=Plugins,
                        )
        async def start(self):
                await super().start()
                self.id = self.me.id
                self.name = self.me.first_name + " " + (self.me.last_name or "")
                self.username = self.me.username
                try:
                        await self.send_message(LOGGER_GROUP, f"**🚀 PLAY-Z RESTRICTED SAVING CONTENT BOT STARTED 🚀**\n\n** Name :** \n{self.name}\n** Username :** \n@{self.username}")
                except (errors.ChannelInvalid, errors.PeerIdInvalid):
                        print("Unable to access log group/channel. Ensure your bot is added to the designated channel/group for logging")
                except Exception as ex:
                        print(f"Bot couldn't access the log group/channel.\nReason: {type(ex).__name__}.\n\n{ex}")
                a = await self.get_chat_member(LOGGER_GROUP, self.id)
                if a.status != ChatMemberStatus.ADMINISTRATOR:
                        print("Kindly promote your bot to admin status in the log group/channel then try later")
                        exit()
                print(f"🌟 {self.name} is now up and running! Say thanks to PLAY-Z 90.")
        async def stop(self):
                await super().stop()

# Userbot session file renamed to "PLAY-Z USER DATA"
userbot = Client("PLAY-Z USER DATA", api_hash=API_HASH, api_id=API_ID, phone_number=PHONE_NUMBER)