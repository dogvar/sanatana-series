# 🪔 Sanatana Series

**Free, bilingual guides to Hindu festivals, sacred literature, prayers and dharmic traditions.**

🌐 **Website:** https://dogvar.github.io/sanatana-series/  
📚 **Explore all guides:** [Open the homepage](https://dogvar.github.io/sanatana-series/)

Sanatana Series shares accessible explanations of traditions, observances and stories in English and Hindi. The site is hosted on GitHub Pages and can be read without creating an account.

## Explore the guides

The following English and Hindi pages are included in this repository:

| Guide | English | हिन्दी |
|---|---|---|
| Aarti Sangrah | [aartis.html](aartis.html) | [aartis-hi.html](aartis-hi.html) |
| Adhik Maas | [adhik-maas.html](adhik-maas.html) | [adhik-maas-hi.html](adhik-maas-hi.html) |
| Akshaya Tritiya | [akshaya-tritiya.html](akshaya-tritiya.html) | [akshaya-tritiya-hi.html](akshaya-tritiya-hi.html) |
| Dhanteras 2026 | [dhanteras.html](dhanteras.html) | [dhanteras-hi.html](dhanteras-hi.html) |
| Diwali 2026 (extended) | [diwali.html](diwali.html) | [diwali-hi.html](diwali-hi.html) |
| Buddha Purnima | [buddha-purnima.html](buddha-purnima.html) | [buddha-purnima-hi.html](buddha-purnima-hi.html) |
| Buddhism Across Asia | [buddhism-spread.html](buddhism-spread.html) | [buddhism-spread-hi.html](buddhism-spread-hi.html) |
| Ganesh Chaturthi | [ganesh-chaturthi.html](ganesh-chaturthi.html) | [ganesh-chaturthi-hi.html](ganesh-chaturthi-hi.html) |
| Gayatri Mantra | [gayatri-mantra.html](gayatri-mantra.html) | [gayatri-mantra-hi.html](gayatri-mantra-hi.html) |
| Bhagavad Gita | [gita.html](gita.html) | [gita-hi.html](gita-hi.html) |
| Guru Purnima | [guru-purnima.html](guru-purnima.html) | [guru-purnima-hi.html](guru-purnima-hi.html) |
| Hanuman Jayanti | [hanuman-jayanti.html](hanuman-jayanti.html) | [hanuman-jayanti-hi.html](hanuman-jayanti-hi.html) |
| Hindu New Year | [hindu-new-year.html](hindu-new-year.html) | [hindu-new-year-hi.html](hindu-new-year-hi.html) |
| Jagannath Rath Yatra | [jagannath-rath-yatra.html](jagannath-rath-yatra.html) | [jagannath-rath-yatra-hi.html](jagannath-rath-yatra-hi.html) |
| Janmashtami | [janmashtami.html](janmashtami.html) | [janmashtami-hi.html](janmashtami-hi.html) |
| Kabir Jayanti | [kabir-jayanti.html](kabir-jayanti.html) | [kabir-jayanti-hi.html](kabir-jayanti-hi.html) |
| Mahavir Jayanti | [mahavir-jayanti.html](mahavir-jayanti.html) | [mahavir-jayanti-hi.html](mahavir-jayanti-hi.html) |
| Nag Panchami | [nag-panchami.html](nag-panchami.html) | [nag-panchami-hi.html](nag-panchami-hi.html) |
| Narasimha Jayanti | [narasimha-jayanti.html](narasimha-jayanti.html) | [narasimha-jayanti-hi.html](narasimha-jayanti-hi.html) |
| Chaitra Navratri | [navratri.html](navratri.html) | [navratri-hi.html](navratri-hi.html) |
| Onam | [onam.html](onam.html) | [onam-hi.html](onam-hi.html) |
| Pitru Paksha | [pitru-paksha.html](pitru-paksha.html) | [pitru-paksha-hi.html](pitru-paksha-hi.html) |
| Ram Navami | [ram-navami.html](ram-navami.html) | [ram-navami-hi.html](ram-navami-hi.html) |
| Ramayana | [ramayana-journey.html](ramayana-journey.html) | [ramayana-journey-hi.html](ramayana-journey-hi.html) |
| Shani Jayanti | [shani-jayanti.html](shani-jayanti.html) | [shani-jayanti-hi.html](shani-jayanti-hi.html) |
| Sharad Navratri | [sharad-navratri.html](sharad-navratri.html) | [sharad-navratri-hi.html](sharad-navratri-hi.html) |
| Shravan Month | [shravan-month.html](shravan-month.html) | [shravan-month-hi.html](shravan-month-hi.html) |

### Interactive tools

- [Hindu Calendar](calendar.html)
- [Festival Date Card Generator](date-card-generator.html)

## Website features

- English and Hindi article editions.
- Responsive layouts for mobile, tablet and laptop screens, including a shared article stylesheet.
- Article cover illustrations in `images/guide-covers/`, with existing devotional imagery retained.
- Page-specific Open Graph artwork for social sharing, with `sanatana-og.png` as a fallback.
- A searchable, categorized homepage and links to individual guides.
- Static hosting: no account, database or paid hosting service required.

## Project structure

```text
index.html                  Homepage
article-responsive.css      Shared responsive article styling
*.html                      English and Hindi articles and tools
images/                     Festival illustrations and other imagery
images/guide-covers/        Decorative article covers
sanatana-og.png             General social-preview fallback
README.md                   Project documentation
```

## Publishing illustrated festival guides

The repository is the source of truth. Follow [AGENTS.md](AGENTS.md) and the repeatable [festival workflow](docs/festival-workflow.md). Work on a feature branch and open a **draft PR**. The owner reviews and merges; GitHub Pages uses its existing deployment setup. Do not push content directly to `main` or replace the site with an older ZIP.

- Review comparable English/Hindi pages and preserve current navigation, images and styling.
- Record city, year, timezone, source and verification date in a [date evidence file](docs/festival-dates-2026.md). Festival dates, ritual windows and temple events are different facts.
- Use original subject-matched artwork, localized alt text and an [asset provenance record](docs/festival-artwork-2026.json).
- Link both editions from the homepage, related guides and verified calendar highlights.
- Run `python3 scripts/validate_festival_guides.py` and the existing changed-page link check. Manually inspect mobile, tablet and desktop layouts before review.

### Dhanteras and extended Diwali 2026

These pages integrate selected prose from the owner's supplied November 2026 ZIP drafts. Neither guide existed on the default branch at the start of this change. Old homepage, calendar, CSS and images from the ZIPs were not copied over the repository. The Diwali draft was expanded with separate Bali Pratipada and regional chapters, fuller Hindi content and corrected date notes. New illustrations were generated for this change; see the provenance record for prompts and image paths.

The guides address the global diaspora. Their redesigned **When** sections distinguish a sourced 2026 reference date, the lunar observance and a reader's local puja timing. Dhanteras is shown as **6 November** and Diwali as **8 November**, using Drik Panchang's New Delhi reference listings. Neither date is presented as an automatically localized result. Readers can open the festival-specific panchang, select their city and confirm 2026. Exact city-specific clock windows are not printed in the guides.

The calendar retains its separately labeled Amsterdam editorial highlights; selecting an external lookup location does not recalculate that stored data. Earlier Netherlands research is preserved in the evidence file for traceability. Local observance and temple schedules still require confirmation.

### Heritage editorial design

The visual refresh preserves the published English/Hindi text, links, metadata and date guidance while improving frontispieces, chapter compositions, typography and mobile reading. See [design notes, artwork review, validation and screenshots](docs/redesign/README.md). Deepavali has its own rangoli-inspired margin pattern and diya separators; Dhanteras retains its approved design.

## Updates and community

A WhatsApp group or channel may be added later for new guides and festival reminders. No WhatsApp invitation link is configured here yet. A newsletter link may also be offered separately; the static website does not itself provide an email-subscription backend.

## Notes

The site is an educational resource. Festival dates and local observances can vary by region, tradition and panchang; readers should confirm local dates where needed.

---

Created and maintained by the Sanatana Series project.
