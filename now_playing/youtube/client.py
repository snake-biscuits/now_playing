from datetime import datetime
import json
from typing import Any, Dict

from .. import config
from . import download
from . import feed


# TODO: organise & present client.cache.videos
# -- tags / channel category (db)
# -- group by channel
# -- flag watched (db)
# TODO: queue
# TODO: downloaded episodes
# TODO: delete stale downloads
class Client:
    cache: feed.SubsCache

    def __init__(self):
        self.cache = feed.SubsCache()

    def __repr__(self) -> str:
        descriptor = f"{len(self.videos)} videos"
        return f"<{self.__class__.__name__} {descriptor} @ 0x{id(self):016X}>"

    def refresh(self, limit: int = 50, **extra_options):
        latest_feed = config.sub_latest_feed()
        # TODO: update on stale timer
        # -- datetime.now() - cache_date > stale_limit
        if latest_feed is None:  # empty cache
            # TODO: logger
            latest_feed = self.latest_info(limit, **extra_options)
            # save cache
            fetch_time = datetime.now().strftime("%Y%m%d-%H%M")
            filename = config.sub_cache_file(
                f"{fetch_time}-{limit}-subscriptions.json")
            with open(filename, "w") as json_file:
                json.dump(latest_feed, json_file)
        self.cache = feed.SubsCache.from_json(latest_feed)

    def latest_info(self, limit: int = 50, **extra_options) -> Dict[str, Any]:
        options = {
            "cookiesfrombrowser": ("firefox",),
            "ignoreerrors": "only_download",
            "lazy_playlist": True,
            "playlistend": limit,
            "quiet": True,
            "simulate": True}
        options.update(extra_options)
        info = download.playlist_info(":ytsubs", **options)
        return info

    # TODO:
    # -- list (filter)
    # -- download
