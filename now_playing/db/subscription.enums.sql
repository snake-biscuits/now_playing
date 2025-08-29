CREATE TABLE IF NOT EXISTS Media (
    name  VARCHAR  NOT NULL  UNIQUE,
);

INSERT INTO Media(name) VALUES
    ('Podcast'),
    ('Channel');  -- YouTube


CREATE TABLE IF NOT EXISTS SubPattern (
    name  VARCHAR  NOT NULL  UNIQUE,
);

INSERT INTO SubPattern(name) VALUES
    ('Everything'),  -- get every episode
    ('SubSeries'),  -- categorised subset
    ('Sometimes'),  -- grazing for filler
    ('Headlines');  -- just the titles thanks
