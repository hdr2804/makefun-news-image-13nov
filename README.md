# The World in One Day — Friday, 13 November 2026

One image summing up the day's world news, drawn as a newspaper front page:
a screenprint-style collage under the masthead "THE WORLD IN ONE DAY", with
the day's lead headline and a ticker of the other stories. Six stories are
pictured:

1. **Iran / Strait of Hormuz** — Tankers burn in a narrow strait at dusk
   (top left) after attacks in the Strait of Hormuz; Iran also claimed a
   strike on a U.S. radar installation. This is the day's lead story and
   carries the headline strip.
2. **Ukraine peace talks** — A long negotiation table (centre) with the
   Ukrainian, Russian, European Union and American flags, as Europe took a
   seat at the peace talks alongside Kyiv, Moscow and Washington.
3. **NVIDIA** — The giant cracked, sparking microchip (top centre) stands
   for the shock resignation of NVIDIA chief Jensen Huang, the day's big
   technology and markets story.
4. **Microsoft outage** — Dark office towers and monitors showing blue
   error faces (right): a global Microsoft outage blanked office screens
   worldwide.
5. **Pope Leo in Peru** — The pope in white waves from a balcony to a vast
   cheering crowd (bottom left), drawn by record crowds on his Peru visit.
6. **Binance hack seizure** — Named in the ticker: U.S. authorities seized
   $1.2B looted in the Binance hack. The plunging red chart arrow (bottom
   right) is the markets' reaction to the day — Hormuz, the NVIDIA shock
   and the outage all landing at once.

## How it runs

`main.py` (Python 3, standard library only) copies the bundled `art.png`
byte-for-byte to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`),
creating the output directory if needed. The image is 1024×865 px and
240,180 bytes, inside the scorer's limits of 1024×1024 px and 1 MiB.
