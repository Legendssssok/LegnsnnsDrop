import asyncio
import importlib
from pyromod import listen
from pyrogram import Client, idle
from pyrogram.errors import FloodWait

from Drop.Config import API_HASH, API_ID, BOT_TOKEN
from Drop.plugins import ALL_MODULES

from .logger import LOGS

async def Start_DropBot():
    try:
        app = Client(
            "app",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="drop/plugins"),
          )
          await app.start()
    except FloodWait as e:
          LOGS.error(f"Bot Wants to Sleep For {e.value}")
          await asyncio.sleep(e.value + 5)
    except Exception as f:
          LOGS.error(f)
    for all_module in ALL_MODULES:
          importlib.import_module("StringSessionBot.plugins." + all_module)
          LOGS.info(f"➢ Successfully Imported : {all_module}")
    LOGS.info("==============================")
    LOGS.info("🔰Support Group🔰 : @LegendBot_OP")
    LOGS.info("⚜️Update Group⚜️  : @LegendBot_AI")
    LOGS.info("==============================")
    await idle()
