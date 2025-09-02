CREATE TABLE IF NOT EXISTS TaggableTable (
    name  VARCHAR  NOT NULL  UNIQUE,
);
INSERT INTO TaggableTable(name) VALUES
    -- cd
    ('CDTrack'),
    ('CompactDisc'),
    -- youtube
    ('Channel'),
    ('ChannelVideo'),
    -- time
    ('Timestamp'),
    -- podcast
    ('Podcast'),
    ('PodcastChannel'),
    ('PodcastEpisode'),
    -- tags
    ('Tag'),
    ('Tagged');  -- e.g. Spoiler, Untag Implied Tag

-- NOTE: transmission is implemented in python
CREATE TABLE IF NOT EXISTS Relation (
    name  VARCHAR  NOT NULL  UNIQUE,
);
INSERT INTO Relation(name) VALUES (
    ('is subset of'),
    ('is in genre'),
    ('is author of');
