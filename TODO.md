# TODOs

 - [ ] Youtube
   - [x] Feed Parser
     - [x] `yt-dlp`
   - [x] Download
     - [x] Python: `yt-dlp`
   - [ ] Playback
     - [ ] Python: `mpv`
 - [ ] Podcasts
   - [x] Feed Parser
     - [x] Python: `lxml`
   - [x] Download
     - [x] Python: `urllib`
   - [ ] Playback
     - [ ] Python: `mpv`

> NOTE: Python `mpv` can run `yt-dlp` directly to play URLs
> -- Pros:
> --  * Simple
> --  * No Caching Required
> --  * No Download Queue Management
> -- Cons:
> --  * Less controls (quality / codec etc.)
> --  * No offline copies
> --  * Buffering


## Collecting Youtube Subscriptions w/ `yt-dlp`
```bash
$ yt-dlp
  :ytsubs
  --cookies-from-browser firefox
  --lazy-playlist
  --dateafter today-0days
  --playlist-end 50
  --simulate
  --print "%(release_date,upload_date)s | %(channel)s | %(title)s"
```

> using `--playlist-end 50` since `--break-on-reject` breaks on livestreams
> can also use `yt-dlp` to download thumbnails or "storyboard"
> TODO: get `id` & `channel_id` & assemble a `.json`


## Podcasts
 * Manage Downloads
 * Queue
 * Sources
   - Apple Podcasts
   - RSS feeds
   - YouTube / Twitch VoD (keep a link in DB)
   - ... there are others
 * Playback speed
 * Remember position between sessions
   - Rollback a few seconds on pause/play
 * skip ~15s forward / back
 * Host & Guest Database
   - Star Chart
   - Other Media Connections (YT, TV etc.)
 * Groups (Same Producer, Similar Category)
 * Description Formatting
   - Cite works referenced / focus of episode
 * Timestamps
   - Pause / Stop at chapter
 * Transcripts
   - Rich Text? (links etc.)
 * Per-podcast audio balancing
 * Release Schedule Calendar


## MPRIS controls
 * allows playerctl to handle play/pause etc.
 * [mpris-python](https://github.com/airtower-luna/mpris-python) (315 lines)
   - [pydbus](https://github.com/LEW21/pydbus)
 * [mpris-notifier](https://github.com/l1na-forever/mpris-notifier/)
   - almost useful, but annoyingly limited
   - a good reference to build on tho


## Waybar module
 * quick controls


## Config
```python
os.path.expanduser("~/.config/now-playing/config.jsonc")
# can python parse .jsonc? what about .ron?
```


## Bonus Goals
 * Rich Presence
   - track data
   - playhead
 * Videogames
   - schedule playtime
   - howlongtobeat integration?
   - retroachievements?
   - PSN? Steam? GOG?
 * TV Episodes
   - add to calendar
 * Books
   - calibre?
 * External Sites
   - backlogged
   - letterboxed
   - myanimelist
 * Studio
   - Live DJ/VJ your media collection
   - Pull Samples from Podcasts & Videos
   - Make YTP w/ VeeDee
 * Task Scheduling
   - Exercise playlist
   - Chill Music Before Bed
   - Second Screen Content Only
   - Touch Grass
 * Live Streams
   - is it possible w/ yt-dlp & mpv?
   - how many features will still work?


## Multiple Sources
 * Castle Super Beast
   - Audio
   - Timestamps Doc
   - Youtube Clips
   - Twitch VoD
   - Twitch Chat
     * XML
     * Danmaku Playback
     * Highlight key info / VIPs
     * Chat Velocity Timeline
 * Well There's Your Problem
   - Youtube Slides
   - John Madden-ing
   - Devon Interjections

### Download Settings
 - No Download (Only Track Updates)
 - Audio Only
 - Video Only


## Youtube
 - [ ] subscriptions
   - [x] info `.json`
   - [ ] shorts (check yt-dlp issues)
   - [ ] download
     - [ ] thumbnails
     - [ ] "storyboards"
     - [ ] videos
     - [ ] progress indicator(s)
 - [ ] tag rules
   - [ ] playback speed
   - [ ] audio only
   - [ ] main screen content vs. second screen content
 - [ ] auto-tagging
   - [ ] channel tag transmission
   - [ ] duration & `media_type` filters
 - [ ] timestamps
   - [ ] chapter > highlight heirarchy
   - [ ] colour coding
   - [ ] from sponsorblock
   - [ ] from comments
     - [ ] prioritise pinned / hearted
     - [ ] common user id / keyword for channel (e.g. "<vtuber>cord")
     - [ ] auto-tag & filter (e.g. ignore "TSKR")
 - [ ] subtitles
   - [ ] commentary
   - [ ] non-english
   - [ ] karaoke
   - [ ] live chat replay

> NOTE: I don't care about machine-generated subs & dubs
> TODO: tag / link JP & EN channel variants


## System Tray
Is it possible w/ Qt?


## Download Rules
`Tags -> Download Flags`
 * Sponsorblock settings
 * `Lang.JP and !Lang.EN -> --write-subs=en`
 * `StreamVoD/Premiere -> --write-chat`
 * `CommentarySubs -> --write-subs=en`


[^assimp]: assimp on GitHub: [Integrate "tinyusdz" project](https://github.com/assimp/assimp/pull/5628)
