import json
import os

from . import utils


root = os.path.expanduser("~/.now_playing/")

# defaults
path = {
    "root": root,
    "pods": os.path.join(root, "Podcasts"),
    "subs": os.path.join(root, "Youtube"),
    "music": os.path.expanduser("~/Music")}


# TODO: config data / files
# - root/queue (rich table)
# - root/nprc (config file)
# - root/user.db
# - pods/.feeds/*.rss
# - pods/Podcast/*.* (audio)
# - pods/subscriptions (rich table)
# - subs/Channel/*.* (video)
# - subs/subscriptions (rich table)

# - NOTE: "rich table" format will likely be `.json`
# - should really handle this with SlopChewy

# TODO: load config file & override paths


def pod_feed(podcast_name: str) -> str:
    podcast_name = utils.sanitise_str(podcast_name)
    return os.path.join(path["pods"], ".feeds", f"{podcast_name}.rss")


def pod_folder(podcast_name: str) -> str:
    podcast_name = utils.sanitise_str(podcast_name)
    return os.path.join(path["pods"], podcast_name)


def pod_subscriptions():
    subscriptions_file = os.path.join(path["pods"], "subscriptions.json")
    with open(subscriptions_file) as json_file:
        subscriptions = json.load(json_file)
    return subscriptions
