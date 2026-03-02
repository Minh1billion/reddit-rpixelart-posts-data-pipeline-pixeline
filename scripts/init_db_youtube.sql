CREATE TABLE youtube_thumbnails (
    id           TEXT PRIMARY KEY,  
    channel_id   TEXT NOT NULL,
    channel_name TEXT,
    title        TEXT,
    thumbnail_url TEXT,
    published_at TIMESTAMPTZ,
    fetched_at   TIMESTAMPTZ
);