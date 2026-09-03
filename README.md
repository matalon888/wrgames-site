# WRGames — attention exchange

A single self-contained page positioning **WRGames as an ad tech company**: an
attention exchange whose supply happens to be games it owns. The games are the
proof and the imagery, not the subject — the subject is the yes.

Built on the layout Daniel supplied (Kanit, `#0C0C0C`, gradient display type,
scroll-driven marquee, magnet centrepiece, scroll-lit manifesto, white rounded
Solutions section, sticky stacked Inventory cards, gradient pill CTA), with
singularads.com's register for the copy: short, declarative, one idea per line.

## Files

| File | What it is |
|---|---|
| `index.src.html` | The page. Images are `{{token}}` placeholders. **Edit this one.** |
| `assets_gen.py` | Cuts every image out of the real store screenshots → `assets/gen/` |
| `build.py` | Inlines `assets/gen/*.jpg` as data URIs → `index.html` |
| `index.html` | Generated, ~2 MB, one file, no external requests but Google Fonts |
| `assets/src/` | The 900×1600 App Store screenshots the crops come from |

```bash
python3 assets_gen.py && python3 build.py && open index.html
```

## Structure

| Section | Job |
|---|---|
| Hero — *The yes is the inventory* | The thesis in five words |
| Marquee | Ad units, labelled, running over real gameplay |
| Manifesto | Scroll-lit paragraph + four hard numbers |
| Solutions | The five things sold: rewarded, playables, in-game surfaces, direct supply, measurement |
| Inventory | The two titles and their surfaces, as sticky case-study cards |
| Close | Deal ID, app-ads.txt line, last month's delivery |

## The argument

Rory Sutherland's psycho-logic: you cannot make an interruption welcome, but you
can put it where somebody was already saying yes. Rewarded video is the only unit
in advertising with a yes inside it — the player taps a button to watch. WRGames
owns the moment end to end, so it sells the yes, not the impression.

## What buy-side reviewers look for, and where it lives

- **Supply path** — Solutions 04: `DIRECT` on every app-ads.txt line, `seller_type: PUBLISHER`, four boxes to the DSP.
- **Their vocabulary** — VAST 4.2, MRAID 3.0, OpenRTB 2.6, IAB intrinsic in-game.
- **Measurement** — Solutions 05: IAB Tech Lab / MRC in-game, MMP postbacks, SKAdNetwork and AdAttributionKit, no IDFA dependency.
- **Provenance** — Inventory: two owned titles, no resold impressions, no second SSP.

## Facts vs. placeholders

Real, from public listings (September 2026): 10M+ Google Play downloads for
*Crash Delivery*; 4.5★ from 93,758 App Store ratings; 3.8★ / 3,099 for
*Airplane Crash Madness*; live since 2020; operator Fun to Mass Games FZE,
Umm Al Quwain, licence 7887. Every image is a crop of a real store screenshot.

Replace before this reaches a buyer: the domain `wrgames.com` and the address
`media@wrgames.com`. No CPMs, fill rates or campaign results are claimed anywhere —
every ad-format statement is a property of the format or of the SDK.

## Notes

- `v1` (games-led, Archivo/Plex, red HUD chrome) is in git history at the first commit.
- The manifesto reveal runs word by word, not letter by letter: inline-block
  letters cannot wrap, so the per-character version broke words across lines.
