-- NOTE: namescape separator dots are for clarity
-- UI should render these tags in the parent colour
-- full name can be shown in a tooltip, otherwise just the last name
-- UI might also associate some core tags w/ icons / emoji
INSERT INTO Tag(name, details) VALUES
    -- Subscription
    ('Subscribed', NULL),
    ('Subscribed.Latest',
     'download the most recent episode'),
    ('Subscribed.CatchUp',
     'downloading episodes since the last one played'),
    ('Subscribed.Series',
     'using a filter to download episodes that are part of a series'),
    ('Subscribed.Headlines',
     'just keeping up with releases, no downloads'),
    ('Subscribed.Binge',
     'watching all episodes, from the very beginning'),
    -- Download
    ('Download', NULL),
    ('Download.Queued', NULL),
    ('Download.InProgress', NULL),
    ('Download.Complete', NULL),
    ('Download.Skip', NULL),
    -- Play
    ('Play', NULL),
    ('Play.Queued', NULL),
    ('Play.InProgress', NULL),
    ('Play.Complete', NULL),
    ('Play.Skip', NULL),
    -- Speed
    ('Speed', 'playback speed'),
    ('Speed.1x', NULL),
    ('Speed.1.25x', NULL),
    ('Speed.1.5x', NULL),
    ('Speed.1.75x', NULL),
    ('Speed.2x', NULL),
    ('Speed.3x', NULL),
    -- Timestamp
    ('Timestamp', NULL),
    ('Timestamp.Chapter', NULL),
    ('Timestamp.Chapter.ColdOpen', 'Teaser'),
    ('Timestamp.Chapter.Recap', 'Previously On'),
    ('Timestamp.Chapter.OP', 'Opening Theme'),
    ('Timestamp.Chapter.ED', 'Credits Theme'),
    -- TODO: song links for OP & ED
    ('Timestamp.Chapter.Preview', 'Next Time On'),
    ('Timestamp.Chapter.Announcements', 'Housekeeping'),
    ('Timestamp.Chapter.Patreons', NULL),
    ('Timestamp.Chapter.Sponsor', NULL),
    ('Timestamp.Chapter.SelfPromo', 'Like & Subscribe'),
    ('Timestamp.Highlight', NULL),
    -- Shows
    ('Show', NULL),  -- tag the Show's tag w/ this
    -- if a tag tagged w/ show is also present,
    -- then these tags should appear as "ShowName.Subset"
    ('Show.Podcast', 'Podcast of Show'),
    ('Show.MainChannel', 'Youtube Channel of Show'),
    ('Show.HighlightChannel', 'Youtube Channel w/ Show Highlights'),
    -- Show People
    ('Show.Person', NULL),
    ('Show.Person.Host', NULL),
    ('Show.Person.Regular', NULL),
    ('Show.Person.Guest', NULL),
    ('Show.Person.Crew', NULL);  -- editor, producer etc.
    -- TODO:
    -- Language (EN, JP, etc.)
    -- Subtitles (CC, Commentary, Karaoke)

INSERT INTO TagRelation(sub_tag, relation, main_tag) VALUES
    -- Subscribed subsets
    (2, 1, 1),
    (3, 1, 1),
    (4, 1, 1),
    (5, 1, 1),
    (6, 1, 1),
    -- Download subsets
    ( 8, 1, 7),
    ( 9, 1, 7),
    (10, 1, 7),
    (11, 1, 7),
    -- Play subsets
    (13, 1, 12),
    (14, 1, 12),
    (15, 1, 12),
    (16, 1, 12),
    -- Speed subsets
    (18, 1, 17),
    (19, 1, 17),
    (20, 1, 17),
    (21, 1, 17),
    (22, 1, 17),
    (23, 1, 17),
    -- Timestamp subsets
    (25, 1, 24),
    (26, 1, 25),
    (27, 1, 25),
    (28, 1, 25),
    (29, 1, 25),
    (30, 1, 25),
    (31, 1, 25),
    (32, 1, 25),
    (33, 1, 25),
    (34, 1, 25),
    (35, 1, 24);
    -- TODO: Show subsets
