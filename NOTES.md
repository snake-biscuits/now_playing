# Notes

## Tagging

**Option Tags**
Must choose one from the subset

**State Tags**
Tags change within a state machine (python)

> Download.Queued -> InProgress -> Complete

**Tag Transission**
e.g. Podcast `Subscribed.*` -> Episode `Download.Queued`


**Show Segment**
WTYP.TheGoddamNews
WTYP.SafetyThird
TF.Interview
Pod.Intro
Pod.Announcements
Pod.Patreons
Vid.Patreons (get via Sponsorblock?)

 * Subscribed
   - Latest (get the latest episode)
   - Subset (filter)
   - Headlines (tracking updates, no downloads)
   - Binge (everything from the start)
 * Download
   - Queued
   - InProgress
   - Complete
 * Play
   - Queued
   - InProgress
   - Complete
   - Skip
 * Speed
   - 1x (default)
   - 1.25x
   - 1.5x
   - 1.75x
   - 2x
 * Timestam
   - Chapter
   - Highlight



## Grouping
`PodcastChannel` combined subscription modes
 * `Audio.Headlines` + `Video.Latest`



## Subscription Plan
 * Quotas
   - Xhrs/day (vary by weekday)
 * Auto-Queue
   - Mains
     * News
     * Weekly Faves
   - Filler
     * Can skip if falling behind on mains
   - Group by tag / Tag schedule
   - Expected Release Dates
 * Catch Up Queue
   - Episodes cut by auto-queue over last X days
   - Unplayed/Unskipped older episodes
 * Play counter
   - Old Gold / Evergreen Episodes


## Playback
 * Be as hands off as possible
 * Download Queuing
   - multi-threading?
   - progress indicators
   - bandwidth throttling / schedule

### `mpris`
> TODO: playerctl
### `mpv`
> TODO: timestamp tracking
### `mpd`
> TODO: timestamp tracking


## Queue Construction
 * `Pile + Rules -> Dynamic Queue`
 * Related to Subscription Plan
 * Playback Queue informs Download Queue


## `.sql` db

> NOTE: use transactions to track history

```sql
ONCE Version(semver, release_date)

ENUM Media(Podcast, Youtube)

-- Podcasts --
TABLE Podcast(name, short_name, folder, url)
TABLE PodcastEpisode(podcast, title, release_date, runtime, url)
TABLE PodcastDownload(podcast_episode, download_date, filesize, filename)

-- Youtube --
TABLE Channel(name, short_name, folder, url)
TABLE ChannelVideo(channel, title, release_date, runtime, url)
TABLE VideoDownload(channel_video, download_date, filesize, filename)

TABLE PodcastChannel(podcast, channel)  -- yt version

TABLE Subscription(media, podcast/channel, level)
ENUM SubLevel(Everything, SubSeries, Sometimes, Headlines, ...)
-- NOTE: SubSeries is for things like an ongoing LP series
-- TODO: user defined criteria for collecting subseries

-- People --
TABLE Person(name)
TABLE PersonBook(person, book)
TABLE PersonSocials(person, site, url)
ENUM Site(Bluesky, Tumblr, Twitter, ...)

-- Connections --
TABLE Host(media, podcast/channel, person)
TABLE Regular(media, podcast/channel, person)
TABLE EpisodeGuest(media, episode, person)
-- Other People --
TABLE MediaPerson(media, podcast/channel, person, role)
ENUM Role(Producer, Editor, Art, Mentioned, ...)

-- Time --
TABLE Timestamp(media, episode, when, text)
ENUM TimestampType(Chapter, HighlightStart, HighlightEnd, NewsItem, Slide, ...)
TABLE Playback(media, episode, when)  -- current playhead
TABLE PlayedEpisode(media, episode)

-- Tagging --
-- TODO: allow tag negation on a per entry basis
-- TODO: tag searching system
-- TODO: tag sourcing (YT metadata etc.)
TABLE Tag(name, description)
TABLE TagAlias(tag, alias)
TABLE TagGroup(name, style, description)
TABLE TagGrouping(tag, group)
TABLE TagRelation(tag_a, relation, tag_b)  -- Baba Is You inspired system
-- Video Game | in genre | TTRPG
-- TTRPG | subset of | RPG
-- Video Game | subset of | Game
ENUM Relation(in genre, subset of, ...)

-- Tagged Things --
TABLE Tagged(table, id, tag)
-- TODO: auto-tag based on parent group
-- Podcast / Tag trickles down etc.
-- TODO: tag transmission rules
-- TODO: untag
```
