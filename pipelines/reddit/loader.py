from datetime import datetime
from supabase import create_client
from core.config import SUPABASE_URL, SUPABASE_KEY
from core.logger import get_logger

log = get_logger(__name__)


def load(entries: list[dict]):
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    incoming_ids = [e["id"] for e in entries]
    existing = supabase.table("pixel_art_posts") \
        .select("id") \
        .in_("id", incoming_ids) \
        .execute()
    existing_ids = {row["id"] for row in existing.data}

    new_count = len(entries) - len(existing_ids)
    log.info(f"Already in DB: {len(existing_ids)} | New: {new_count}")

    records = []
    for entry in entries:
        is_new = entry["id"] not in existing_ids
        log.info(f"  {'[NEW]' if is_new else '[DUP]'} {entry['title'][:60]}")
        records.append({**entry, "fetched_at": datetime.utcnow().isoformat()})

    supabase.table("pixel_art_posts").upsert(records).execute()
    log.info(f"Done. Pushed {len(records)} records ({new_count} new, {len(existing_ids)} updated).")