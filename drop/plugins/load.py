import os
import time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from drop.database.storefile_db import *
from drop.database.time_db import *
from drop.Config import MAX_TIME
from drop.helpers.check import check_sudo

max_time = MAX_TIME

# Start Message

@Client.on_message(filters.private & filters.incoming & filters.command("unload"))
async def unload(bot, msg):
    if not check_sudo(msg.chat.id):
        return
    clean_store()
    await msg.reply_text(f"Successfully Unloaded All")


@Client.on_message(filters.private & filters.incoming & filters.command("load"))
async def load(bot, msg):
    if not check_sudo(msg.chat.id):
        return
    editable = await msg.reply_text("Send me File")
    input = await bot.listen(editable.chat.id)
    x = await input.download()
    try:
        with open(x, "r") as f:
            content = f.read()
            new_content = content.split("\n")
            for i in new_content:
                add_store(i)
        lol = get_store()
        await msg.reply_text(f"Successfully Loaded : {len(lol)}") 
        os.remove(x)
    except Exception as e:
        await msg.reply_text(f"ERROR : {e}")
        os.remove(x)
    clean_time()


@Client.on_message(filters.private & filters.incoming & filters.command("drop"))
async def claim(bot, msg):
    user_id = msg.from_user.id
    last_message_times = get_time()
    if user_id in last_message_times:
        return await msg.reply_text("You've already received this drop item or there is no stock. Stay tuned for the next drops!")
    owo = get_store()
    if len(owo) > 0:
        file = owo[0]
        await msg.reply_text(f"Successfully generated your drop! Here it is:\n\n • {file}")
        del_store(file)
        add_time(msg.from_user.id, time.time())
    else:
        return await msg.reply_text(f"You've already received this drop item or there is no stock. Stay tuned for the next drops!")
    
    


"""

@Client.on_message(filters.private & filters.incoming & filters.command("drop"))
async def claim(bot, msg):
    user_id = msg.from_user.id
    last_message_times = get_time()
    if user_id in last_message_times:
        time_since_last_message = time.time() - last_message_times[user_id]
        if time_since_last_message < int(max_time):
            seconds = int(max_time) - time_since_last_message
            seconds = seconds % (24 * 3600)
            hour = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60
            remaining_time = ("%d hours & %02d minutes & %02d seconds " % (hour, minutes, seconds))
            cooldown_message = f"Please wait {remaining_time}.**"
            return await msg.reply_text(cooldown_message)
    owo = get_store()
    if len(owo) > 0:
        file = owo[0]
        await msg.reply_text(f"Successfully generated your drop! Here it is:\n\n • {file}")
        del_store(file)
        add_time(msg.from_user.id, time.time())
    else:
        return await msg.reply_text(f"You've already received this drop item or there is no stock. Stay tuned for the next drops!")
    
"""


    
