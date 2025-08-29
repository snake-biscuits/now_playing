# UI Notes

## Web Interface
Would be nice to offer up, could control locally w/ my phone
Maybe even web playback?
Being able to do layout in html & css
Haven't gotten deep into trying that, but would still like to try


## Migrate Database
Database might change in future versions, need a process to update the database
Fingerprinting the old database's table definitions might be a cool approach


## Playback
seeing lots of small-time apps using vlc or mpv on the backend
mpv + mpd could be interesting
`QtMultimedia.QAudio`? [Example](https://doc.qt.io/qtforpython-6.5/examples/example_multimedia_audiooutput.html)

 * [python-mpv](https://github.com/jaseg/python-mpv)


## Disc Visualiser
 * Inspired by Sega Dreamcast's `0GDTEX.PVR`

 * Slide out of album cover to reveal disc
 * Disc Art
 * Rotate yaw-wise, showing shiny side
 * Slide back into cover

 * Generate a `.gif`?
 * Needs to be animated w/ transparency
 * APNG? SVG?

 * alpha channel for top side print 
   - some cds let the shine through
 * holographic material / shader
   - animated frames w/ a transition tied to view angle
   - like this: [holographic card](https://www.youtube.com/watch?v=ifZBfhl_Zmk)


## Vinyl View
Good for full albums / podcasts
Progress indicator with a coloured spiral
Move the stylus to seek
"Scratch" w/ touch or click + drag
Change RPM to change speed (podcasts)

Can also do a separate texture for the vinyl sticker, sleeve & vinyl itself
Don't forget that the A-Side & B-Side can be different too
Some podcasts could have the B-Side change on a chapter transition

Would be super cool to match the actual location on a physical vinyl
That means accurate rpms & groove sizes
Might be able to work out a waveform -> vinyl bumpmap script...

Vinyl white noise would be a cool aesthetic option too
Probably best as an option so users can blend in as much as they like

Try not to get sucked into the idea of making a DJ turntable
Would be very cool, but also a lot of work

### 2D or 3D
`.svg` animation / `.usd` turntable
`assimp` added `.usd` (`a`, `c` & `z`) support in `v5.4.3`[^asssimp]
`bsp_tool` has `.usd` saving support, I haven't added parsing yet.

`.svg` is really flexible, but would require a web browser, maybe
also have to do nesting & blend effects to mix the textures for each album
might be best to have a 3D render in a framebuffer, so 3D

but `.svg` would look really good miniaturised for UI stuff
an abstract vinyl, maybe with stylus progress & implied spinning

3D would also let us do something like a whirlitzer playlist
animated mechanism changing the discs etc.
pauses between tracks are common on vinyl too, to help you find them
since the change in grooves is visual to the naked eye

### [Stats](https://en.wikipedia.org/wiki/Phonograph_record)
1880s-1940s shellac:
10" 78 rpm LP "seventy-eights"

Post-1940 PVC (hence vinyl):
12" 33 & 1/3 rpm LP
7" 45 rpm "forty-fives"


## Audio Cassette
Another custom art option, could be sticker bombed or written on
also various transparent options
tape thickness on rotors would be a cool way to see progress

would be fairly simple to animate in 3D w/ a scaling cylinder
need to remember to scale the uv coords too tho

the most satisfying animation would be clicking into a player though


## Now Playing notification
 * `notify-send`
 * generated album art gif
   - CD / Vinyl
   - 45, A-Side, B-Side, 

> just this would be worth everything
> would be a great script to attach to mpd


## System Tray
Close window, keep playing


## MPD client
get everything unified in one GUI app


## Disc Ripping Tools
 * [pyDiscRip](https://github.com/AkBKukU/pyDiscRip)
   - Video: [Tech Tangents II](https://www.youtube.com/watch?v=k2EAW-EAZek)


## Music Browser
See: [TagStudio](https://github.com/TagStudioDev/TagStudio)

 * link metadata to music without editing files
 * album art database
   - case front & back
   - disc
   - booklet
   - misc.
 * `.usd` of jewel case + accessories would be neat

