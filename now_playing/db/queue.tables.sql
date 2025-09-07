CREATE TABLE IF NOT EXISTS QueuedToDownload (
    media        INTEGER  NOT NULL,
    guid         VARCHAR  NOT NULL,
    next         INTEGER,  -- simplifies reshuffling
    downloading  BOOLEAN,  -- NULL=NotYet,True=Now,False=Done
    FOREIGN KEY (media) REFERENCES Media(rowid),
    -- guid -> PodcastEpisode / ChannelVideo (guid)
    FOREIGN KEY (next) REFERENCES QueuedMedia(rowid)
);


CREATE TABLE IF NOT EXISTS QueuedToPlay (
    media    INTEGER  NOT NULL,
    row_id   INTEGER  NOT NULL,
    next     INTEGER,  -- simplifies reshuffling
    playing  BOOLEAN,  -- NULL=NotYet,True=Now,False=Done
    FOREIGN KEY (media) REFERENCES Media(rowid),
    -- row_id -> EpisodeDownload / VideoDownload (rowid)
    FOREIGN KEY (next) REFERENCES QueuedMedia(rowid)
);
