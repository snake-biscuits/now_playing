from __future__ import annotations
from datetime import datetime
import json
# import os
from typing import Any, Dict, Tuple, List


Entry = Dict[str, Any]


class Video:
    _entry: Entry
    video: Tuple[str, str]
    channel: Tuple[str, str]
    date: datetime
    duration: int  # seconds

    def __init__(self):
        # TODO: default values
        self._entry = dict()
        self.video = ("", "")
        self.channel = ("", "")
        self.date = datetime.now()
        self.duration = 0

    def __repr__(self) -> str:
        title, yt_id = self.video
        if len(title) > 64:
            title = f"{title[:61]}..."
        descriptor = f'"{title}" [{yt_id}] {self.runtime}'
        return f"<{self.__class__.__name__} {descriptor} @ 0x{id(self):016X}>"

    @property
    def url(self):
        title, yt_id = self.video
        return f"https://youtube.com/watch?v={yt_id}"

    # TODO: move to utils
    @property
    def runtime(self) -> str:
        if isinstance(self.duration, str):
            return self.duration
        hours = self.duration // (60 * 60)
        minutes = (self.duration // 60) % 60
        seconds = self.duration % 60
        if hours > 0:
            return f"{hours}:{minutes:02d}:{seconds:02d}"
        else:
            return f"{minutes}:{seconds:02d}"

    @classmethod
    def from_entry(cls, entry: Entry) -> Video:
        if entry is None:
            return None
        out = cls()
        out._entry = entry
        out.video = (entry["title"], entry["id"])
        out.channel = (entry["channel"], entry["channel_id"])
        out.date = datetime.utcfromtimestamp(entry["timestamp"])
        out.duration = entry.get("duration", "???")  # media_type == "video"
        # TODO:
        # -- thumbnail
        # -- view_count, likes & dislikes
        # -- description
        # -- tags (youtube tags, not our tags)
        return out

    @classmethod
    def from_url(cls, url: str) -> Video:
        if "://" in url:
            protocol, url = url.split("://")
        domain, divider, basename = url.partition("/")
        basename, divider, args = basename.partition("?")
        args = args.split("&")
        args_dict = {
            key: value
            for key, divider, value in [
                arg.partition("=")
                for arg in args]}
        out = cls()
        out.video = ("???", args_dict["v"])
        return out


# TODO: Thumbnail


class SubsCache:
    videos: List[Video]
    time: datetime

    def __init__(self):
        self.videos = list()
        self.time = datetime.now()

    def __repr__(self):
        # TODO: total runtime
        descriptor = f'{len(self.videos)} videos'
        return f"<{self.__class__.__name__} {descriptor} @ 0x{id(self):016X}>"

    @classmethod
    def from_json(cls, info: Dict[str, Any]) -> SubsCache:
        out = cls()
        out._json = info
        out.videos = [
            Video.from_entry(entry)
            for entry in info["entries"]
            if entry is not None]
        return out

    @classmethod
    def from_file(cls, filename: str) -> SubsCache:
        with open(filename) as json_file:
            info = json.load(json_file)
        out = cls.from_json(info)
        out.time = datetime.strptime(filename[:13], "%Y%m%d-%H%M")
        # out.time = datetime.fromtimestamp(os.path.getmtime(filename))
        return out
