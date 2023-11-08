import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from drop.database.storefile_db import *

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
    owo = get_store()
    file = owo[0]
    await msg.reply_text(f"You Have Successfully Claimed\n\n • {file}")
    del_store(file)
    


    
