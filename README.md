# WRGames — ad-tech positioning site

A single self-contained page that positions WRGames (the studio behind *Crash Delivery*
and *Airplane Crash Madness*) as an **owned-and-operated mobile games supply source**,
written for the buy-side procurement questions Magnite and TripleLift actually ask.

## Files

| File | What it is |
|---|---|
| `index.src.html` | The page. Assets are `{{token}}` placeholders. **Edit this one.** |
| `build.py` | Inlines every asset as a base64 data URI → `index.html` |
| `index.html` | Generated. One file, no external requests except Google Fonts. |
| `assets/` | Real store art: App Store screenshots + game-art badges |

```bash
python3 build.py      # rebuild index.html after editing index.src.html
open index.html
```

## The argument

Rory Sutherland's psycho-logic, applied to rewarded video: you cannot make an
interruption welcome, but you can put it where somebody was already saying yes.
A crash game is a machine for producing that moment — the run ends in a wreck,
arousal peaks, and the player *taps a button* to watch thirty seconds so he can
go again. The site sells the moment, not the impression.

Sections, in order: thesis → the thirty seconds (5 steps) → the numbers →
the two titles → four ad units → supply path (sellers.json, DIRECT-only) → contact.

## What buy-side reviewers look for, and where it lives on the page

- **Supply path optimisation** — the "Four boxes" section: `DIRECT` in sellers.json,
  no RESELLER lines, one hop from our SDK to the exchange.
- **Format specs in their language** — VAST 4.2, MRAID 3.0, OpenRTB 2.6, IAB intrinsic in-game.
- **Measurement** — IAB Tech Lab / MRC in-game guidelines, MMP postbacks, SKAdNetwork / AdAttributionKit.
- **Brand safety + privacy** — no cookies, no IDFA dependency, under-13 age-gated out of
  personalised demand (both titles are rated for everyone).

## Design

Deliberately single-theme. The chrome is the games' own HUD: the red callout banner
from their screenshots became the buttons, the distance pill became the stat chip, and
the left boost bar became the scroll progress rail. Deep night ground so the games'
bright daylight art carries the colour. Archivo (expanded, heavy) / IBM Plex Sans / IBM Plex Mono.

## Facts vs. placeholders

Real, from public listings (September 2026): 10M+ Google Play downloads for
*Crash Delivery*; 4.5★ from 93,758 App Store ratings; 3.8★ / 3,099 for
*Airplane Crash Madness*; shipped Jan 2020, v1.8.0 Aug 2026; operating entity
Fun to Mass Games FZE, Umm Al Quwain, licence 7887. All screenshots are the real
store assets.

Placeholders to replace before this goes anywhere near a buyer: the domain
`wrgames.com`, the address `media@wrgames.com`, and the `seller_id` in the
sellers.json snippet. Every ad-format claim on the page is a property of the format
or of the SDK — no invented CPMs, fill rates or campaign results.
