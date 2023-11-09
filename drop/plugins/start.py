from datetime import datetime
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
    await bot.send_message(msg.chat.id, "BOT INFORMATION\n/help - shows this message\n/drop - claim drop\n/invite - invites to the server")
    add_users(msg.chat.id)


@Client.on_message(filters.private & filters.incoming & filters.command("stats"))
async def stats(bot, msg):
    id = get_users()
    file = get_store()
    await bot.send_message(msg.chat.id, f"Total Users = {len(id)}\n\nTotal File Stored = {len(file)}")

@Client.on_message(filters.private & filters.incoming & filters.command("send"))
async def send(bot, msg):
    id = get_users()
    lol = await msg.reply_text("Send me Broadcast Message\n\nTo Cancel : Click /cancel")
    br_msg = await bot.listen(lol.chat.id)
    success = 0
    fail = 0
    if br_msg.text == "/cancel":
       return await msg.reply_text("Cancelled Successfully")
    start = datetime.now()
    for i in id:
        try:
            await bot.send_message(int(i), br_msg.text)
            success += 1
        except BaseException:
            fail += 1
    end = datetime.now()
    time_taken = (end - start).seconds
    await bot.send_message(msg.chat.id, 
                           f"""
**Broadcast completed in {time_taken} seconds.**
Total Users in Bot - {len(id)}
**Sent to** : `{success} users.`
**Failed for** : `{fail} user(s).`""",
                          )


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
