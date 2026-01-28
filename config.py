# Developed by Sino (@idseno)
import os

class Config:
    API_ID = int(os.getenv("API_ID", "your_api_id"))  # From Telegram API
    API_HASH = os.getenv("API_HASH", "your_api_hash")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
    SESSION_STRING = os.getenv("SESSION_STRING", "your_assistant_session_string")  # For assistant
    OWNER_ID = int(os.getenv("OWNER_ID", "your_telegram_id"))  # Your ID: @idseno
    OWNER_USERNAME = "@idseno"
    CHANNEL_USERNAME = "@senovip"
    BOT_NAME = "سورس ميوزك سينو"
    NEXGEN_API_KEY = os.getenv("NEXGEN_API_KEY", "your_nexgen_api_key")  # From NexGenBots
    FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL", "@senovip")  # Force subscribe channel
    DEFAULT_LANGUAGE = "ar"  # Arabic default
    MUSIC_IMAGE_URL = "https://source.unsplash.com/featured/?music"  # Default music image
    WELCOME_IMAGE_URL = "https://source.unsplash.com/featured/?welcome,music"  # Welcome image
