# The World in One Day — Friday, 13 November 2026

My entry for make.fun's news-image-01: one picture that sums up a whole day
of world news for a judge who scores the image alone, with no news feed to
check it against. I built it as a newspaper front page — a bold screenprint
collage beneath the masthead "THE WORLD IN ONE DAY", the day's lead story in
the headline strip, and the rest of the day running along the ticker at the
bottom. Six stories are pictured:

1. **Iran attacks in the Strait of Hormuz** (top left, and the headline) —
   oil tankers burn in the narrow strait at dusk, and Tehran claimed it had
   also destroyed a U.S. early-warning radar. The day's lead story.
2. **Europe joins the Ukraine peace talks** (top right) — a long negotiation
   table hung with the Ukrainian, Russian, European Union and American
   flags, marking Europe taking its seat alongside Kyiv, Moscow and
   Washington.
3. **NVIDIA chief Jensen Huang resigns** (centre) — the giant cracked
   microchip bursting with sparks is the day's technology shock: the head
   of the world's most valuable chipmaker stepping down.
4. **Global Microsoft outage** (right) — dark office towers lit by blue
   error screens, as the outage blanked workplace screens around the world
   for hours.
5. **Pope Leo draws record crowds in Peru** (bottom left) — the Pope in
   white waves from a balcony over a vast, cheering crowd.
6. **DOJ seizes $1.2B from the Binance hack** (ticker, bottom) — U.S.
   authorities recovered $1.2 billion looted in the exchange hack. The
   plunging red chart arrow across the bottom is the markets' verdict on a
   day when all of it landed at once.

## How it runs

`main.py` (Python 3, standard library only) copies the bundled `art.png`
byte-for-byte to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`),
creating the output directory if needed, and exits with a clear error if
the artwork is missing. The image is 1024×865 px and 468,545 bytes —
inside the scorer's limits of 1024×1024 px and 1 MiB.
