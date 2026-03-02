from datetime import datetime
from supabase import create_client
from core.config import SUPABASE_URL, SUPABASE_KEY
from core.logger import get_logger
from typing import List, Dict

log = get_logger(__name__)

def load(entries: List[Dict]):
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    incoming_ids = [e["id"] for e in entries]
    existing = supabase.table("youtube_thumbnails") \
        .select("id") \
        .in_("id", incoming_ids) \
        .execute()
    existing_ids = {row["id"] for row in existing.data}

    log.info(f"Already in DB: {len(existing_ids)}")
    log.info(f"New videos: {len(entries) - len(existing_ids)}")

    records = []
    for entry in entries:
        is_new = entry["id"] not in existing_ids
        log.info(f"  {'[NEW]' if is_new else '[DUP]'} {entry['title'][:60]}")
        records.append({**entry, "fetched_at": datetime.utcnow().isoformat()})

    supabase.table("youtube_thumbnails").upsert(records).execute()
    log.info(f"Done. Pushed {len(records)} records.")