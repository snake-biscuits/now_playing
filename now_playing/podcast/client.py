from datetime import datetime
import os
import urllib

from .. import config
from . import download
from . import feed


# TODO: queue
# TODO: downloaded episodes
# TODO: delete stale downloads
class Client:
    def __init__(self):
        self.feeds = dict()
        self.names = dict()
        self.errors = {
            "download": dict(),
            "parse": dict()}

    def __repr__(self) -> str:
        descriptor = f"{len(self.feeds)} feeds"
        return f"<{self.__class__.__name__} {descriptor} @ 0x{id(self):016X}>"

    def refresh(self):
        subscriptions = config.pod_subscriptions()
        for sub in subscriptions["podcasts"]:
            name, guid, url = sub["name"], sub["guid"], sub["url"]
            self.names[guid] = name
            # create download folder, if needed
            podcast_folder = config.pod_folder(name)
            if not os.path.exists(podcast_folder):
                os.mkdir(podcast_folder)
            # fetch feed file
            # TODO: break out into own method
            # -- update stale feeds (w/ backup)
            feed_fn = config.pod_feed(name)
            if not os.path.exists(feed_fn):
                try:
                    fn = download.feed_file(name, url)
                    assert fn == feed_fn, f"{feed_fn=}, {fn=}"
                except urllib.error.HTTPError as exc:
                    self.errors["download"][guid] = exc
            # parse feed file
            try:
                self.feeds[guid] = feed.FeedFile.from_file(feed_fn)
            except Exception as exc:
                self.errors["parse"][guid] = exc

    def list_episodes(self, guid: str, count: int, direction: int = 1):
        if direction == -1:
            start, stop, step = -1, -count, -1
        else:
            start, stop, step = 0, count, 1
        pod = self.feeds[guid]
        for episode in pod.episodes[start:stop:step]:
            user_tz = datetime.now().astimezone().tzinfo
            local_time = episode.time.astimezone(user_tz)
            release = local_time.strftime("%a, %d %b %Y %H:%M")
            index = pod.episodes.index(episode)
            print(f"{index:03d} | {release} | {episode.title}")

    def download(self, guid: str, index: int) -> str:
        episode = self.feeds[guid].episodes[index]
        podcast_name = self.names[guid]
        return download.episode(podcast_name, episode)
