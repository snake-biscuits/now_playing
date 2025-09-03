-- from podcast.tables import Podcast
-- from youtube.tables import Channel
-- from subscription.enums import Media, SubPattern

CREATE TABLE IF NOT EXISTS Subscription (
    media    INTEGER  NOT NULL,
    outlet   VARCHAR  NOT NULL,
    pattern  INTEGER  NOT NULL,
    -- NOTE (media, outlet) must be unqiue
    FOREIGN KEY (media) REFERENCES Media(rowid),  -- Podcast or Channel
    -- outlet references either Podcast or Channel
    FOREIGN KEY (pattern) REFERENCES SubPattern(rowid)
);

CREATE TABLE IF NOT EXISTS PodcastChannel (
    podcast  VARCHAR  NOT NULL,
    channel  VARCHAR  NOT NULL,
    -- flag for highlight channel / video episodes?
    FOREIGN KEY (podcast) REFERENCES Podcast(name),
    FOREIGN KEY (channel) REFERENCES Channel(guid)
);
