CREATE TABLE IF NOT EXISTS pixel_art_posts (
    id          TEXT PRIMARY KEY,
    title       TEXT,
    author      TEXT,
    url         TEXT,
    image_url   TEXT,
    created_utc TEXT,
    fetched_at  TEXT,
    raw_content TEXT
);