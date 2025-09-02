-- from tag.enums.sql import Relation, TaggableTable


CREATE TABLE IF NOT EXISTS Tag (
    name         VARCHAR  NOT NULL  UNIQUE,
    description  VARCHAR,
);
-- NOTE: a tag can be a link to another table
-- might need some special indicator for these tags
-- or just tag them...
-- TODO: generate & link a tag for every podcast & person
-- TODO: IP tag that links to both podcast & channel
-- or maybe "MediaProperty" would be a better name
-- "Watched"/"Listened" can also be expressed as a tag

CREATE TABLE IF NOT EXISTS Tagged (
    tag       INTEGER  NOT NULL,
    category  INTEGER  NOT NULL,
    row_id    INTEGER  NOT NULL,
    untag     BOOLEAN,  -- NULL == false
    FOREIGN KEY (tag) REFERENCES Tag(rowid),
    FOREIGN KEY (cat) REFERENCES TaggableTable(rowid),
);

CREATE TABLE IF NOT EXISTS TagAlias (
    tag    INTEGER  NOT NULL,
    alias  VARCHAR  NOT NULL  UNIQUE,
    FOREIGN KEY (tag) REFERENCES Tag(rowid),
);

-- Baba Is You inspired system
-- NOTE: tag transmission (inheritance) will be handled by python
CREATE TABLE IF NOT EXISTS TagRelation (
    sub_tag   INTEGER  NOT NULL,
    relation  INTEGER  NOT NULL,
    main_tag  INTEGER  NOT NULL,
    FOREIGN KEY (sub_tag) REFERENCES Tag(rowid),
    FOREIGN KEY (main_tag) REFERENCES Tag(rowid),
);
-- e.g. TTRPG | is subset of | RPG
