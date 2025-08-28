import os
from urllib.request import Request, urlopen

from .. import config
from . import feed


def get_file(url: str, dest_filename: str, mime_type: str = None) -> int:
    header = {
        "User-Agent": "now_playing/25.8 (podcast client)",
        "Accept": mime_type if mime_type is not None else "*/*",
        "Accept-Charset": "utf-8",
        "Accept-Language": "en-AU,en"}
    response = urlopen(Request(url, headers=header))
    # TODO: validate response
    # TODO: download progress bar
    # -- [####.....] ??% ?/???MB @ ??? Kb/s | filename
    # TODO: mkdirs
    with open(dest_filename, "wb") as out_file:
        out_file.write(response.read())
    return os.path.getsize(dest_filename)


# TODO: check os.path.getmtime before re-downloading feeds
def feed_file(podcast_name: str, feed_url: str) -> str:
    dest_filename = config.pod_feed(podcast_name)
    mime_types = [
        "aplication/atom+xml;q=0.8"
        "application/rdf+xml;q=0.6"
        "application/rss+xml",
        "application/xml;q=0.4",
        "text/xml;q=0.4"]
    download_size = get_file(feed_url, dest_filename, ",".join(mime_types))
    assert download_size > 0
    return dest_filename


# TODO: check to see if episode is already downloaded
def episode(podcast_name: str, episode: feed.Episode) -> str:
    url, mime_type = episode.audio_url
    filename = episode.filename
    dest_filename = os.path.join(config.pod_folder(podcast_name), filename)
    download_size = get_file(url, dest_filename, mime_type)
    assert download_size > 0
    return dest_filename
