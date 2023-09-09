from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup

# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg):
    user = await bot.get_me()
    mention = user.mention
    await bot.send_message(msg.chat.id, "Thank you for joining, you've been subscribed to our bot. When we do a drop, you will receive a notification. ❤️")
