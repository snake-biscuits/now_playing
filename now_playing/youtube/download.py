from typing import Any, Dict, List

import yt_dlp

from . import feed


# TODO: Logger class


def playlist_info(url: str, **extra_options) -> Dict[str, Any]:
    """returns json-serialisable yt-dlp info"""
    options = {
        "ignoreerrors": "only_download",
        "quiet": True,
        "simulate": True}
    options.update(extra_options)
    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.sanitize_info(ydl.extract_info(url, download=False))
        # NOTE: it'd be cool if we could yield each entry as we load it
        # -- just for faster paralellism
        # -- progress indicators would be cool too
        # -- a logger class might help enable this
    return info


# NOTE: ideally called in batches w/ the same settings
# -- e.g. sponsorblock modes, chat / subtitles etc.
# -- can also use yt-dlp config files from config folder
def videos(video_list: List[feed.Video], **extra_options) -> int:
    options = {
        "ignoreerrors": "only_download",
        "quiet": True,
        "simulate": False}
    options.update(extra_options)
    with yt_dlp.YoutubeDL(options) as ydl:
        error_code = ydl.download([video.url for video in video_list])
        return error_code
