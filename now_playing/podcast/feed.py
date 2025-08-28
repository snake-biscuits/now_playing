# https://datatracker.ietf.org/doc/html/rfc5005
# https://en.wikipedia.org/wiki/XPath
from __future__ import annotations
from datetime import datetime
from typing import List, Tuple, Union

from lxml import etree

from .. import utils


# NOTE: we don't sanitise or check the xml in any way
# -- that's really bad for security
# -- it's not hard to make a malicious feed


class Episode:
    _xml: etree.Element
    # core
    number: Union[int, str]
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
        self.number = "???"
        self.page = ""
        self.title = ""
        self.time = datetime.now()

    def __repr__(self) -> str:
        user_tz = datetime.now().astimezone().tzinfo
        # NOTE: could also use zoneinfo.ZoneInfo("Country/State")
        time = self.time.astimezone(user_tz).strftime("%a, %d %b %Y %H:%M")
        descriptor = f"{time} - {self.title}"
        return f"<{self.__class__.__name__} {descriptor} @ 0x{id(self):016X}>"

    @property
    def filename(self) -> str:
        release = self.time.strftime("%Y%m%d-%H%M")
        ep_no = self.number
        if isinstance(ep_no, int):
            ep_no = f"{ep_no:03d}"
        ep_title = utils.sanitise_str(self.title)
        if len(ep_title) > 64:
            ep_title = f"{ep_title[:63]}-"
        url, mime_type = self.audio_url
        ext = url.rpartition(".")[-1]
        return f"{release}-{ep_no}-{ep_title}.{ext}"

    @classmethod
    def from_element(cls, element: etree.Element) -> Episode:
        # NOTE: rss 2.0 element (atom may be different)
        out = cls()
        out._xml = element

        children = {
            etree.QName(child.tag).localname: child
            for child in element}

        enclosure = children["enclosure"].attrib
        out.audio_url = (enclosure["url"], enclosure["type"])
        out.description = children["description"].text
        out.guid = children["guid"].text
        out.title = children["title"].text
        # optionals
        if "comments" in children:
            out.comments = children["comments"].text
        if "link" in children:
            out.page = children["link"].text
        if "episode" in children:  # itunes:episode
            out.number = int(children["episode"].text)

        publish_time = children["pubDate"].text
        # datetime_from_rfc_822
        # RSS date-times all conform to RFC 822, tho year *can* be 2 character
        # TODO: better time string detection
        last_word = publish_time.split(" ")[-1]
        if not last_word.isalpha():
            # assuming format: "Fri, 11 Jul 2025 10:51:04 +0100"
            out.time = datetime.strptime(
                publish_time, "%a, %d %b %Y %H:%M:%S %z")
        else:
            out.time = datetime.strptime(
                publish_time, "%a, %d %b %Y %H:%M:%S %Z")
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
        if "width" in children and "height" in children:
            out.size = (
                int(children["width"].text),
                int(children["height"].text))
        else:
            out.size = ("?", "?")

        return out


# NOTE: Feeds come in Complete, Paged & Archive variants (RFC 5005)
class FeedFile:
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
        descriptor = f'"{self.title}" ({len(self.episodes)} episodes)'
        return f"<{self.__class__.__name__} {descriptor} @ 0x{id(self):016X}>"

    # TODO: save to db
    # TODO: load from db
    # TODO: update from url
    # -- download a fresh .xml, compare & update

    @classmethod
    def from_atom(cls, atom: etree.ElementTree) -> FeedFile:
        # https://datatracker.ietf.org/doc/html/rfc4287
        out = cls()
        out._xml = atom
        root = atom.getroot()
        assert root.tag == "feed"

        raise NotImplementedError("`.atom` parser not yet implemented")

        return out

    @classmethod
    def from_rss(cls, rss: etree.ElementTree) -> FeedFile:
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
    def from_file(cls, filename: str) -> FeedFile:
        xml = etree.parse(filename)
        root = xml.getroot()
        if root.tag == "rss":
            assert root.get("version") == "2.0"
            return cls.from_rss(xml)
        elif root.tag == "feed":
            return cls.from_atom(xml)
        else:
            raise NotImplementedError(
                f"cannot get feed from XML w/ root: '{root.tag}'")
