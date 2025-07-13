# https://datatracker.ietf.org/doc/html/rfc5005
# https://en.wikipedia.org/wiki/XPath
from __future__ import annotations
from datetime import datetime
from typing import List, Tuple
from urllib.request import urlretrieve

from lxml import etree
# NOTE: we don't sanitise or check the xml in anyway
# -- that's really bad for security
# -- it's not hard to make a malicious feed

# https://trashfuturepodcast.podbean.com/
# url = "https://feed.podbean.com/trashfuturepodcast/feed.xml"


# NOTE: could use `requests` for asyncronyous downloads
# -- can have a loading bar this way
# -- stackoverflow example w/ `tqdm`:
# -- https://stackoverflow.com/a/10744565
# from tqdm import tqdm
# import requests
# url = "http://download.thinkbroadband.com/10MB.zip"
# response = requests.get(url, stream=True)
# with open("10MB", "wb") as handle:
#     for data in tqdm(response.iter_content(chunk_size=1024), unit="kB"):
#         handle.write(data)
def download(feed_url: str, podcast_name: str) -> str:
    # NOTE: could use "urllib.request.urlopen" to parse in-memory
    # -- keeping a cache would be nicer tho
    # -- don't need to flood podcast servers w/ traffic
    # TODO: get "tmp/" folder from config
    # -- should be a cache of some kind
    # -- expose controls to flush / refresh cache to the user
    # -- as well as date information (up-to-date check)
    # TODO: use same extension as feed_url
    filename, message = urlretrieve(feed_url, f"tmp/{podcast_name}.rss")
    # TODO: validate message (http.client.HTTPMessage)
    # NOTE: file should always be xml (can verify in HTTPMessage headers)
    # -- possible extensions: ".atom", ".rss", ".xml"
    return filename


# TODO: download & cache audio
# -- playback handled by another module (ui?)
# -- playback state handled by db (speed, progress etc.)
class Episode:
    # core
    title: str
    audio_url: Tuple[str, str]  # url, mime-type
    # metadata
    comments: str  # url
    description: str  # html
    guid: str  # url?
    page: str  # url
    time: datetime

    def __init__(self):
        self.audio_url = ("", "")
        self.comments = ""
        self.description = ""
        self.guid = ""
        self.page = ""
        self.title = ""
        self.time = datetime.now()

    def __repr__(self) -> str:
        user_tz = datetime.now().astimezone().tzinfo
        # NOTE: could also use zoneinfo.ZoneInfo("Country/State")
        time = self.time.astimezone(user_tz).strftime("%a, %d %b %Y %H:%M")
        descriptor = f"{time} - {self.title}"
        return f"<{self.__class__.__name__} {descriptor} @ 0x{id(self):016X}>"

    @classmethod
    def from_element(cls, element: etree.Element) -> Episode:
        # NOTE: rss 2.0 element (atom may be different)
        out = cls()

        children = {
            child.tag: child
            for child in element}

        enclosure = children["enclosure"].attrib
        out.audio_url = (enclosure["url"], enclosure["type"])
        out.comments = children["comments"].text
        out.description = children["description"].text
        out.guid = children["guid"].text
        out.page = children["link"].text
        out.title = children["title"].text

        publish_time = children["pubDate"].text
        # assuming format: "Fri, 11 Jul 2025 10:51:04 +0100"
        # RSS date-times all conform to RFC 822, tho year *can* be 2 character
        out.time = datetime.strptime(publish_time, "%a, %d %b %Y %H:%M:%S %z")
        # NOTE: RFC 5005 lists multiple time formats, might need a regex switch
        return out


# TODO: download & cache image
# -- display handled by ui
class Artwork:
    page: str
    size: Tuple[int, int]
    title: str
    url: str

    def __init__(self):
        self.page = ""
        self.size = (0, 0)
        self.title = ""
        self.url = ""

    def __repr__(self) -> str:
        width, height = self.size
        descriptor = f"{self.title} {width}x{height}"
        return f"<{self.__class__.__name__} {descriptor} @ 0x{id(self):016X}>"

    @classmethod
    def from_element(cls, element: etree.Element) -> Artwork:
        # NOTE: rss 2.0 element (atom may be different)
        out = cls()

        children = {
            child.tag: child
            for child in element}

        out.url = children["url"].text
        out.title = children["title"].text
        out.page = children["link"].text
        out.size = (
            int(children["width"].text),
            int(children["height"].text))

        return out


# NOTE: Feeds come in Complete, Paged & Archive variants (RFC 5005)
class Feed:
    _xml: etree.ElementTree  # for debug
    artwork: Artwork
    description: str  # html
    episodes: List[Episode]
    page: str  # url
    title: str

    def __init__(self):
        self._xml = None
        self.artwork = Artwork()
        self.description = ""
        self.episodes = list()
        self.path = ""
        self.title = ""

    def __repr__(self) -> str:
        descriptor = f"{self.title} ({len(self.episodes)} episodes)"
        return f"<{self.__class__.__name__} {descriptor} @ 0x{id(self):016X}>"

    # TODO: save to db
    # TODO: load from db
    # TODO: update from url
    # -- download a fresh .xml, compare & update

    @classmethod
    def from_atom(cls, atom: etree.ElementTree) -> Feed:
        # https://datatracker.ietf.org/doc/html/rfc4287
        out = cls()
        out._xml = atom
        root = atom.getroot()
        assert root.tag == "feed"

        raise NotImplementedError("`.atom` parser not yet implemented")

        return out

    @classmethod
    def from_rss(cls, rss: etree.ElementTree) -> Feed:
        # https://en.wikipedia.org/wiki/RSS
        # https://www.rssboard.org/rss-specification
        out = cls()
        out._xml = rss
        root = rss.getroot()
        assert root.tag == "rss"
        assert root.get("version") == "2.0"
        # TODO: check root.nsmap (namespaces)

        channel = rss.xpath("/rss/channel")[0]

        out.title = channel.xpath("title")[0].text
        out.page = channel.xpath("link")[0].text
        out.description = channel.xpath("description")[0].text

        # TODO: optional metadata
        # -- lastBuildDate
        # -- category
        # -- copyright
        # -- generator
        # -- language
        # -- ttl (time to live; minutes until cache should refresh; 1440m=24h)

        # NOTE: "image" element is optional
        # -- so we use a for loop
        # -- could be wierd if there's multiple image tags for some reason
        for image in channel.xpath("image"):
            out.artwork = Artwork.from_element(image)
            # NOTE: some podcasts can have per-episode art too
            # -- is this part of the itunes spec?

        out.episodes = [
            Episode.from_element(item)
            for item in channel.xpath("item")]

        return out

    @classmethod
    def from_file(cls, filename: str) -> Feed:
        xml = etree.parse(filename)
        root = xml.getroot()
        if root.tag == "rss" and root.get("version") == "2.0":
            return cls.from_rss(xml)
        elif root.tag == "feed":
            return cls.from_atom(xml)
        else:
            raise NotImplementedError(
                f"cannot get feed from XML w/ root: '{root.tag}'")
