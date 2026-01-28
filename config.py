# Developed by Sino (@idseno)
import os
from dotenv import load_dotenv  # Added for .env loading

load_dotenv()  # Load .env file

class Config:
    API_ID = int(os.getenv("API_ID", "your_api_id"))
    API_HASH = os.getenv("API_HASH", "your_api_hash")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
    SESSION_STRING = os.getenv("SESSION_STRING", "your_assistant_session_string")
    OWNER_ID = int(os.getenv("OWNER_ID", "your_telegram_id"))
    OWNER_USERNAME = "@idseno"
    CHANNEL_USERNAME = "@senovip"
    BOT_NAME = "سورس ميوزك سينو"
    NEXGEN_API_KEY = os.getenv("NEXGEN_API_KEY", "your_nexgen_api_key")
    FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL", "@senovip")
    DEFAULT_LANGUAGE = "ar"
    MUSIC_IMAGE_URL = "https://source.unsplash.com/featured/?music"
    WELCOME_IMAGE_URL = "https://source.unsplash.com/featured/?welcome,music"
