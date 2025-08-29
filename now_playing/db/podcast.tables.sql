CREATE TABLE IF NOT EXISTS Podcast (
    name  VARCHAR NOT NULL  UNIQUE,
    guid  VARCHAR NOT NULL  UNIQUE,  -- abbreviation
    url   VARCHAR NOT NULL,
);

CREATE TABLE IF NOT EXISTS PodcastEpisode (
    podcast       VARCHAR  NOT NULL,
    title         VARCHAR  NOT NULL,  -- title
    guid          VARCHAR  NOT NULL,  -- guid
    release_date  VARCHAR  NOT NULL,  -- pubDate
    runtime       INTEGER  NOT NULL,  -- enclosure.length (seconds)
    url           VARCHAR  NOT NULL,  -- enclosure.url
    FOREIGN KEY (podcast) REFERENCES Podcast(guid),
);

CREATE TABLE IF NOT EXISTS EpisodeDownload (
    episode     VARCHAR  NOT NULL  UNIQUE,
    downloaded  VARCHAR  NOT NULL,  -- timestamp
    filesize    INTEGER  NOT NULL,  -- in bytes
    filename    VARCHAR  NOT NULL,
    FOREIGN KEY (episode) REFERENCES PodcastEpisode(guid),
);
