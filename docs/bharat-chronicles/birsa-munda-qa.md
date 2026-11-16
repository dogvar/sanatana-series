# Birsa Munda · Draft review and QA

The English and Hindi editions share all 12 sections, nine timeline entries, six glossary entries and 17 bibliography entries. The article before the bibliography is approximately 3,070 English words including timeline and glossary labels. The historical review and artwork credits are in [the research notes](birsa-munda-research.md).

## Checks

- Ran the repository's changed-page local link check and festival validator. The existing guide preservation check also passed against main at `c694eb4`.
- Ran the existing festival layout suite across 24 page and viewport combinations and the existing narrow-screen, no-JavaScript and reduced-motion checks. The first layout run, concurrent with asset generation and browser capture, reported incomplete homepage image loads on one viewport. A subsequent standalone run passed all 24 combinations, with the referenced image files present.
- Checked both biography editions in Chrome at 320, 390, 768 and 1440 px. Verified reflow, Devanagari font availability, skip-link focus, timeline operation with Enter and Space, bilingual navigation, in-page anchors, canonical and reciprocal alternates, structured data, image decoding and absence of JavaScript exceptions or failed local responses. The homepage collection and both article links also passed at all four sizes. The contents and timeline work without JavaScript. [Browser report](browser-qa.json).
- Checked key text colors against their backgrounds. Main copy on parchment is 12.3:1. The lowest tested key pair is gold on the hero gradient at 4.9:1.
- Reviewed the sources through their online pages or accessible PDF copies. Replaced an unreliable Rycroft mirror with the journal's own page. Some Cambridge, India Code, PIB, NCERT and news links served their contents through the research browser but timed out or blocked the separate automated HEAD check. The research notes give bibliographic details and alternatives where available.
- Visually reviewed desktop and mobile article captures. Screen-reader and non-Chromium browser testing were outside this pass.

## Screenshots

| View | English desktop | English mobile | Hindi desktop | Hindi mobile |
| --- | --- | --- | --- | --- |
| Opening | [1440 px](screenshots/birsa-munda-hero-1440.webp) | [390 px](screenshots/birsa-munda-hero-390.webp) | [1440 px](screenshots/birsa-munda-hi-hero-1440.webp) | [390 px](screenshots/birsa-munda-hi-hero-390.webp) |
| Ulgulan chapter | [1440 px](screenshots/birsa-munda-ulgulan-1440.webp) | [390 px](screenshots/birsa-munda-ulgulan-390.webp) | [1440 px](screenshots/birsa-munda-hi-ulgulan-1440.webp) | [390 px](screenshots/birsa-munda-hi-ulgulan-390.webp) |
| Timeline | | | [1440 px](screenshots/birsa-munda-hi-timeline-1440.webp) | [390 px](screenshots/birsa-munda-hi-timeline-390.webp) |

## Scope

The collection uses a permanent homepage section, with links from the desktop navigation and mobile hero. The repo has no Chhath Puja guide or sitemap to update; the festival catalog and calendar are untouched. The existing GitHub project serves as the route for corrections. The optional PDF and additional art production remain outside this draft. The research notes include briefs for the remaining images.
