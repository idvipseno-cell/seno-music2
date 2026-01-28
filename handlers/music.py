# Developed by Sino (@idseno)
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped
import yt_dlp
from config import Config

async def handle_download(client, message):
    query = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
    if not query:
        await message.reply("أرسل اسم الأغنية / Send song name")
        return
    
    # Download using yt-dlp
    ydl_opts = {'format': 'bestaudio', 'outtmpl': 'downloads/%(title)s.%(ext)s'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=True)
        file_path = ydl.prepare_filename(info['entries'][0])
    
    # Send with transparent button and image
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("شغل في القناة", callback_data=f"play_{file_path}")]])
    await client.send_photo(message.chat.id, Config.MUSIC_IMAGE_URL, caption=f"تم تحميل: {query}", reply_markup=keyboard)

async def handle_play(client, message):
    # Assume file_path from callback or message
    file_path = "downloads/song.mp3"  # Placeholder, integrate with download
    chat_id = message.chat.id
    await calls.join_group_call(chat_id, AudioPiped(file_path), stream_type=StreamType().local_stream)
    await message.reply("تم التشغيل / Playing")

async def handle_stop(client, message):
    chat_id = message.chat.id
    await calls.leave_group_call(chat_id)
    await message.reply("تم الإيقاف / Stopped")

async def handle_pause(client, message):
    chat_id = message.chat.id
    await calls.pause_stream(chat_id)
    await message.reply("تم الإيقاف المؤقت / Paused")
