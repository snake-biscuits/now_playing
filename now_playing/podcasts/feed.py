# https://datatracker.ietf.org/doc/html/rfc5005
# https://en.wikipedia.org/wiki/RSS
# https://en.wikipedia.org/wiki/XPath
# https://www.w3.org/2005/Atom
from urllib.request import urlretrieve

from lxml import etree

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
    filename, message = urlretrieve(feed_url, f"tmp/{podcast_name}.rss")
    # TODO: validate message (http.client.HTTPMessage)
    return filename


class PodcastFeed:
    xml: etree.ElementTree

    def __init__(self):
        self.xml = None
        # TODO: default empty-ish xml

    def __repr__(self) -> str:
        descriptor = ...
        f"<{self.__class__.__name__} {descriptor} @ 0x{id(self):016X}>"

    def parse_xml(self):
        if self.xml is None:
            raise RuntimeError("no feed data!")
        raise NotImplementedError()
        # TODO: parse RSS / Atom feed (what's the difference?)
        # -- artwork
        # -- release dates
        # -- episode titles
        # -- episode descriptions
        # -- episode files (audio download)
        root = self.xml.root()
        assert root.get("version") == "2.0"
        # TODO: check root.nsmap (namespaces)

        # accessing element data
        # index as a list to get children
        # `.keys()` / `.items()` / `.attrib` to get attributes
        # `.tag` for xml tag
        # `.text` for inner text

        # image = root.xpath("/rss/channel/image")[0]
        # tag: url, text: https://*.png
        # tag: title, text: TRASHFUTURE
        # tag: link, text: https://trashfuture.co.uk
        # tag: width, text: 144
        # tag: height, text: 144

        # episodes = root.xpath("/rss/channel/item")
        # tags = {
        #     'comments',
        #     'description',
        #     'enclosure',
        #     'guid',
        #     'link',
        #     'pubDate',
        #     'title',
        #     '{http://purl.org/rss/1.0/modules/content/}encoded',
        #     '{http://www.itunes.com/dtds/podcast-1.0.dtd}author',
        #     '{http://www.itunes.com/dtds/podcast-1.0.dtd}block',
        #     '{http://www.itunes.com/dtds/podcast-1.0.dtd}duration',
        #     '{http://www.itunes.com/dtds/podcast-1.0.dtd}episode',
        #     '{http://www.itunes.com/dtds/podcast-1.0.dtd}episodeType',
        #     '{http://www.itunes.com/dtds/podcast-1.0.dtd}explicit',
        #     '{http://www.itunes.com/dtds/podcast-1.0.dtd}summary',
        #     '{http://www.itunes.com/dtds/podcast-1.0.dtd}title'}

        # NOTE: RFC 5005 lists multiple date formats, might need a regex filter
        # episode.get("pubDate") -> "Fri, 11 Jul 2025 10:51:04 +0100" ->
        # datetime.datetime.strptime(..., "%a, %d %b %Y %H:%M:%S %z")

    @classmethod
    def from_file(cls, rss_filename: str):
        out = cls()
        out.xml = etree.parse(rss_filename)
        out.parse_xml()
        return out
