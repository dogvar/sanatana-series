# Sanatana Series — Codex repository instructions

This repository is the **source of truth** for https://dogvar.github.io/sanatana-series/.
Work on a feature branch and open a **draft pull request**. Never push content changes directly to `main`, merge a PR, or publish without the owner's explicit approval.

## New festival guide workflow
1. Read the current `index.html`, `calendar.html`, `README.md`, existing comparable English/Hindi guide pages, and `article-responsive.css` before editing. Preserve current functionality, layout, and all existing guides.
2. Research festival dates using reputable, location-specific panchang sources. Distinguish festival date from puja/muhurat time; mention city, time zone, and regional or tradition-specific differences. Never invent dates, timings, or citations. The calendar is an editorial selection, **not** a live panchang API.
3. Create an original, substantial, readable English guide `<slug>.html` and a complete Hindi edition `<slug>-hi.html`. Tell the story with cultural context, distinguish scriptural accounts from regional folklore, explain significance and practical observances, and include sources. Do not use machine-like literal Hindi or placeholder text.
4. Add culturally accurate, **subject-matched** illustrations to `images/` (prefer optimized WebP), with useful alt text. Do not replace them with generic symbols or unrelated deity pictures. Verify copyright and provenance for external images. If generation tooling is unavailable, report the missing asset rather than linking to a nonexistent image.
5. Update the homepage card and cross-links, calendar highlights only when verified, social preview metadata, and README guide listing. Preserve English/Hindi navigation. Do not overwrite newer changes by copying an old ZIP wholesale.
6. Maintain the premium dark editorial aesthetic, legible and prominent Devanagari wordmark, responsive layouts, and accessible keyboard navigation. Avoid the misleading heading “Always in season”.
7. Check relative links, image references, mobile viewport, bilingual parity, and dates. Summarize files changed and any unverified facts in the PR description.

## Safety and publishing
- Do not add API keys or secrets to static pages or GitHub Actions.
- No direct commits to `main`; request review via draft PR.
- GitHub Pages should deploy only through the repository's existing publishing setup after the owner merges.
- Treat GitHub Actions checks as mechanical validation, **not** proof of historical or religious accuracy.
