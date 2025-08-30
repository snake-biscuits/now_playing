from datetime import datetime
import fnmatch
import json
import os
from typing import Any, Dict

from . import utils


root = os.path.expanduser("~/.now_playing/")

# defaults
path = {
    "root": root,
    "pods": os.path.join(root, "Podcasts"),
    "subs": os.path.join(root, "Youtube"),
    "music": os.path.expanduser("~/Music")}


# TODO: config data / files
# - root/queue.txt (rich table)
# - root/nprc (config file)
# - root/user.db
# - pods/.feeds/*.rss
# - pods/.feeds/subscriptions.json (rich table)
# - pods/Podcast/*.* (audio)
# - subs/Channel/*.* (video)
# - subs/.feeds/subscriptions.json (rich table)

# - NOTE: "rich table" format will likely be `.json`
# - should really handle this with SlopChewy

# TODO: load config file & override paths

# TODO: mkdirs if not exists


def pod_feed(podcast_name: str) -> str:
    podcast_name = utils.sanitise_str(podcast_name)
    return os.path.join(path["pods"], ".feeds", f"{podcast_name}.rss")


def pod_folder(podcast_name: str) -> str:
    podcast_name = utils.sanitise_str(podcast_name)
    folder = os.path.join(path["pods"], podcast_name)
    if not os.path.exists(folder):
        os.mkdir(folder)
    return folder


def pod_subscriptions() -> Dict[str, Any]:
    subscriptions_file = os.path.join(
        path["pods"], ".feeds", "subscriptions.json")
    with open(subscriptions_file) as json_file:
        subscriptions = json.load(json_file)
    return subscriptions


def sub_cache_dir() -> str:
    return os.path.join(path["subs"], ".feeds")


def sub_cache_file(filename: str) -> str:
    return os.path.join(sub_cache_dir(), filename)


def sub_latest_feed() -> (datetime, Dict[str, Any]):
    candidates = fnmatch.filter(
        os.listdir(sub_cache_dir()), "*-subscriptions.json")
    if len(candidates) == 0:
        return None
    candidates_dates = {
        datetime.strptime(fn[:13], "%Y%m%d-%H%M"): fn
        for fn in candidates}
    fetch_date, filename = sorted(candidates_dates.items())[0]
    filename = sub_cache_file(filename)
    with open(filename) as json_file:
        subscriptions = json.load(json_file)
    return subscriptions
