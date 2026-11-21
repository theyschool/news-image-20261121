#!/usr/bin/env python3
"""Render entry.png: a one-page newspaper summing up Saturday 21 November 2026.

Written fresh for news-image-20261121. Every word on the poster is set with
Pillow using real font files (DejaVu / Liberation); no image model touches
the text. The output is deterministic: same code, same fonts, same bytes.
"""

from PIL import Image, ImageDraw, ImageFont

W = 1024
H = 1024

PAPER = (248, 245, 236)
INK = (20, 20, 20)
MUTED = (92, 88, 80)
RULE = (40, 40, 40)
RED = (178, 30, 40)
TEAL = (16, 84, 92)
BLUE = (29, 78, 121)
GREEN = (38, 104, 54)
PURPLE = (96, 52, 128)
ORANGE = (190, 96, 16)
BROWN = (128, 84, 28)
PINK = (168, 44, 92)
NAVY = (24, 42, 84)
GOLD = (176, 132, 20)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_I = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap measured with the real font."""
    lines = []
    current = ""
    for word in text.split():
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_block(draw, xy, text, fnt, fill, max_w, leading):
    x, y = xy
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def centred(draw, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


# ---------------------------------------------------------------- stories
# (label, colour, headline, deck) -- every item verified against reports
# dated 21 November 2026 (or first reported that day in some time zone);
# see README.md for the source list.
LEAD_LABEL = "LEAD STORY  ·  CLIMATE  ·  ANTALYA, TÜRKIYE"
LEAD_HEAD = "COP31 deadlock sends climate talks into overtime"
LEAD_DECK = (
    "Fossil-fuel talks stall at the UN summit in Antalya. The draft deal "
    "never mentions fossil fuels, delegates cannot agree, and the talks "
    "run past their Friday close."
)

STORIES = [
    ("SPACE · MERCURY", NAVY,
     "BepiColombo enters orbit around Mercury",
     "After eight years and nine flybys, ESA and JAXA's orbiters are "
     "captured by Mercury today."),
    ("SAUDI ARABIA", RED,
     "Three Houthi missiles intercepted bound for Riyadh",
     "The coalition says all three were destroyed, a day after its "
     "strikes on Houthi workshops."),
    ("NATO · POLAND", BLUE,
     "Rutte heads to Warsaw for emergency talks",
     "NATO's chief flies in after Russian missiles crashed in Poland. "
     "PM Tusk: a deliberate provocation."),
    ("UKRAINE", BLUE,
     "Kyiv counts cost of huge Russian barrage",
     "Hundreds of missiles and drones hit bridges, power and homes in "
     "a vast attack on the capital."),
    ("PERU", GREEN,
     "Magnitude 6.7 quake rocks central Peru",
     "A strong quake near Carhuamayo, 109 miles from Lima, shakes the "
     "Andes; damage checks begin."),
    ("MARKETS · NEW YORK", BROWN,
     "Wall Street ends worst week in over a year",
     "The S&P 500 sheds $2.4 trillion in a week as Nvidia plunges 14% "
     "in a single day."),
    ("ASIA · MARKETS", BROWN,
     "Asian markets slide in the global sell-off",
     "Twelve of thirteen Asian markets fall. India's Sensex bucks the "
     "trend, up 898 points."),
    ("DIPLOMACY", PURPLE,
     "Allies condemn Moscow over the barrage",
     "France and Canada condemn the strikes on Kyiv and back Ukraine "
     "and Poland."),
    ("AFRICA · CLIMATE TALKS", GREEN,
     "African negotiators press for a stronger deal",
     "The African Group makes its case in Antalya as the summit runs "
     "into overtime."),
    ("SUDAN", ORANGE,
     "Sudan's civil war grinds on",
     "Army and RSF fighting continues across Sudan, with civilians "
     "bearing the brunt."),
    ("WEATHER · FLORIDA", TEAL,
     "Florida faces more flooding this weekend",
     "A coastal low brings heavy rain into Saturday, with flood risk "
     "rated at its highest level."),
    ("CLIMATE · PROTESTS", TEAL,
     "Protesters in Antalya call draft deal a failure",
     "Campaigners say a text silent on fossil fuels betrays the "
     "summit's purpose."),
    ("SPORT · FORMULA 1", PINK,
     "Race night on the Las Vegas Strip",
     "Formula 1 headlines Saturday night after wet, spray-soaked "
     "practice under the Sphere."),
    ("SPORT · RUGBY", PINK,
     "Nations Championship: six matches today",
     "A full Saturday card of international rugby, England against "
     "the All Blacks included."),
    ("CULTURE · 21 NOVEMBER", GOLD,
     "World Television Day is marked worldwide",
     "The UN's day honours television's role in carrying news across "
     "borders — like today's."),
]


# ---------------------------------------------------------------- drawing
def draw_globe(draw, cx, cy, r):
    """A simple flat globe with a sun arc, for the lead-story panel."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(30, 96, 110))
    land = (74, 158, 120)
    # crude continent blobs, clipped by hand to sit inside the circle
    draw.ellipse([cx - 62, cy - 48, cx - 8, cy + 6], fill=land)
    draw.ellipse([cx - 30, cy + 18, cx + 12, cy + 62], fill=land)
    draw.ellipse([cx + 18, cy - 58, cx + 66, cy - 14], fill=land)
    draw.ellipse([cx + 30, cy + 8, cx + 60, cy + 40], fill=land)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(230, 240, 235), width=4)
    # sun and heat arcs above the globe
    draw.ellipse([cx + r - 6, cy - r - 34, cx + r + 30, cy - r + 2], fill=(240, 178, 60))
    for i in range(3):
        rr = r + 14 + i * 13
        draw.arc([cx - rr, cy - rr, cx + rr, cy + rr], start=205, end=335,
                 fill=(216, 84, 60), width=5)


def masthead(draw):
    draw.rectangle([0, 0, W, H], fill=PAPER)
    draw.line([28, 26, W - 28, 26], fill=RULE, width=3)
    centred(draw, 34, "ALL THE DAY'S NEWS · ON ONE PAGE · SATURDAY EDITION",
            font(SANS_B, 15), MUTED)
    centred(draw, 58, "THE WORLD IN ONE DAY", font(SERIF_B, 66), INK)
    # the date banner: the most important line on the page
    draw.rectangle([28, 140, W - 28, 196], fill=RED)
    centred(draw, 150, "SATURDAY 21 NOVEMBER 2026", font(SANS_B, 40), (255, 255, 255))
    centred(draw, 202, "Antalya · Riyadh · Warsaw · Kyiv · Mercury · Lima · New York · Las Vegas",
            font(SANS_I, 16), MUTED)
    draw.line([28, 232, W - 28, 232], fill=RULE, width=2)


def lead(draw):
    top = 246
    draw.rectangle([28, top, W - 28, top + 208], outline=RULE, width=2)
    draw.text((48, top + 14), LEAD_LABEL, font=font(SANS_B, 16), fill=RED)
    y = draw_block(draw, (48, top + 40), LEAD_HEAD, font(SERIF_B, 36), INK, 600, 43)
    draw_block(draw, (48, y + 8), LEAD_DECK, font(SANS, 17), (46, 44, 40), 600, 21)
    # illustration panel on the right of the lead box
    px0, py0, px1, py1 = 676, top + 12, W - 40, top + 196
    draw.rectangle([px0, py0, px1, py1], fill=(18, 52, 66))
    draw_globe(draw, (px0 + px1) // 2, (py0 + py1) // 2 + 2, 46)
    cap = "ANTALYA, TÜRKIYE"
    cw = draw.textlength(cap, font=font(SANS_B, 13))
    draw.text(((px0 + px1 - cw) / 2, py1 - 22), cap, font=font(SANS_B, 13),
              fill=(235, 240, 238))


def grid(draw):
    cols = 3
    rows = 5
    x0, y0 = 28, 470
    cell_w = (W - 56 - (cols - 1) * 22) // cols
    cell_h = 99
    for idx, (label, colour, head, deck) in enumerate(STORIES):
        cx = x0 + (idx % cols) * (cell_w + 22)
        cy = y0 + (idx // cols) * cell_h
        draw.line([cx, cy, cx + cell_w, cy], fill=colour, width=4)
        draw.text((cx, cy + 7), label, font=font(SANS_B, 13), fill=colour)
        y = draw_block(draw, (cx, cy + 25), head, font(SANS_B, 16), INK, cell_w, 19)
        draw_block(draw, (cx, y + 3), deck, font(SANS, 11), (52, 50, 46), cell_w, 14)


def footer(draw):
    draw.line([28, 972, W - 28, 972], fill=RULE, width=2)
    centred(draw, 980,
            "Sources: broadcaster and wire reports of 21 November 2026 · Set in real type with Pillow · No photograph is used",
            font(SANS, 12), MUTED)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    masthead(draw)
    lead(draw)
    grid(draw)
    footer(draw)
    img.save("entry.png", format="PNG", optimize=True)


if __name__ == "__main__":
    main()
