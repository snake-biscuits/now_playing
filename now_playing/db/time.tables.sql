CREATE TABLE IF NOT EXISTS Timestamp (
    media       INTEGER  NOT NULL,
    episode     VARCHAR  NOT NULL,
    start_time  VARCHAR  NOT NULL,
    end_time    VARCHAR,  -- use NULL for single point markers (or chapter start)
    title       VARCHAR,
    details     VARCHAR
);
