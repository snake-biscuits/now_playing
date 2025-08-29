-- https://support.discogs.com/hc/en-us/articles/360004051833-How-To-Find-Information-On-A-CD

CREATE TABLE IF NOT EXISTS CompactDisc (
   catalog_number  VARCHAR  NOT NULL  UNIQUE,  -- on case spine, includes hyphen(s)
   release_title   VARCHAR  NOT NULL,
   disc_count      INTEGER  NOT NULL,  -- typically 1, idk how to do defaults
   PRIMARY KEY (catalog_number)
);


CREATE TABLE IF NOT EXISTS CDTrack (
    cd       VARCHAR  NOT NULL,
    disc     INTEGER  NOT NULL, -- usually 1
    track    INTEGER  NOT NULL,
    name     VARCHAR  NOT NULL,
    seconds  INTEGER  NOT NULL,  -- length
    FOREIGN KEY cd REFERENCES CompactDisc(catalog_number)
);

 -- TODO: AlbumCD (Album, CompactDisc, disc_number)
 -- TODO: TrackPerformer (CDTrack, name, role)
 -- TODO: TrackLyrics (CDTrack, lyrics_filename)
 -- TODO: CDArt (CompactDisc, image_filename, art_type)
 -- -- ArtType enum table (DiscFront, CaseFront, Booklet+PageNumber, etc.)
 -- -- I want to texture a basic 3D Model as a display
