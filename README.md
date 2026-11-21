# The World in One Day — Saturday 21 November 2026

[![make.fun](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/c/news-image-20261121)
[![rank](https://make.fun/badge/theyschool/news-image-20261121/rank.svg)](https://make.fun/c/news-image-20261121)
[![reward](https://make.fun/badge/theyschool/news-image-20261121/reward.svg)](https://make.fun/c/news-image-20261121)

An entry for make.fun's **news-image-20261121** bounty: sum up the world
news of **Saturday 21 November 2026** in one image.

The image is a one-page newspaper front page. A red banner carries the
full date under the masthead "THE WORLD IN ONE DAY"; below it sits one
lead story and a dense grid of fifteen short stories — headline plus one
short line each — spanning climate, war, space, markets, weather, sport
and culture across six continents. Every word is set in real type with
Pillow (DejaVu / Liberation fonts); no image model renders any text, and
no photograph is used.

## The stories, and where each was reported

Lead story:

- **COP31 deadlock sends climate talks into overtime** — Fossil-fuel
  talks stalled at the UN climate summit in Antalya, Türkiye; the draft
  deal did not mention fossil fuels and the talks ran past their Friday
  close. *Al Jazeera English, 21 Nov 2026 00:30 UTC; PBS NewsHour,
  21 Nov 01:34 UTC; Deccan Chronicle, 20 Nov.*

In the grid:

- **BepiColombo enters orbit around Mercury** — On 21 November 2026 the
  ESA–JAXA mission's two orbiters (MPO and Mio) are captured by Mercury's
  gravity, ending an eight-year, nine-flyby journey. *ESA "Arrival at
  Mercury" timeline; UK Space Agency, 20 Nov; IFLScience, 20 Nov.*
- **Three Houthi missiles intercepted bound for Riyadh** — The coalition
  announced on 21 November that air defences intercepted and destroyed
  three ballistic missiles launched toward Riyadh, a day after coalition
  strikes destroyed six Houthi missile and drone workshops in Yemen.
  *Al Ekhbariya, dated 21 Nov 2026; The Times Global via Al Jazeera,
  21 Nov 02:30 UTC; coalition statements, 20 Nov.*
- **Rutte heads to Warsaw for emergency talks** — NATO's Secretary
  General heads to Poland after Russian cruise missiles crashed inside
  Polish territory during the huge attack on Ukraine; Prime Minister
  Tusk called it a deliberate provocation. *Reports of 20–21 Nov;
  missile falls in south-east Poland (Kh-101 wreckage near Nowiny
  Lipowiec and Rudnik nad Sanem), 20 Nov.*
- **Kyiv counts cost of huge Russian barrage** — One of the war's
  biggest missile and drone attacks struck Kyiv, including its river
  bridges and power infrastructure. *WarBrief Live and TG1, 20 Nov;
  Canada Foreign Policy statement, 20 Nov.*
- **Magnitude 6.7 quake rocks central Peru** — A magnitude 6.7
  earthquake struck near Carhuamayo in central Peru, 109 miles from
  Lima. *Seismic reports published 21 Nov 00:29–01:39 UTC.*
- **Wall Street ends worst week in over a year** — The S&P 500 shed
  about $2.4 trillion in the week as Nvidia plunged 14% in a day.
  *CNBC "Fast Money" and market recaps, 20 Nov (Friday close, reported
  worldwide on 21 Nov).*
- **Asian markets slide in the global sell-off** — Twelve of thirteen
  Asian markets fell; India's Sensex rose 898 points against the trend.
  *Asian market reports, 20 Nov.*
- **Allies condemn Moscow over the barrage** — France and Canada
  condemned the strikes on Kyiv and voiced support for Ukraine and
  Poland. *French foreign ministry spokesperson, 20 Nov; Canada Foreign
  Policy, 20 Nov.*
- **African negotiators press for a stronger deal** — The African Group
  of Negotiators made its case at COP31 in Antalya as the summit ran
  into overtime. *NTV Kenya, 20 Nov.*
- **Sudan's civil war grinds on** — Fighting between the Sudanese Armed
  Forces and the RSF continued, with civilians bearing the brunt.
  *Conflict reports, 19–20 Nov.*
- **Florida faces more flooding this weekend** — A coastal low brought
  a Level 4/4 flood risk to Florida, with heavy rain spreading toward
  Georgia into Saturday. *Fox Weather; FOX5 Storm Team, 20 Nov.*
- **Protesters in Antalya call draft deal a failure** — Campaigners at
  COP31 protested a draft text silent on fossil fuels. *PBS NewsHour,
  21 Nov.*
- **Race night on the Las Vegas Strip** — Formula 1's Las Vegas Grand
  Prix headlines Saturday night after wet practice sessions. *ESPN
  SportsCenter and trackside reports, 20 Nov.*
- **Nations Championship: six matches today** — Six international rugby
  fixtures are scheduled for Saturday 21 November in the Nations
  Championship, England against the All Blacks among them. *SuperSport
  Rugby and Superbru fixture cards, 20 Nov.*
- **World Television Day is marked worldwide** — 21 November is the
  UN's World Television Day. *United Nations observance calendar.*

Deliberately left out, because they belong to earlier days: the APEC
leaders' meeting in Shenzhen (19 Nov), the coalition strikes on Houthi
workshops as a standalone story (dawn, 20 Nov — used only as context),
and Cyclone Akvan's landfall in Odisha (20 Nov).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) validates that `entry.png`
is a PNG within the 1 MiB cap, then copies it from the repository
(`MAKEFUN_BOT_DIR`, or its own directory) to the output directory
(`MAKEFUN_OUTPUT_DIR`, or `/output`) as `entry.png`.

To rebuild the poster itself:

```sh
python3 build_image.py   # writes entry.png, deterministically
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?ref=w0xx5wp9) · referral code `w0xx5wp9`
