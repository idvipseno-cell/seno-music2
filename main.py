# Developed by Sino (@idseno) - Music Bot Source Sino
# Channel: @senovip
# This bot is for playing music in Telegram calls and channels with advanced features.

import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pytgcalls import PyTgCalls
from config import Config
from handlers import start_handler, music_handler, dev_handler
from utils.helpers import auto_leave_assistant

# Initialize bot and assistant
app = Client("music_bot", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)
assistant = Client("assistant", api_id=Config.API_ID, api_hash=Config.API_HASH, session_string=Config.SESSION_STRING)
calls = PyTgCalls(assistant)

# Start the bot
@app.on_message(filters.command("start"))
async def start(client, message):
    await start_handler.handle_start(client, message)

# Music commands (Arabic and English)
@app.on_message(filters.regex(r"^(يوت|تنزيل|نزل|انطيني|download|yt)$"))
async def download_music(client, message):
    await music_handler.handle_download(client, message)

@app.on_message(filters.regex(r"^(شغل|تشغيل|ابدي|play|start)$"))
async def play_music(client, message):
    await music_handler.handle_play(client, message)

@app.on_message(filters.regex(r"^(اوكف|سكب|stop)$"))
async def stop_music(client, message):
    await music_handler.handle_stop(client, message)

@app.on_message(filters.regex(r"^(ايقاف مؤقت|pause)$"))
async def pause_music(client, message):
    await music_handler.handle_pause(client, message)

# Developer commands
@app.on_message(filters.user(Config.OWNER_ID) & filters.command("devpanel"))
async def dev_panel(client, message):
    await dev_handler.handle_dev_panel(client, message)

@app.on_message(filters.user(Config.OWNER_ID) & filters.command("broadcast"))
async def broadcast(client, message):
    await dev_handler.handle_broadcast(client, message)

@app.on_message(filters.user(Config.OWNER_ID) & filters.command("forcesub"))
async def force_sub(client, message):
    await dev_handler.handle_force_sub(client, message)

# Auto leave assistant after 300 seconds
async def auto_leave_task():
    while True:
        await asyncio.sleep(300)
        await auto_leave_assistant(assistant)

async def main():
    await app.start()
    await assistant.start()
    await calls.start()
    asyncio.create_task(auto_leave_task())
    await app.idle()

if __name__ == "__main__":
    asyncio.run(main())
