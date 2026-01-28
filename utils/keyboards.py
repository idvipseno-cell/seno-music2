# Developed by Sino (@idseno)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_control_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("▶️", callback_data="play"), InlineKeyboardButton("⏸️", callback_data="pause")],
        [InlineKeyboardButton("⏹️", callback_data="stop"), InlineKeyboardButton("🔄", callback_data="next")]
    ])
