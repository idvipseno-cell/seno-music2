# Developed by Sino (@idseno)
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pytgcalls import GroupCall  # Updated import
from pytgcalls.types import AudioPiped, AudioQuality  # Added for compatibility
import yt_dlp
from config import Config

# Note: Pass GroupCall instance here or import it
# Assuming calls is passed or global

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

async def handle_play(client, message, calls):  # Added calls parameter
    # Assume file_path from callback or message
    file_path = "downloads/song.mp3"  # Placeholder, integrate with download
    chat_id = message.chat.id
    await calls.join(chat_id)  # Updated method
    await calls.start_audio(file_path, AudioQuality.HIGH)  # Updated for GroupCall
    await message.reply("تم التشغيل / Playing")

async def handle_stop(client, message, calls):  # Added calls parameter
    chat_id = message.chat.id
    await calls.leave(chat_id)  # Updated method
    await message.reply("تم الإيقاف / Stopped")

async def handle_pause(client, message, calls):  # Added calls parameter
    chat_id = message.chat.id
    await calls.set_pause(chat_id, True)  # Updated method
    await message.reply("تم الإيقاف المؤقت / Paused")
