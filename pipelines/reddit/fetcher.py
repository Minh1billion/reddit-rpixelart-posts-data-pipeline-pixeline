import feedparser
import httpx
from core.logger import get_logger
from core.config import RSS_URL

log = get_logger(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/rss+xml, application/xml, text/xml"
}


def get_image_url(entry) -> str:
    for key in ["media_content", "media_thumbnail"]:
        media = entry.get(key, [])
        if media:
            return media[0].get("url", "")
    return ""


def fetch_entries() -> list[dict]:
    log.info(f"Fetching from: {RSS_URL}")
    response = httpx.get(RSS_URL, headers=HEADERS, follow_redirects=True)
    log.info(f"HTTP status: {response.status_code}")

    feed = feedparser.parse(response.text)
    log.info(f"Entries fetched: {len(feed.entries)}")

    if not feed.entries:
        log.warning("No entries found.")
        return []

    entries = []
    for entry in feed.entries:
        entries.append({
            "id": entry.get("id", entry.link).split("comments/")[-1].split("/")[0],
            "title": entry.title,
            "author": entry.get("author", "unknown"),
            "url": entry.link,
            "image_url": get_image_url(entry),
            "created_utc": entry.published,
            "raw_content": str(entry.get("summary", ""))
        })

    return entries