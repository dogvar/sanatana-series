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

## Storytelling and editorial standards

Sanatana Series is a personal cultural blog for families, young readers, international visitors and people discovering Indian traditions for the first time. Research deeply. Write simply. Tell the story beautifully. Keep the evidence available without interrupting the reader. These standards apply to new guides and substantial narrative revisions. Leave older articles in place unless a revision is requested or needed for the current task.

### Research and reader-facing copy

- Record detailed research, verification, source comparisons, uncertainties, editorial decisions and bibliographic information in separate research notes. Use the article for the story, essential context, illustrations, concise source notes and optional further reading.
- Introduce the main source or tradition near the story heading. Place short links or numbered notes at natural paragraph or section boundaries. End with compact sources and further reading. Keep verse-by-verse comparisons and research methodology out of the article unless readers need them to understand a consequential difference.
- When versions differ, choose a well-supported account and tell it coherently. Briefly explain consequential alternatives afterward, with links. If two accounts are central, tell them as separate stories. Focus on differences that affect characters, events, endings or festival meaning. Never hide a major contradiction or combine incompatible episodes into an invented account.

### Narrative craft and accuracy

- Open with a moment, question or situation that draws the reader in. Introduce the main characters, their relationships, setting, conflict and stakes as they become relevant. One or two short introductory paragraphs will usually suffice. Add further context where the story calls for it.
- Tell events in a clear sequence with natural transitions, well-paced paragraphs, and emotional depth grounded in the source. Give turning points room to breathe and let the ending show why the story matters. Use warm, plain language. Avoid compressed news-style summaries, repeated source attribution, artificial suspense, inflated drama and decorative prose.
- Use length as a pacing judgment. Roughly 350–650 words often suits an individual sacred story when the source supports it. Shorter stories may need less. Use natural breaks for longer stories and expand only where the material warrants it.
- Do not invent dialogue, scriptural quotations, supernatural events, historical incidents, motives, private thoughts, emotions or scenery. Preserve morally difficult episodes with care and retain the source's context. Acknowledge meaningful uncertainty briefly where it affects the reader's understanding.

### Match the writing to the material

- **Sacred narratives:** Write immersive, respectful storybook prose and identify the source tradition.
- **Historical biographies:** Write engaging narrative nonfiction grounded in the record, with no invented events or dialogue.
- **Festival rituals:** Explain customs clearly and practically, with room for community variation.
- **Dates and calendars:** Give concise, verifiable information and follow the location and timing requirements above.
- **Philosophy and reflections:** Keep explanations approachable and distinguish textual teachings from modern reflection.
- **Science and health:** Use appropriate evidence and distinguish traditional beliefs from demonstrated findings.

### Hindi and visual storytelling

- Give the Hindi edition the same editorial care as the English. Write natural, accessible Hindi with a warm literary voice. Avoid literal translation and unnecessary Sanskritized or bureaucratic vocabulary. Preserve important events, meanings and factual qualifications in both editions.
- Use illustrations that help readers recognize a scene, character, object or tradition. Vary composition and visual style where the subject warrants it. Avoid generic decoration, repetitive images and visual details that contradict the cited narrative or historical evidence. Follow the existing cultural accuracy, accessibility and provenance requirements.

### Final editorial review

Before submitting a guide, read both editions as a first-time visitor would. Check that the opening engages, the context is sufficient, the events unfold clearly, the quotations or source notes support the prose, and the ending gives the story meaning. Cut background that interrupts the story, and move detailed comparisons to the research notes. Confirm that the Hindi reads naturally and preserves the same facts and qualifications. Rewrite any narrative that reads like a research report or encyclopedia summary. Follow all existing accuracy, accessibility, repository and publishing checks.
