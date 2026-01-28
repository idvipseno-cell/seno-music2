# Developed by Sino (@idseno)
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

async def handle_dev_panel(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("إذاعة", callback_data="broadcast"), InlineKeyboardButton("اشتراك إجباري", callback_data="forcesub")]
    ])
    await message.reply("لوحة التحكم المطور:", reply_markup=keyboard)

async def handle_broadcast(client, message):
    # Broadcast logic (send to all chats)
    await message.reply("أرسل الرسالة للإذاعة / Send message to broadcast")

async def handle_force_sub(client, message):
    # Force subscribe logic
    await message.reply("تم تفعيل الاشتراك الإجباري / Force sub enabled")
