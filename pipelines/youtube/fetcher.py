import httpx
from core.config import YOUTUBE_API_KEY, YOUTUBE_CHANNEL_IDS
from core.logger import get_logger
from typing import List, Dict

log = get_logger(__name__)

PLAYLIST_URL = "https://www.googleapis.com/youtube/v3/playlistItems"

def _uploads_playlist_id(channel_id: str) -> str:
    return "UU" + channel_id[2:]

def fetch_channel(channel_id: str, max_results: int = 50) -> List[Dict]:
    playlist_id = _uploads_playlist_id(channel_id)
    log.info(f"Fetching channel: {channel_id}")

    params = {
        "part": "snippet",
        "playlistId": playlist_id,
        "maxResults": max_results,
        "key": YOUTUBE_API_KEY,
    }
    response = httpx.get(PLAYLIST_URL, params=params, timeout=10)
    log.info(f"HTTP status: {response.status_code}")

    items = response.json().get("items", [])
    log.info(f"Videos found: {len(items)}")

    entries = []
    for item in items:
        snippet = item["snippet"]
        video_id = snippet["resourceId"]["videoId"]
        thumbs = snippet.get("thumbnails", {})

        thumb_url = (
            thumbs.get("maxres")
            or thumbs.get("high")
            or thumbs.get("medium")
            or thumbs.get("default")
            or {}
        ).get("url", "")

        entries.append({
            "id": video_id,
            "channel_id": channel_id,
            "channel_name": snippet.get("channelTitle", ""),
            "title": snippet["title"],
            "thumbnail_url": thumb_url,
            "published_at": snippet.get("publishedAt", ""),
        })

    return entries


def fetch_entries() -> List[Dict]:
    all_entries = []
    for channel_id in YOUTUBE_CHANNEL_IDS:
        try:
            entries = fetch_channel(channel_id)
            all_entries.extend(entries)
        except Exception as e:
            log.error(f"Failed to fetch channel {channel_id}: {e}")  
    log.info(f"Total videos fetched: {len(all_entries)}")
    return all_entries