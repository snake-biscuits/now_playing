from __future__ import annotations
from datetime import datetime
import os
import shutil
from typing import Dict, Tuple
import urllib

from .. import config
from . import download
from . import feed


class Client:
    errors: Dict[str, Dict[str, Exception]]
    # ^ {"download/parse": {"guid": Error}}
    feeds: Dict[str, feed.FeedFile]
    # ^ {"guid": FeedFile}
    subscriptions: Dict[str, Tuple[str, str]]
    # ^ {"guid": ("name", "url")}

    def __init__(self):
        self.errors = {
            "download": dict(),
            "parse": dict()}
        self.feeds = dict()
        self.subscriptions = dict()
        # boot
        self.fetch_subscriptions()

    def __repr__(self) -> str:
        descriptor = f"{len(self.feeds)} feeds"
        return f"<{self.__class__.__name__} {descriptor} @ 0x{id(self):016X}>"

    # subscriptions
    def fetch_subscriptions(self):
        subscriptions = config.pod_subscriptions()
        # TODO: check .feeds for untracked .rss / .xml
        # -- add to subscriptions.json
        # -- generate GUID (capitals / first letters of title)
        for sub in subscriptions["podcasts"]:
            name, guid, url = sub["name"], sub["guid"], sub["url"]
            self.subscriptions[guid] = (name, url)
            self.update_feed(guid)

    # feeds
    def feed_filename(self, guid: str) -> str:
        name, url = self.subscriptions[guid]
        return config.pod_feed(name)

    def update_feed(self, guid: str, now=False):
        feed_file = self.feed_filename(guid)
        if now:
            shutil.move(feed_file, feed_file + ".bak")
            self.download_feed(guid)
        elif os.path.exists(feed_file):
            self.fetch_feed(guid)
            assert guid not in self.errors["parse"]
            feed = self.feeds[guid]
            minutes_old = (datetime.now() - feed.time).total_seconds() / 60
            if minutes_old > feed.ttl:
                print(f'"{guid}" is stale! updating...')
                shutil.move(feed_file, feed_file + ".bak")
                self.download_feed(guid)
        else:  # no FeedFile
            self.download_feed(guid)
        self.fetch_feed(guid)

    def download_feed(self, guid: str):
        if guid in self.errors["download"]:
            self.errors["download"].pop(guid)
        name, url = self.subscriptions[guid]
        feed_file = self.feed_filename(guid)
        try:
            filename = download.feed_file(name, url)
            assert filename == feed_file, f"{feed_file=}, {filename=}"
        except urllib.error.HTTPError as exc:
            self.errors["download"][guid] = exc

    def fetch_feed(self, guid: str):
        if guid in self.errors["parse"]:
            self.errors["parse"].pop(guid)
        feed_fn = self.feed_filename(guid)
        try:
            self.feeds[guid] = feed.FeedFile.from_file(feed_fn)
        except FileNotFoundError as exc:  # inform caller
            raise exc
        except Exception as exc:  # log parse failure
            self.errors["parse"][guid] = exc

    # episodes
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

    def list_all_episodes(self, count: int, direction: int = 1):
        for guid, (name, url) in self.subscriptions.items():
            print("===", name, f"({guid})", "===")
            self.list_episodes(guid, count, direction)

    def download(self, guid: str, index: int) -> str:
        episode = self.feeds[guid].episodes[index]
        podcast_name, url = self.subscriptions[guid]
        return download.episode(podcast_name, episode)

    # TODO: list downloaded episodes
    # TODO: delete stale / watched episodes (w/ logging)
