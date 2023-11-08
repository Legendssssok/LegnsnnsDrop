from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from drop.Config import INVITE_LINK
# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg):
    user = await bot.get_me()
    mention = user.mention
    await bot.send_message(msg.chat.id, "Thank you for joining, you've been subscribed to our bot. When we do a drop, you will receive a notification. ❤️")


@Client.on_message(filters.private & filters.incoming & filters.command("invite"))
async def invite(bot, msg):
    user = await bot.get_me()
    mention = user.mention
    await bot.send_message(msg.chat.id, f"Here's the channel link : {INVITE_LINK}.You will be notified there when there is a new drop.")



@Client.on_message(filters.private & filters.incoming & filters.command("/help"))
async def hlp(bot, msg):
    user = await bot.get_me()
    mention = user.mention
    await bot.send_message(msg.chat.id, "BOT INFORMATION\n/help\n - shows this message\n/drop - claim drop\n/invite - invites to the server")
