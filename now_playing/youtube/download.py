from typing import Any, Dict, List

import yt_dlp


# TODO: feed.Video.from_json(entry)
Video = Dict[str, Any]
# ^ {"id": str, ...}
VideoList = List[Video]


def subscriptions_list(since: str = "now-1day", limit: int = 50) -> VideoList:
    options = {
        "cookiesfrombrowser": ("firefox",),
        "daterange": yt_dlp.utils.DateRange(start=since),
        "ignoreerrors": "only_download",
        "lazy_playlist": True,
        "playlistend": limit,
        "quiet": True,
        "simulate": True}
    # TODO: use a logger rather than "quiet"

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.sanitize_info(ydl.extract_info(":ytsubs", download=False))

    # collect everything we need to present to the user
    # let them decide on downloads etc.
    keys = (
        "id", "title",
        "channel_id", "channel",
        "upload_date", "timestamp",
        "media_type", "duration",
        "thumbnail", "view_count", "description")

    videos = [
        {key: entry.get(key, None) for key in keys}
        for entry in info["entries"]
        if entry is not None]

    # NOTE: daterange doesn't appear to be filtering out videos
    # TODO: fine, I'll do it myself.

    return videos


# TODO: download youtube videos
# -- sponsorblock settings from config
# -- or just use a yt-dlp config file
