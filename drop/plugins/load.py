from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from drop.database.storefile_db import *

# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("load"))
async def start(bot, msg):
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

