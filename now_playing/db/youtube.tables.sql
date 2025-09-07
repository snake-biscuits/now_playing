-- NOTE: urls are generated from guids

CREATE TABLE IF NOT EXISTS Channel (
    name  VARCHAR NOT NULL  UNIQUE,
    guid  VARCHAR NOT NULL  -- @ChannelName etc.
);

CREATE TABLE IF NOT EXISTS ChannelVideo (
    channel       VARCHAR  NOT NULL,
    title         VARCHAR  NOT NULL,
    release_date  VARCHAR  NOT NULL,
    runtime       INTEGER  NOT NULL,
    guid          VARCHAR  NOT NULL  UNIQUE,  -- watch?v={GUID}
    FOREIGN KEY (channel) REFERENCES Channel(guid)
);

CREATE TABLE IF NOT EXISTS VideoDownload (
    video       VARCHAR  NOT NULL  UNIQUE,
    downloaded  VARCHAR  NOT NULL,  -- timestamp
    filesize    INTEGER  NOT NULL,  -- in bytes
    filename    VARCHAR  NOT NULL,
    FOREIGN KEY (video) REFERENCES ChannelVideo(guid)
);
