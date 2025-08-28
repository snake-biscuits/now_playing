from datetime import datetime
import os
import urllib

from .. import config
from . import download
from . import feed


# TODO: queue
# TODO: downloaded episodes
class Client:
    def __init__(self):
        self.feeds = dict()
        self.errors = {
            "download": dict(),
            "parse": dict()}

    def refresh(self):
        subscriptions = config.pod_subscriptions()
        for sub in subscriptions["podcasts"]:
            name, url = sub["name"], sub["url"]
            # create download folder, if needed
            podcast_folder = config.pod_folder(name)
            if not os.path.exists(podcast_folder):
                os.mkdir(podcast_folder)
            # fetch feed file
            feed_fn = config.pod_feed(name)
            if not os.path.exists(feed_fn):
                try:
                    fn = download.feed_file(name, url)
                    assert fn == feed_fn, f"{feed_fn=}, {fn=}"
                except urllib.error.HTTPError as exc:
                    self.errors["download"][name] = exc
            # parse feed file
            try:
                self.feeds[name] = feed.FeedFile.from_file(feed_fn)
            except Exception as exc:
                self.errors["parse"][name] = exc

    def list_episodes(self, podcast_name: str, count: int, direction: int = 1):
        if direction == -1:
            start, stop, step = -1, -count, -1
        else:
            start, stop, step = 0, count, 1
        pod = self.feeds[podcast_name]
        for episode in pod.episodes[start:stop:step]:
            user_tz = datetime.now().astimezone().tzinfo
            local_time = episode.time.astimezone(user_tz)
            release = local_time.strftime("%a, %d %b %Y %H:%M")
            index = pod.episodes.index(episode)
            print(f"{index:03d} | {release} | {episode.title}")

    def download(self, podcast_name: str, index: int) -> str:
        episode = self.feeds[podcast_name].episodes[index]
        return download.episode(podcast_name, episode)
