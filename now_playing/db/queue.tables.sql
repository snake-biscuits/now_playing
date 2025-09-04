-- NOTE: queue should be updated w/ sql transactions
CREATE TABLE IF NOT EXISTS QueuedMedia (
    media    INTEGER  NOT NULL,
    id       INTEGER  NOT NULL,  -- EpisodeDownload / VideoDownload
    next     INTEGER,  -- simplifies reshuffling
    playing  BOOLEAN,  -- NULL=Unplayed,True=Playing,False=Played
    FOREIGN KEY (media) REFERENCES Media(rowid),
    FOREIGN KEY (next) REFERENCES QueuedMedia(rowid)
);
