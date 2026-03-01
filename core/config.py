import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
RSS_URL = os.getenv("RSS_URL", "https://www.reddit.com/r/PixelArt/.rss")
ENV = os.getenv("ENV", "development")