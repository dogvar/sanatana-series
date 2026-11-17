# Tulsi Vivah 2026 · QA and preview

[Research and date evidence](research.md) · [Artwork provenance](artwork.json) · [Browser results](browser-qa.json)

- The festival validator passed for all eight festival pages. It checked bilingual anchor parity, local image and link references, language alternates, the new reference dates and calendar data.
- The existing guide preservation check passed for the four Dhanteras and Diwali pages. The two Diwali and two Chhath pages only add related links. The existing Chhath hero pin stays in place.
- Chrome passed both new editions at 320, 390, 768 and 1440 px. Checks included reflow, real image dimensions, alt text, date sequence, content links, keyboard skip and contents navigation, language switching, the local Hindi font, metadata and the homepage and calendar links. The guide contents and reading path also work with JavaScript disabled in the 390 px preview.
- The existing layout suite passed 24 page and viewport combinations. The existing narrow-layout and progressive-enhancement suite passed.
- Seven WebP placements were checked visually for subject and framing. The accompanying social image is a separate crop of the courtyard image. Ceremony images and devotional art are identified as AI-generated. Sampled body, link, and timeline text pairs measured at least 5.35:1. Manual browser review used Chrome without a screen reader.

| View | English | हिन्दी |
| --- | --- | --- |
| Desktop hero | [1440 px](screenshots/tulsi-vivah-1440-hero.webp) | [1440 px](screenshots/tulsi-vivah-hi-1440-hero.webp) |
| Mobile hero | [390 px](screenshots/tulsi-vivah-390-hero.webp) | [390 px](screenshots/tulsi-vivah-hi-390-hero.webp) |
| Sacred stories | [Desktop](screenshots/tulsi-vivah-1440-stories.webp) | [Mobile](screenshots/tulsi-vivah-hi-390-stories.webp) |
| Wedding rites | [Desktop](screenshots/tulsi-vivah-1440-ritual.webp) | [Mobile](screenshots/tulsi-vivah-hi-390-ritual.webp) |
