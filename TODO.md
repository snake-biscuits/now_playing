# TODOs

 - [x] `youtube`
   - [x] `feed` (`yt-dlp`)
   - [x] `download` (`yt-dlp`)
   - [x] `client`
 - [x] `podcast`
   - [x] `feed` (`lxml`)
   - [x] `download` (`urllib`)
   - [x] `client`
 - [ ] `playback`
   - [ ] `mpv` wrapper
   - [ ] slight rollback on unpause (user configurable)
 - [ ] `ui`
   - [ ] manage
     - [ ] queue
     - [ ] subscriptions
       - [ ] add new (external search API)
     - [ ] downloads
     - [ ] playback
       - [ ] speed
   - [ ] system tray
 - [ ] `db`
   - [x] essentials
     - [x] subscriptions & downloads
       - [x] podcasts
       - [x] youtube
     - [x] playhead
     - [x] timestamps
     - [x] tags
     - [x] queue
   - [ ] subscriptions / queue / history
     - [ ] use sql transactions
   - [ ] people
   - [ ] tags
     - [x] essential tags (`tag.data.sql`)
     - [ ] user tag definitions (via `ui`)
 - [ ] automated processing
   - [ ] description parser
   - [ ] group filters (title regex, runtime etc.)
   - [ ] references & citations
 - [ ] CDs (original focus)
   - [x] database
   - [ ] archiving (ripping)
   - [ ] artwork
   - [ ] playback / queue
 - [ ] bonus
   - [ ] transcripts
   - [ ] per-show EQ / volume / playback speed
   - [ ] scheduling
     - [ ] releases
     - [ ] tasks (e.g. fold laundry + audio media)
       - [ ] gaming
       - [ ] reading
       - [ ] TV episodes
       - [ ] exercise
       - [ ] meals
       - [ ] screen break
       - [ ] chill before bed
     - [ ] sleep mode (end of chapter)
   - [ ] books
     - [ ] comics
     - [ ] audio-books
     - [ ] schedule reading time
   - [ ] MPRIS / playerctl
     * [mpris-python](https://github.com/airtower-luna/mpris-python) (315 lines)
       - [pydbus](https://github.com/LEW21/pydbus)
     * [mpris-notifier](https://github.com/l1na-forever/mpris-notifier/)
       - almost useful, but annoyingly limited
       - a good reference to build on tho
   - [ ] notifications
     - [ ] "Now Playing: ..."
     - [ ] Animated Thumbnails
     - [ ] MTV / VH1 style Overlay
   - [ ] waybar module (like system tray)
   - [ ] rich presence
   - [ ] Studio
     - [ ] mix deck to play around w/ music & samples
     - [ ] Live DJ/VJ
     - [ ] YTP editor (VeeDee)
   - [ ] Live Stream Playback
     - [ ] Watch Live
     - [ ] Danmaku Chat

### `mpv` direct url playback w/ `yt-dlp`
 * Pros:
   - Simple
   - No Caching Required
   - No Download Queue Management
 * Cons:
   - Less controls (quality / codec etc.)
   - No offline copies
   - Buffering


## Bonus Goals
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
[*YES*](https://doc.qt.io/qtforpython-6/examples/example_widgets_desktop_systray.html)
See Also: [Media Player Example](https://doc.qt.io//qtforpython-6/examples/example_qtdemos_mediaplayer.html)


## Download Rules
`Tags -> Download Flags`
 * Sponsorblock settings
 * `Lang.JP and !Lang.EN -> --write-subs=en`
 * `StreamVoD/Premiere -> --write-chat`
 * `CommentarySubs -> --write-subs=en`


[^assimp]: assimp on GitHub: [Integrate "tinyusdz" project](https://github.com/assimp/assimp/pull/5628)
