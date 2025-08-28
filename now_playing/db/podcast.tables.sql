CREATE TABLE IF NOT EXISTS Podcast (
    name  VARCHAR NOT NULL  UNIQUE,
    url   VARCHAR NOT NULL,
);

CREATE TABLE IF NOT EXISTS PodcastEpisode (
    podcast       INTEGER  NOT NULL,
    title         VARCHAR  NOT NULL,  -- title
    guid          VARCHAR  NOT NULL,  -- guid
    release_date  VARCHAR  NOT NULL,  -- pubDate
    runtime       INTEGER  NOT NULL,  -- enclosure.length (seconds)
    url           VARCHAR  NOT NULL,  -- enclosure.url
);

CREATE TABLE IF NOT EXISTS PodcastDownload (
    podcast_episode, download_date, filesize, filename
);
