# Guru Nanak Dev Ji Gurpurab: cultural and editorial QA

Reviewed 21 November 2026. Automated checks prove structure and exact text matches. They do not prove historical or religious accuracy.

## Verified

- All quoted Gurbani matches BaniDB exactly for Gurmukhi, transliteration, Ang and author, in both editions.
- English and Hindi have the same sections, anchors, chapters, stories and qualifications.
- Janamsakhi stories carry a visible label and are separated from Gurbani and from the historical narrative.
- Guru Nanak's compositions are distinguished from the 1604 compilation and the 1708 conferral of Guruship.
- Browser checks at 360, 390, 768 and 1440 px covered both new pages, the homepage, calendar, Tulsi Vivah (both languages), Diwali and Chhath: no horizontal overflow, script errors, failed local requests or broken images. Details are in `browser-qa.json`.
- Language switching, contents anchors and the keyboard skip link work on the new pages.
- `scripts/validate_festival_guides.py` passes. Tulsi Vivah files are unchanged.

## Not complete

- **Illustrations:** 6 of 12 are placed after full-size review. Plates 1, 7, 8 and 9 were held for cultural or visual errors, and Plates 11 and 12 are not yet supplied. See `artwork.json`.
- **Social image:** no page-specific image yet, so the pages use a summary card.
- **Sikh reviewer:** no knowledgeable Sikh reader has reviewed the guide.
- **Hindi:** written and proofread by the agent, not by a native-speaking editor.
- **Sources:** several preferred sources were inaccessible. See `research.md`.
- **Gurmukhi font:** the pages rely on device fonts. It rendered correctly in Chrome on macOS. Other devices were not tested.

## Questions for editorial approval

1. May the Guru be depicted at all, and if so how? The recommendation is no visible face.
2. Should the guide publish with placeholders, or wait for artwork?
3. Is the English BaniDB wording ("God", "he") acceptable, or is a gender-neutral translation preferred?
4. Should the guide name the Kartik and Vaisakh date debate more fully, or keep the current brief note?
5. Who will carry out the Sikh community review before publication?
