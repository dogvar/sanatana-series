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

## Sanatana Kathavachan production

Offer bilingual illustrated, podcast-style narration for new guides when editorial approval and suitable audio tools are available. Use the approved English and Hindi scripts as controlled production inputs. Extract only marked spoken passages and retain original files and checksums. Flag source or pronunciation concerns for editorial review before changing a script.

Start each new episode with a consistent storyteller reference and a 30–45 second sample in each language. Use gentle animation, culturally appropriate artwork and independently timed natural delivery. Reuse relevant existing artwork. Obtain approval of the voice, character and pilot before producing complete episodes. Check source fidelity, pronunciation, pace, captions, sound levels, rendered frames and the final listening experience. Clearly report which checks were performed and any unresolved quality issues.

Organize scripts, artwork references, voice settings, timing data, subtitles, project sources, licenses and QA notes under a reusable episode directory. Prefer available local or free tools and require authorization for paid APIs. Voice cloning requires consent. Keep large source images, models and video renders outside the website repository, with an asset manifest that records file hashes and provenance.

After episode approval, integrate a reusable Kathavachan component near the beginning of the English and Hindi guides. Preserve the written article. Provide clearly labelled bilingual audio and video, large accessible controls, speed adjustment, fullscreen video, optional subtitles and MP3 downloads, lazy loading and no autoplay. Review media size and hosting limits before adding files. Use a draft PR and publish only with the owner's approval.

### Approved recurring Kathavachan production standard

The owner approved the Tulsi Vivah Hindi and English pilots: retain their recurring adult Indian woman storyteller, terracotta sari with emerald edge, character sheet and host layers. Use `production/kathavachan/tulsi-vivah/production.json` and its asset manifest as the baseline. Preserve the approved Swara Hindi and Neerja Indian-English voices at -8% rate unless the owner approves a change; keep the exact marked narration without shortening or rewriting it. Save the original scripts and checksums. Generate each language independently and use its measured timings.

Use varied illustrations matching the actual narrated events, with the narrator appearing briefly at the opening, transitions and closing. Inspect every selected image at full resolution before rendering, particularly shoulder/elbow/wrist connections, finger counts, grips on vessels and weapons, deity iconography, and continuity of objects such as the kavacha. A contact sheet alone is insufficient. Regenerate faulty anatomy or contradictory imagery; inspect actual rendered shots and subtitles again afterward.

Export 1080p H.264/AAC masters, optimized web copies, separate MP3s and matching-language SRT/WebVTT. Aim for -16 LUFS integrated and true peaks below -1 dBTP in actual encoded files. Use suitable traditional Indian instrumental music with recorded licence/provenance and gentle ducking beneath speech. Do not substitute a synthetic drone placeholder. Keep the music quiet and the voice clear; do not add narration echo, delay or reverb without owner approval. Provide readable shaped Hindi captions, natural pacing, gentle movement and cinematic transitions. Record the difference between automated checks, visual review and human listening; never claim unperformed listening or pronunciation approval.

Preserve character and visual references, approved voice settings, production configuration, exact scripts, cue timings, prompts, hashes and rebuild instructions for future episodes. Large masters and raw art stay in the separately delivered production workspace. Include optimized delivery media in Git only after measuring repository size, individual-file limits and Pages transfer requirements. Prefer owner-approved external hosting as the catalogue grows. Keep guide prose and SEO intact; prepare integration in a draft PR and obtain final approval before publishing.
