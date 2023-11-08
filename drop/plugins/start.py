from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from drop.Config import INVITE_LINK
from drop.database.users_db import *
from drop.database.storefile_db import *

# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg):
    user = await bot.get_me()
    mention = user.mention
    await bot.send_message(msg.chat.id, "Thank you for joining, you've been subscribed to our bot. When we do a drop, you will receive a notification. ❤️")
    add_users(msg.chat.id)


@Client.on_message(filters.private & filters.incoming & filters.command("stats"))
async def stats(bot, msg):
    id = get_users()
    file = get_store()
    await bot.send_message(msg.chat.id, f"Total Users = {len(id)}\n\nTotal File Stored = {len(file)}")


@Client.on_message(filters.private & filters.incoming & filters.command("invite"))
async def invite(bot, msg):
    user = await bot.get_me()
    mention = user.mention
    await bot.send_message(msg.chat.id, f"Here's the channel link : {INVITE_LINK}.You will be notified there when there is a new drop.")



@Client.on_message(filters.private & filters.incoming & filters.command("help"))
async def hlp(bot, msg):
    user = await bot.get_me()
    mention = user.mention
    await bot.send_message(msg.chat.id, "BOT INFORMATION\n/help - shows this message\n/drop - claim drop\n/invite - invites to the server")
