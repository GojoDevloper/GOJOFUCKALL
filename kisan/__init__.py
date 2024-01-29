import asyncio
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram import Client,filters
from pyrogram.types import *
from kisan import config
import logging
from pyrogram.errors import (
    ChatAdminRequired
)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if config.BOT_TOKEN:
  @bot.on_message(filters.command("banall"))
  async def _(bot, msg):
    print("getting memebers from {}".format(msg.chat.id))
    async for i in bot.iter_chat_members(msg.chat.id):
        try:
            await bot.ban_chat_member(chat_id =msg.chat.id,user_id=i.user.id)
            print("kicked {} from {}".format(i.user.id,msg.chat.id))
        except FloodWait as e:
            await asyncio.sleep(e.x)
            print(e)
        except Exception as e:
            print(" failed to kicked {} from {}".format(i.user.id,e))           
    print("process completed")


if config.BOT_TOKEN:
  @bot.on_message(filters.command(["start"]))
  async def hello(bot, message):
  await message.reply_photo(photo=f"https://telegra.ph/file/0dacefd89e48a69b57f2a.jpg",
                              caption=f"ʜᴇʏ,{0}\n◉ɪ ᴀᴍ ᴀ ʙᴀɴᴀʟʟ ʙᴏᴛ.!\n\n\n◉ɪ ᴀᴍ ꜱᴏ ᴘᴏᴡᴇʀ ꜰᴜʟʟ ᴛᴏ ᴄʜᴇᴀᴋ ᴍʏ ᴘᴏᴡᴇʀ ɢɪʙ ᴍᴇ ꜰᴜʟʟ ᴀᴅᴍɪɴ ʀɪɢʜᴛꜱ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ ᴀɴᴅ ᴛʏᴘᴇ  /banall ᴛᴏ ꜱᴇᴇ ᴍᴀɢɪᴄ.",

  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗢𝗪𝗡𝗘𝗥", url=f"https://t.me/{gojo_104}")
                ]
                
           ]
        ),
                           )
