# Developed by Sino (@idseno)
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

async def handle_start(client, message):
    user = message.from_user
    lang = message.text.split()[-1] if len(message.text.split()) > 1 else Config.DEFAULT_LANGUAGE
    
    if lang not in ["ar", "en"]:
        lang = Config.DEFAULT_LANGUAGE
    
    # Language selection if first time
    if not hasattr(user, 'language') or user.language != lang:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("العربية", callback_data="lang_ar"), InlineKeyboardButton("English", callback_data="lang_en")]
        ])
        await message.reply("اختر اللغة / Choose language:", reply_markup=keyboard)
        return
    
    # Welcome message
    welcome_text = f"""
- Hi? {user.first_name}
سورس ميوزك سينو
- تخصصي تشغيل الميوزك في المكالمات
- سريع وقوي مع مميزات رائعة
- منصات التشغيل المدعومة: يوتيوب - سبوتيفاي - ريسو - ابل ميوزك - ساوندكلود
لـ تصفح الاوامر افرغ زر قائمة الاوامر
    """
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("اضفني لمجموعتك", url=f"https://t.me/{client.username}?startgroup=true")],
        [InlineKeyboardButton("المساعدة", callback_data="help"), InlineKeyboardButton("المطور", url=f"https://t.me/{Config.OWNER_USERNAME}")],
        [InlineKeyboardButton("قناة المطور", url=f"https://t.me/{Config.CHANNEL_USERNAME}")]
    ])
    await message.reply_photo(Config.WELCOME_IMAGE_URL, caption=welcome_text, reply_markup=keyboard)
