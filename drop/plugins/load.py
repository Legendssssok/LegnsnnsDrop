import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from drop.database.storefile_db import *
from drop.database.time_db import *
from drop.Config import MAX_TIME

max_time = MAX_TIME

# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("load"))
async def load(bot, msg):
    editable = await msg.reply_text("Send me File")
    input = await bot.listen(editable.chat.id)
    x = await input.download()
    try:
        with open(x, "r") as f:
            content = f.read()
            new_content = content.split("\n")
            for i in new_content:
                add_store(i)
        os.remove(x)
        lol = get_store()
        await msg.reply_text(f"Successfully Loaded : {len(lol)}") 
    except Exception as e:
        await msg.reply_text(f"ERROR : {e}")
        os.remove(x)


@Client.on_message(filters.private & filters.incoming & filters.command("claim"))
async def claim(bot, msg):
    last_message_times = get_time()
    time_since_last_message = time.time() - last_message_times[user_id]
    if time_since_last_message < int(max_time):
        remaining_time = int(max_time) - time_since_last_message
        cooldown_message = f"Please wait {int(remaining_time / 60)} minutes & {int(remaining_time % 60)} seconds before posting another message to the channel.\n\n**Your post is added to queue & will be posted after {int(remaining_time / 60)} minutes & {int(remaining_time % 60)} seconds automatically.**"
        return await message.reply_text(cooldown_message)
    owo = get_store()
    file = owo[0]
    await msg.reply_text(f"Successfully generated your drop! Here it is:\n\n • {file}")
    del_store(file)
    
    


    
