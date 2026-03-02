import os
from dotenv import load_dotenv

env_file = os.getenv("ENV_FILE", ".env.dev")
load_dotenv(env_file)

# Database
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Reddit
RSS_URL = os.getenv("RSS_URL", "https://www.reddit.com/r/PixelArt/.rss")

# Youtube
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
YOUTUBE_CHANNEL_IDS = [
    cid.strip()
    for cid in os.getenv("YOUTUBE_CHANNEL_IDS", "").split(",")
    if cid.strip()
]

# Environment
ENV = os.getenv("ENV", "development")