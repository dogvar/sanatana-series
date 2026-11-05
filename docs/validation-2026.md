# Dhanteras / Diwali validation

Base inspected: `5692fbe59055cd2df0531110c3ababfbcbb8db69` (`main`). Neither requested guide pair existed there. No open PR for these guides was found. Attachment prose was selected individually; no existing page or image was replaced from a ZIP.

Validation completed 5 November 2026. The global-diaspora revision replaces the city-specific guide callouts with sourced reference dates, lunar observances and an external city lookup; the calendar’s stored location-labeled dates are retained:

- Dependency-free festival validator: passed. Checks four new guides, reciprocal language links and section IDs, local file/anchor references, image attributes and social image paths, sourced reference dates and local panchang links, calendar dates and generated homepage/calendar data links.
- Existing changed-page link/image check from `.github/workflows/validate.yml`: run locally against the committed diff. See the draft PR for its outcome and remote CI status.
- Headless Chrome / Playwright: passed all 24 page/viewport combinations (six pages × 360, 390, 768, 1440 px). No horizontal document overflow, broken image loads or JavaScript page errors. Language navigation, keyboard skip links, homepage filters, calendar month navigation and external location selection passed. The reusable browser script freezes the date to 5 November 2026. Details: [JSON report](browser-check-2026.json).
- Visual review: checked mobile and desktop screenshots, dark/gold colors, Devanagari wordmark, chapter layout and all fourteen original illustrations. [Screenshots](screenshots/) are review artifacts, not a separate deployment. HTML image dimensions match the generated assets.
- Additional artwork pass: **16/16** guide/viewport combinations passed at 360, 390, 768 and 1440 px, including all new illustrations and the five illustrated Diwali overview cards. [Artwork layout report](art-layout-check-2026.json).
- `git diff --check`: passed. No existing guides or images deleted; the changes retain existing article styles and navigation. Only the homepage, calendar, README and validation workflow are modified among pre-existing files.

## Open editorial issues

- Bali Pratipada and Gujarati New Year: the guides explain regional rules without asserting a worldwide Gregorian date or a local muhurat.
- Narak Chaturdashi festival listing and abhyanga bath date differ between sources; no bath window is invented.
- Archived research records location and temple-event differences. Reader-facing chapters now explain the lunar sequence and direct each household to local timing.
- Religious narratives, Hindi prose and AI-generated iconography should receive the owner's editorial/cultural review before merge. Automated checks cannot certify these judgments.
- Unrelated existing calendar dates were preserved, not re-audited. Temple schedules can change.

No merge, Pages deployment, publication or default-branch write is part of this change.
