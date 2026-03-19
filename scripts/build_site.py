from __future__ import annotations

import html
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STYLESHEET = "styles.css"
FAVICON_HREF = (
    "data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 "
    "viewBox=%220 0 100 100%22%3E%3Ctext y=%22.9em%22 font-size=%2290%22%3E"
    "%F0%9F%87%A8%F0%9F%87%B7%3C/text%3E%3C/svg%3E"
)


@dataclass
class DayPlan:
    number: int
    label: str
    theme: str
    summary: str
    images: list[str] = field(default_factory=list)
    captions: list[str] = field(default_factory=list)
    bullets: list[str] = field(default_factory=list)


@dataclass
class Itinerary:
    slug: str
    name: str
    tagline: str
    summary: str
    hero_image: str
    hero_caption: str
    pros: list[str]
    cons: list[str]
    hotels: list[str]
    days: list[DayPlan]

    @property
    def filename(self) -> str:
        return f"{self.slug}.html"


@dataclass
class FlightInfo:
    airline: str
    flight_number: str
    route: str
    date: str
    depart_time: str
    arrive_time: str
    duration: str
    travelers: str
    confirmed: bool = True


# ---------------------------------------------------------------------------
# Flight data
# ---------------------------------------------------------------------------

OUTBOUND_FLIGHT = FlightInfo(
    airline="Air Transat",
    flight_number="TS 112",
    route="YYZ \u2192 SJO nonstop",
    date="Thu Apr 16",
    depart_time="7:05 PM",
    arrive_time="10:35 PM",
    duration="5h 30m",
    travelers="3 (Daniel, Emilie, Madison)",
    confirmed=True,
)

RETURN_FLIGHT = FlightInfo(
    airline="Air Canada",
    flight_number="AC 956",
    route="SJO \u2192 YYZ nonstop",
    date="Wed Apr 22",
    depart_time="7:55 AM",
    arrive_time="3:05 PM",
    duration="5h 10m",
    travelers="2 (Emilie & Madison)",
    confirmed=True,
)


# ---------------------------------------------------------------------------
# Local images (downloaded from Wikimedia Commons / Pexels)
# ---------------------------------------------------------------------------

IMG = {
    "manuel_antonio_beach": "images/manuel-antonio-beach.jpg",
    "manuel_antonio_monkeys": "images/capuchin-manuel-antonio.jpg",
    "arenal_volcano": "images/arenal-volcano.jpg",
    "arenal_bridges": "images/arenal-hanging-bridges.jpg",
    "sloth": "images/sloth.jpg",
    "playa_conchal": "images/playa-conchal.jpg",
    "tamarindo": "images/tamarindo-beach.jpg",
    "quepos_fishing": "images/fishing-boat.jpg",
    "la_fortuna_waterfall": "images/la-fortuna-waterfall.jpg",
    "hot_springs": "images/hot-springs.jpg",
    "guanacaste_beach": "images/guanacaste-coast.jpg",
    "sjo_airport": "images/sjo-airport.jpg",
    "costa_rica_fruit": "images/fruit-market.jpg",
    "howler_monkey": "images/howler-monkey.jpg",
    "dominical": "images/dominical-beach.jpg",
    "los_suenos": "images/los-suenos.jpg",
    "capuchin": "images/capuchin-beach.jpg",
}


# ---------------------------------------------------------------------------
# Itinerary data
# ---------------------------------------------------------------------------

ITINERARIES = [
    Itinerary(
        slug="resort",
        name="The Resort",
        tagline="One hotel, maximum chill",
        summary="Settle into the JW Marriott Guanacaste for the entire trip. Luxury beach resort with day trips to fishing, remote beaches, and Tamarindo shopping.",
        hero_image=IMG["guanacaste_beach"],
        hero_caption="Guanacaste coastline",
        pros=[
            "One base \u2014 unpack once, relax all week",
            "JW Marriott luxury resort with Titanium perks",
            "Minimal planning and logistics",
        ],
        cons=[
            "4-hour drives bookend the trip (SJO \u2194 Guanacaste)",
            "Fewer monkeys and sloths than Manuel Antonio",
            "Less variety in landscapes",
        ],
        hotels=["JW Marriott Guanacaste Resort & Spa (Marriott points)"],
        days=[
            DayPlan(
                number=0,
                label="Thu Apr 16",
                theme="Arrive & Settle",
                summary="Land at SJO at 10:35 PM. Short shuttle to airport hotel, crash for the night.",
                images=[IMG["sjo_airport"]],
                captions=["Juan Santamar\u00eda International Airport"],
                bullets=[
                    "Air Transat TS 112 lands at 10:35 PM",
                    "Shuttle to airport hotel (Marriott San Jos\u00e9 or Holiday Inn Express)",
                    "Quick dinner at hotel or nearby",
                    "Early night \u2014 big drive tomorrow",
                ],
            ),
            DayPlan(
                number=1,
                label="Fri Apr 17",
                theme="Drive to Guanacaste",
                summary="4-hour scenic drive northwest to the JW Marriott Guanacaste. Settle in and catch sunset on the beach.",
                images=[IMG["guanacaste_beach"], IMG["tamarindo"]],
                captions=["Guanacaste coast", "Pacific sunset"],
                bullets=[
                    "Pick up rental car at SJO",
                    "4-hour scenic drive along the Pan-American Highway",
                    "Check in at JW Marriott Guanacaste Resort & Spa",
                    "Explore the resort \u2014 pools, beach, grounds",
                    "Golden-hour walk on Mansita Beach",
                    "Sunset dinner at the resort",
                ],
            ),
            DayPlan(
                number=2,
                label="Sat Apr 18",
                theme="Deep-Sea Fishing",
                summary="Morning fishing charter out of Flamingo or Tamarindo. Chase sailfish and mahi-mahi in the Pacific, then relax poolside.",
                images=[IMG["quepos_fishing"], IMG["guanacaste_beach"]],
                captions=["Pacific sport fishing", "Back at the resort"],
                bullets=[
                    "Early departure for Flamingo marina (30 min drive)",
                    "Half-day deep-sea fishing charter \u2014 sailfish, mahi-mahi, roosterfish",
                    "Return to resort by early afternoon",
                    "Pool and beach afternoon",
                    "Fresh catch dinner if the crew cleans your fish",
                ],
            ),
            DayPlan(
                number=3,
                label="Sun Apr 19",
                theme="Remote Beach Hopping",
                summary="Discover hidden beaches along the Gold Coast: Playa Conchal\u2019s crushed-shell shore, Playa San Juanillo, and howler monkeys in the trees.",
                images=[IMG["playa_conchal"], IMG["howler_monkey"]],
                captions=["Playa Conchal", "Howler monkey"],
                bullets=[
                    "Drive to Playa Conchal \u2014 crushed seashell beach, clear snorkeling",
                    "Continue to Playa San Juanillo \u2014 secluded and quiet",
                    "Spot howler monkeys in the coastal forest canopy",
                    "Tropical fruit from roadside stands \u2014 mango, cas, guanábana",
                    "Sunset back at the resort",
                ],
            ),
            DayPlan(
                number=4,
                label="Mon Apr 20",
                theme="Tamarindo & Shopping",
                summary="Beach day in Tamarindo with surfing, boutique bathing-suit shopping, and tropical fruit stands.",
                images=[IMG["tamarindo"], IMG["costa_rica_fruit"]],
                captions=["Tamarindo beach", "Tropical fruit stand"],
                bullets=[
                    "Drive to Tamarindo (30 min)",
                    "Morning surf lesson or beach time",
                    "Boutique shopping \u2014 bathing suits, local crafts",
                    "Tropical fruit tasting \u2014 fresh juices and smoothies",
                    "Lunch at a beachfront restaurant",
                    "Return to resort for final sunset swim",
                ],
            ),
            DayPlan(
                number=5,
                label="Tue Apr 21",
                theme="Last Beach & Return",
                summary="Morning beach walk, then 4-hour drive back to the SJO area. Overnight near the airport for early flights.",
                images=[IMG["guanacaste_beach"], IMG["sjo_airport"]],
                captions=["Morning on the coast", "Back to SJO"],
                bullets=[
                    "Final sunrise beach walk",
                    "Late morning checkout from JW Marriott",
                    "4-hour drive back to San Jos\u00e9 area",
                    "Stop for souvenirs and coffee along the way",
                    "Check in to airport hotel",
                    "Early night \u2014 Emilie & Madison fly out at 7:55 AM",
                ],
            ),
        ],
    ),
    Itinerary(
        slug="explorer",
        name="The Explorer",
        tagline="New spot every day, maximum variety",
        summary="A road trip through Costa Rica\u2019s greatest hits: Manuel Antonio monkeys, Quepos fishing, Arenal volcano hot springs, Sarapiquí fruit farms, and everything in between.",
        hero_image=IMG["manuel_antonio_beach"],
        hero_caption="Manuel Antonio National Park",
        pros=[
            "See the most \u2014 hit every interest (monkeys, sloths, fishing, fruit, beaches)",
            "Maximum variety of landscapes and experiences",
            "Best mix of Pacific coast and volcano rainforest",
        ],
        cons=[
            "Lots of driving (3\u20134 hours on multiple days)",
            "Pack and unpack daily \u2014 new hotel every night",
            "More planning and coordination required",
        ],
        hotels=[
            "Airport hotel (night 0 & 5)",
            "Manuel Antonio boutique hotel (nights 1\u20132)",
            "La Fortuna / Arenal lodge (night 3)",
            "Sarapiquí eco-lodge (night 4)",
        ],
        days=[
            DayPlan(
                number=0,
                label="Thu Apr 16",
                theme="Arrive & Settle",
                summary="Land at SJO at 10:35 PM. Shuttle to airport hotel for the night.",
                images=[IMG["sjo_airport"]],
                captions=["SJO Airport"],
                bullets=[
                    "Air Transat TS 112 lands at 10:35 PM",
                    "Shuttle to airport hotel",
                    "Quick dinner and early night",
                    "Tomorrow: 3-hour drive to Manuel Antonio",
                ],
            ),
            DayPlan(
                number=1,
                label="Fri Apr 17",
                theme="Manuel Antonio Arrival",
                summary="3-hour drive south to Manuel Antonio. Afternoon on the beach with capuchin monkeys in the trees overhead.",
                images=[IMG["manuel_antonio_beach"], IMG["capuchin"]],
                captions=["Manuel Antonio beach", "White-faced capuchin"],
                bullets=[
                    "Pick up rental car and head south on Costanera highway",
                    "3-hour drive to Manuel Antonio (scenic Pacific coast road)",
                    "Check in to boutique hotel near the park",
                    "Afternoon at Playa Espadilla \u2014 capuchin monkeys roam the beach",
                    "Sunset from the Manuel Antonio hillside",
                    "Dinner in Quepos town",
                ],
            ),
            DayPlan(
                number=2,
                label="Sat Apr 18",
                theme="Park & Fishing",
                summary="Morning guided tour of Manuel Antonio National Park (monkeys, sloths, beaches), then afternoon fishing charter from Quepos.",
                images=[IMG["manuel_antonio_monkeys"], IMG["quepos_fishing"], IMG["sloth"]],
                captions=["Capuchin in Manuel Antonio", "Quepos sport fishing", "Three-toed sloth"],
                bullets=[
                    "Early entry to Manuel Antonio National Park with a guide",
                    "Spot white-faced capuchins, howler monkeys, and two- and three-toed sloths",
                    "Swim at the park\u2019s hidden beaches",
                    "Afternoon fishing charter out of Quepos marina",
                    "Chase sailfish, mahi-mahi, and roosterfish",
                    "Dinner with fresh catch in Quepos",
                ],
            ),
            DayPlan(
                number=3,
                label="Sun Apr 19",
                theme="Arenal & Hot Springs",
                summary="4-hour drive inland to La Fortuna. Afternoon sloth spotting, evening soak in volcanic hot springs with Arenal views.",
                images=[IMG["arenal_volcano"], IMG["hot_springs"], IMG["sloth"]],
                captions=["Arenal Volcano", "Volcanic hot springs", "Sloth spotting"],
                bullets=[
                    "Morning checkout, 4-hour drive to La Fortuna / Arenal",
                    "Stop for roadside tropical fruit along the way",
                    "Check in to Arenal lodge with volcano views",
                    "Afternoon sloth-spotting walk (guided, near Arenal)",
                    "Evening at Tabac\u00f3n or Baldi hot springs",
                    "Dinner with Arenal Volcano glowing in the background",
                ],
            ),
            DayPlan(
                number=4,
                label="Mon Apr 20",
                theme="Bridges, Waterfalls & Fruit",
                summary="Arenal hanging bridges and La Fortuna waterfall in the morning, then drive to Sarapiquí for chocolate and tropical fruit farms.",
                images=[IMG["arenal_bridges"], IMG["la_fortuna_waterfall"], IMG["costa_rica_fruit"]],
                captions=["Mistico Hanging Bridges", "La Fortuna Waterfall", "Tropical fruit"],
                bullets=[
                    "Mistico Arenal Hanging Bridges \u2014 walk through the canopy",
                    "La Fortuna Waterfall hike (500 steps down and back up)",
                    "Drive to Sarapiquí (1.5 hours through lush lowlands)",
                    "Chocolate and tropical fruit farm tour",
                    "Taste exotic fruits: rambutan, starfruit, guanábana",
                    "Overnight at Sarapiquí eco-lodge",
                ],
            ),
            DayPlan(
                number=5,
                label="Tue Apr 21",
                theme="Fruit Market & Return",
                summary="Morning at a local fruit market, then 2-hour drive back to SJO. Last-minute shopping, overnight near the airport.",
                images=[IMG["costa_rica_fruit"], IMG["sjo_airport"]],
                captions=["Fresh tropical fruit", "Back to SJO"],
                bullets=[
                    "Morning visit to local fruit and produce market",
                    "Stock up on Costa Rican coffee and chocolate",
                    "2-hour drive back to San Jos\u00e9",
                    "Souvenir shopping in Escaz\u00fa or Multiplaza",
                    "Check in to airport hotel",
                    "Early night \u2014 Emilie & Madison fly at 7:55 AM",
                ],
            ),
        ],
    ),
    Itinerary(
        slug="sweet-spot",
        name="The Sweet Spot",
        tagline="Two bases, best of both worlds",
        summary="Split the trip between the Central Pacific coast (Los Sueños Marriott, Manuel Antonio, Quepos fishing) and the Arenal volcano region (hot springs, hanging bridges, sloths). One hotel change, maximum variety.",
        hero_image=IMG["manuel_antonio_monkeys"],
        hero_caption="Capuchin monkey at Manuel Antonio",
        pros=[
            "Best wildlife variety \u2014 monkeys on beaches, sloths in cloud forest",
            "Two distinct experiences: Pacific coast + volcano rainforest",
            "Marriott points for Los Sueños, only one hotel change",
        ],
        cons=[
            "Day 4 has a long drive (4 hours coast to volcano)",
            "Less time at each location than a single-base trip",
            "Miss the Guanacaste Gold Coast beaches",
        ],
        hotels=[
            "Airport hotel (night 0 & 5)",
            "Los Sueños Marriott Ocean & Golf Resort (nights 1\u20133, Marriott points)",
            "La Fortuna / Arenal lodge (night 4)",
        ],
        days=[
            DayPlan(
                number=0,
                label="Thu Apr 16",
                theme="Arrive & Settle",
                summary="Land at SJO at 10:35 PM. Quick transfer to airport hotel.",
                images=[IMG["sjo_airport"]],
                captions=["SJO Airport"],
                bullets=[
                    "Air Transat TS 112 lands at 10:35 PM",
                    "Shuttle to airport hotel",
                    "Quick dinner and early night",
                    "Tomorrow: 2\u20133 hour drive to the Central Pacific coast",
                ],
            ),
            DayPlan(
                number=1,
                label="Fri Apr 17",
                theme="Central Pacific Coast",
                summary="2\u20133 hour drive to Los Sueños Marriott. Afternoon beach time on the Central Pacific coast, sunset over Herradura Bay.",
                images=[IMG["los_suenos"], IMG["manuel_antonio_beach"]],
                captions=["Herradura Bay", "Pacific coast beach"],
                bullets=[
                    "Pick up rental car, drive to Los Sueños / Herradura (2\u20133 hours)",
                    "Check in at Los Sueños Marriott Ocean & Golf Resort",
                    "Afternoon at the resort beach and pools",
                    "Optional: drive 1 hour south to Manuel Antonio for a preview",
                    "Sunset over Herradura Bay",
                    "Dinner at the resort or in Jac\u00f3 town",
                ],
            ),
            DayPlan(
                number=2,
                label="Sat Apr 18",
                theme="Manuel Antonio National Park",
                summary="Full day at Manuel Antonio: guided tour through the park spotting capuchins, howler monkeys, sloths, and iguanas. Swim at pristine park beaches.",
                images=[IMG["manuel_antonio_monkeys"], IMG["manuel_antonio_beach"], IMG["sloth"]],
                captions=["Capuchin monkeys", "Park beach", "Three-toed sloth"],
                bullets=[
                    "Drive to Manuel Antonio (1 hour south)",
                    "Guided tour of the national park (book ahead \u2014 limited daily entry)",
                    "Spot white-faced capuchins, howler monkeys, two-toed sloths",
                    "Swim at Playa Manuel Antonio \u2014 monkeys on the beach",
                    "Lunch at a park-adjacent restaurant",
                    "Return to Los Sueños for evening at the resort",
                ],
            ),
            DayPlan(
                number=3,
                label="Sun Apr 19",
                theme="Fishing & Remote Beaches",
                summary="Morning fishing charter from Quepos (the sailfish capital), then afternoon exploring remote beaches near Dominical.",
                images=[IMG["quepos_fishing"], IMG["dominical"]],
                captions=["Quepos sport fishing", "Dominical coastline"],
                bullets=[
                    "Early morning drive to Quepos marina (1 hour)",
                    "Half-day fishing charter \u2014 sailfish, mahi-mahi, dorado",
                    "Drive south to Dominical for a wild, uncrowded beach afternoon",
                    "Spot howler monkeys in the trees along the coast road",
                    "Fresh tropical fruit from roadside stands",
                    "Return to Los Sueños for final night at the Marriott",
                ],
            ),
            DayPlan(
                number=4,
                label="Mon Apr 20",
                theme="Arenal Volcano & Hot Springs",
                summary="4-hour drive from the coast to La Fortuna. Arenal volcano views, afternoon hanging bridges walk, and evening volcanic hot springs.",
                images=[IMG["arenal_volcano"], IMG["arenal_bridges"], IMG["hot_springs"]],
                captions=["Arenal Volcano", "Hanging bridges canopy walk", "Hot springs"],
                bullets=[
                    "Morning checkout from Los Sueños, 4-hour drive to La Fortuna",
                    "Check in to Arenal lodge with volcano views",
                    "Afternoon at Mistico Arenal Hanging Bridges \u2014 canopy walk through the rainforest",
                    "Spot sloths, toucans, and howler monkeys from the bridges",
                    "Evening soak in Tabac\u00f3n or Baldi volcanic hot springs",
                    "Dinner with a view of Arenal Volcano",
                ],
            ),
            DayPlan(
                number=5,
                label="Tue Apr 21",
                theme="Sloths, Waterfalls & Return",
                summary="Morning sloth spotting and La Fortuna waterfall, then 2.5-hour drive back to SJO. Overnight near the airport.",
                images=[IMG["sloth"], IMG["la_fortuna_waterfall"], IMG["sjo_airport"]],
                captions=["Sloth spotting", "La Fortuna Waterfall", "Back to SJO"],
                bullets=[
                    "Early guided sloth and wildlife walk near Arenal",
                    "Visit La Fortuna Waterfall (if time allows)",
                    "Late morning drive back to San Jos\u00e9 area (2.5 hours)",
                    "Stop for Costa Rican coffee and souvenirs",
                    "Check in to airport hotel",
                    "Early night \u2014 Emilie & Madison fly at 7:55 AM",
                ],
            ),
        ],
    ),
]


# ---------------------------------------------------------------------------
# HTML helpers
# ---------------------------------------------------------------------------

SITE_URL = "https://dburkhardt.github.io/costa_rica_2026"

HEAD_COMMON = f"""\
  <link rel="icon" href="{FAVICON_HREF}">
  <meta property="og:image" content="{SITE_URL}/social-share.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Costa Rica 2026">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Playfair+Display:wght@600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{STYLESHEET}">"""


def nav_links(current_page: str | None = None) -> str:
    links = ['<a href="index.html" class="nav-home">Costa Rica 2026</a>']
    for itin in ITINERARIES:
        classes = "day-link"
        if current_page == itin.slug:
            classes += " active"
        links.append(f'<a href="{itin.filename}" class="{classes}">{html.escape(itin.name)}</a>')
    logistics_classes = "day-link"
    if current_page == "logistics":
        logistics_classes += " active"
    links.append(f'<a href="logistics.html" class="{logistics_classes}">Logistics</a>')
    return "\n".join(links)


def flight_row(flight: FlightInfo) -> str:
    row_class = ' class="featured"' if flight.confirmed else ""
    badge = '<span class="flight-badge">Booked</span>' if flight.confirmed else ""
    return f"""
          <tr{row_class}>
            <td>
              <div class="flight-airline">
                <strong>{html.escape(flight.airline)}</strong>
                {badge}
              </div>
            </td>
            <td><span class="flight-route">{html.escape(flight.route)}</span></td>
            <td><span class="flight-date">{html.escape(flight.date)}</span><span class="flight-time">{html.escape(flight.depart_time)}</span></td>
            <td><span class="flight-date">{html.escape(flight.date)}</span><span class="flight-time">{html.escape(flight.arrive_time)}</span></td>
            <td><span class="flight-duration">{html.escape(flight.duration)}</span></td>
            <td><span class="flight-points">{html.escape(flight.travelers)}</span></td>
          </tr>
"""


# ---------------------------------------------------------------------------
# Page renderers
# ---------------------------------------------------------------------------

def render_index() -> str:
    cards = []
    for itin in ITINERARIES:
        preview_bullets = []
        for day in itin.days[1:4]:
            preview_bullets.append(f"<li><strong>Day {day.number}:</strong> {html.escape(day.theme)}</li>")
        pros_preview = "".join(f"<li>{html.escape(p)}</li>" for p in itin.pros[:2])

        cards.append(f"""
      <article class="excursion-card reveal">
        <a class="card-media" href="{itin.filename}">
          <img src="{html.escape(itin.hero_image)}" alt="{html.escape(itin.hero_caption)}">
        </a>
        <div class="card-copy">
          <div class="eyebrow">{html.escape(itin.tagline)}</div>
          <h2><a href="{itin.filename}">{html.escape(itin.name)}</a></h2>
          <p>{html.escape(itin.summary)}</p>
          <ul class="preview-list">
            {pros_preview}
          </ul>
          <div class="card-meta">
            <span>{len(itin.days)} days \u00b7 {len(itin.hotels)} hotel{'s' if len(itin.hotels) != 1 else ''}</span>
            <a href="{itin.filename}">View itinerary</a>
          </div>
        </div>
      </article>
""")

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Costa Rica \u00b7 April 2026</title>
  <meta name="description" content="Costa Rica family trip, April 16 to 22, 2026. Three itinerary options to choose from.">
  <meta property="og:title" content="Costa Rica \u00b7 April 2026">
  <meta property="og:description" content="Costa Rica family trip, April 16 to 22, 2026. Three itinerary options to choose from.">
  <meta property="og:url" content="{SITE_URL}/">
{HEAD_COMMON}
</head>
<body class="site-home">
  <header class="site-nav">
    <nav>
      {nav_links(current_page="home")}
    </nav>
  </header>

  <main>
    <section class="hero hero-home reveal">
      <div class="hero-copy">
        <div class="eyebrow">Costa Rica \u00b7 Apr 16\u201322, 2026</div>
        <h1>Jungle to shore.</h1>
        <p>Five days between Pacific beaches, volcanic hot springs, and rainforest canopy. Three ways to do it \u2014 pick your adventure.</p>
        <div class="hero-actions">
          <a href="#options" class="btn-primary">See options</a>
          <a href="logistics.html" class="btn-secondary">Flights</a>
        </div>
      </div>
      <div class="hero-panel">
        <img src="{html.escape(IMG['manuel_antonio_beach'])}" alt="Manuel Antonio beach">
      </div>
    </section>

    <section class="section-head reveal" id="options">
      <div class="eyebrow">Three itineraries</div>
      <h2>Pick your adventure</h2>
      <p>Each option covers the same five full days (Fri Apr 17 \u2013 Tue Apr 21). Arrive Thursday night, depart Wednesday morning. Tap any card to see the full day-by-day plan.</p>
    </section>

    <section class="excursion-grid">
      {''.join(cards)}
    </section>
  </main>
</body>
</html>
"""


def render_itinerary(itin: Itinerary) -> str:
    day_blocks = []
    for day in itin.days:
        bullet_items = "".join(f"<li>{html.escape(b)}</li>" for b in day.bullets)

        gallery_imgs = ""
        if day.images:
            imgs = []
            for img_src, caption in zip(day.images, day.captions):
                imgs.append(f'<img src="{html.escape(img_src)}" alt="{html.escape(caption)}">')
            gallery_imgs = f"""
        <div class="day-gallery">
          {''.join(imgs)}
        </div>"""

        day_blocks.append(f"""
      <div class="day-block reveal">
        <div class="eyebrow">Day {day.number} \u00b7 {html.escape(day.label)}</div>
        <h3>{html.escape(day.theme)}</h3>
        <p>{html.escape(day.summary)}</p>
        <ul>
          {bullet_items}
        </ul>{gallery_imgs}
      </div>
""")

    pros_items = "".join(f"<li>{html.escape(p)}</li>" for p in itin.pros)
    cons_items = "".join(f"<li>{html.escape(c)}</li>" for c in itin.cons)
    hotel_items = "".join(f"<li>{html.escape(h)}</li>" for h in itin.hotels)

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(itin.name)} \u00b7 Costa Rica</title>
  <meta name="description" content="{html.escape(itin.summary)}">
  <meta property="og:title" content="{html.escape(itin.name)} \u00b7 Costa Rica">
  <meta property="og:description" content="{html.escape(itin.summary)}">
  <meta property="og:url" content="{SITE_URL}/{itin.filename}">
{HEAD_COMMON}
</head>
<body class="site-day">
  <header class="site-nav">
    <nav>
      {nav_links(current_page=itin.slug)}
    </nav>
  </header>

  <main>
    <section class="hero hero-day reveal">
      <div class="hero-copy">
        <span class="option-badge">{html.escape(itin.tagline)}</span>
        <div class="eyebrow">Costa Rica \u00b7 Apr 16\u201322</div>
        <h1>{html.escape(itin.name)}</h1>
        <p>{html.escape(itin.summary)}</p>
        <div class="hero-actions">
          <a href="#days" class="btn-primary">Day by day</a>
          <a href="#details" class="btn-secondary">Pros & cons</a>
        </div>
      </div>
      <div class="hero-panel">
        <img src="{html.escape(itin.hero_image)}" alt="{html.escape(itin.hero_caption)}">
      </div>
    </section>

    <section class="content-grid" id="details">
      <article class="detail-card reveal">
        <div class="eyebrow">Hotels</div>
        <h2>Where you\u2019ll stay</h2>
        <ul class="detail-list">
          {hotel_items}
        </ul>
        <div class="pros-cons">
          <div>
            <h3>Pros</h3>
            <ul>{pros_items}</ul>
          </div>
          <div>
            <h3>Cons</h3>
            <ul>{cons_items}</ul>
          </div>
        </div>
      </article>

      <aside class="detail-card reveal accent-card">
        <div class="eyebrow">At a glance</div>
        <h2>{html.escape(itin.name)}</h2>
        <p>{html.escape(itin.tagline)}</p>
        <div class="stat-row">
          <span class="stat-label">Days</span>
          <strong>{len(itin.days)} days</strong>
        </div>
        <div class="stat-row">
          <span class="stat-label">Hotels</span>
          <strong>{len(itin.hotels)} location{'s' if len(itin.hotels) != 1 else ''}</strong>
        </div>
        <div class="stat-row">
          <span class="stat-label">Style</span>
          <strong>{html.escape(itin.tagline)}</strong>
        </div>
      </aside>
    </section>

    <section class="section-head reveal" id="days">
      <div class="eyebrow">Day by day</div>
      <h2>{html.escape(itin.name)}</h2>
      <p>Full breakdown from arrival to departure.</p>
    </section>

    {''.join(day_blocks)}

    <section class="pager">
      <a href="index.html" class="pager-link">All options</a>
      <a href="logistics.html" class="pager-link">Flights</a>
    </section>
  </main>
</body>
</html>
"""


def render_logistics() -> str:
    outbound_row = flight_row(OUTBOUND_FLIGHT)
    return_row = flight_row(RETURN_FLIGHT)

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Logistics \u00b7 Costa Rica</title>
  <meta name="description" content="Confirmed flights for Costa Rica, April 2026.">
  <meta property="og:title" content="Logistics \u00b7 Costa Rica">
  <meta property="og:description" content="Confirmed flights for Costa Rica, April 2026.">
  <meta property="og:url" content="{SITE_URL}/logistics.html">
{HEAD_COMMON}
</head>
<body class="site-day">
  <header class="site-nav">
    <nav>
      {nav_links(current_page="logistics")}
    </nav>
  </header>

  <main>
    <section class="hero hero-day reveal">
      <div class="hero-copy">
        <div class="eyebrow">Logistics \u00b7 Apr 16\u201322, 2026</div>
        <h1>Flights</h1>
        <p>Both flights are booked and confirmed. Arrive SJO Thursday night, depart Wednesday morning. Daniel continues to Brazil for work.</p>
        <div class="hero-actions">
          <a href="#outbound" class="btn-primary">Outbound</a>
          <a href="#return" class="btn-secondary">Return</a>
        </div>
      </div>
      <div class="hero-panel">
        <img src="{html.escape(IMG['sjo_airport'])}" alt="SJO Airport">
      </div>
    </section>

    <section class="content-grid">
      <article class="detail-card reveal" id="overview">
        <div class="eyebrow">Timing</div>
        <h2>Key details</h2>
        <ul class="detail-list">
          <li>Outbound: Air Transat TS 112 on Thu Apr 16. YYZ \u2192 SJO nonstop, arrives 10:35 PM.</li>
          <li>Return: Air Canada AC 956 on Wed Apr 22. SJO \u2192 YYZ nonstop, departs 7:55 AM.</li>
          <li>Return is for Emilie & Madison only \u2014 Daniel continues to Brazil.</li>
          <li>5 full days in Costa Rica: Fri Apr 17 through Tue Apr 21.</li>
          <li>Need airport hotel for arrival night (Thu) and final night (Tue).</li>
        </ul>
      </article>

      <aside class="detail-card reveal accent-card">
        <div class="eyebrow">Trip window</div>
        <h2>Apr 16\u201322</h2>
        <p>Arrive late Thursday, five full adventure days, depart early Wednesday.</p>
        <div class="stat-row">
          <span class="stat-label">Outbound</span>
          <strong>3 travelers</strong>
        </div>
        <div class="stat-row">
          <span class="stat-label">Return</span>
          <strong>2 travelers</strong>
        </div>
        <div class="stat-row">
          <span class="stat-label">Full days</span>
          <strong>5 days</strong>
        </div>
      </aside>
    </section>

    <section class="section-head reveal" id="outbound">
      <div class="eyebrow">Thu Apr 16</div>
      <h2>Outbound</h2>
      <p>Toronto to San Jos\u00e9, nonstop on Air Transat. All three travelers.</p>
    </section>

    <section class="logistics-grid">
      <article class="detail-card flight-card logistics-span reveal">
        <div class="eyebrow">YYZ \u2192 SJO</div>
        <h2>Outbound flight</h2>
        <div class="table-wrap">
          <table class="flight-table">
            <thead>
              <tr>
                <th>Airline</th>
                <th>Route</th>
                <th>Departs</th>
                <th>Arrives</th>
                <th>Duration</th>
                <th>Travelers</th>
              </tr>
            </thead>
            <tbody>
              {outbound_row}
            </tbody>
          </table>
        </div>
      </article>
    </section>

    <section class="section-head reveal" id="return">
      <div class="eyebrow">Wed Apr 22</div>
      <h2>Return</h2>
      <p>San Jos\u00e9 to Toronto, nonstop on Air Canada. Emilie and Madison only \u2014 Daniel heads to Brazil.</p>
    </section>

    <section class="logistics-grid">
      <article class="detail-card flight-card logistics-span reveal">
        <div class="eyebrow">SJO \u2192 YYZ</div>
        <h2>Return flight</h2>
        <div class="table-wrap">
          <table class="flight-table">
            <thead>
              <tr>
                <th>Airline</th>
                <th>Route</th>
                <th>Departs</th>
                <th>Arrives</th>
                <th>Duration</th>
                <th>Travelers</th>
              </tr>
            </thead>
            <tbody>
              {return_row}
            </tbody>
          </table>
        </div>
      </article>

      <aside class="detail-card reveal">
        <div class="eyebrow">Note</div>
        <h2>Daniel\u2019s onward travel</h2>
        <ul class="detail-list">
          <li>Daniel does not return to Toronto on Apr 22.</li>
          <li>He continues from Costa Rica to Brazil for work (separate booking).</li>
          <li>Emilie and Madison fly home together on AC 956.</li>
        </ul>
      </aside>
    </section>

    <section class="pager">
      <a href="index.html" class="pager-link">All options</a>
      <a href="{ITINERARIES[0].filename}" class="pager-link">{html.escape(ITINERARIES[0].name)}</a>
    </section>
  </main>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    (ROOT / "index.html").write_text(render_index(), encoding="utf-8")
    (ROOT / "logistics.html").write_text(render_logistics(), encoding="utf-8")
    for itin in ITINERARIES:
        (ROOT / itin.filename).write_text(render_itinerary(itin), encoding="utf-8")
    print(f"Built: index.html, logistics.html, {', '.join(i.filename for i in ITINERARIES)}")


if __name__ == "__main__":
    main()
