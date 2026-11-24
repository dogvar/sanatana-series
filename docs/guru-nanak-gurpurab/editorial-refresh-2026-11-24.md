# Guru Nanak editorial refresh — 24 November 2026

Starting point: main `c263f862e6f44248fc0d2712dafe20ba1255d025`. The owner approved the proposed homepage cover, a story illustration for the guide hero, improved chapter hierarchy and source-sensitive narrative editing. They subsequently asked that Hindu beliefs be represented accurately and respectfully, supplied two greeting images and the existing bilingual videos, and flagged the English pronunciation of Ek Onkar. Work is for a draft PR; no publication is authorized.

## What changed

- Following the owner's clarification, the homepage retains the Sanatana Series ghats hero, original headline and discovery links. Guru Nanak appears as a compact latest-guide card beneath the hero actions, with the supplied cover thumbnail and English/Hindi links. `HOME_FEATURE` selects this card independently of date-driven festival status. The card remains horizontal on mobile instead of recreating the old stretched plaque.
- The article hero reuses the existing Mardana illustration; the near-square greeting is removed from that role. Mobile title/lead precede the art. Existing illustrations and older greeting assets remain archived, not overwritten.
- A compact reference-date panel links to the official CAG Punjab 2026 holiday list and to local-gurdwara guidance. It does not claim location-aware timing. The birth-month question remains in an optional note. The seven-stop timeline is optional and distinguishes his lifetime from later scripture milestones.
- Three journey sakhis have coherent narrative progression, individual anchors, source links and separate reflections. The thread story was revised for sensitive framing. The three daily commitments have greater prominence; all original definitions remain available. All original Gurmukhi, transliteration and translation paragraphs remain unchanged; secondary layers are optional.
- Two original story illustrations were generated using the built-in ImageGen tool: Lalo's hospitality and Haridwar. Full-resolution inspection checked posture, hands and the opposite offering directions. These are interpretive illustrations, not records of historical appearances or independent proof of the events.
- The approved portrait greeting with the printed `guru-nanak-gurpurab.html` address is available at the end of both guides. The other supplied square greeting prints a nonexistent `guru-nanak-dev.html` URL and was not selected.
- A variable Noto Serif Gurmukhi font is self-hosted with its unmodified OFL licence. Source: Google Fonts, `ofl/notoserifgurmukhi`, fetched 24 November 2026. Only the font filename was normalized; outlines were not altered.

## Sensitive interfaith passages: evidence and limits

**The user explicitly requested a correctness check before retaining the sacred-thread and water-offering stories.** Their inclusion here establishes that they are documented Sikh traditional accounts; it does not assert that historians have independently proved each incident.

### Sacred thread

- [Macauliffe, The Sikh Religion, vol. I (1909), chapter II](https://sacred-texts.com/book/the-sikh-religion-volume-1/life-of-guru-nanak-chapter-ii), pp. 15–18, narrates the ceremony and refusal. This is a later devotional biography based on Sikh traditions, not an eyewitness record.
- The underlying teaching has direct scriptural support: `ਦਇਆ ਕਪਾਹ ਸੰਤੋਖੁ ਸੂਤੁ ਜਤੁ ਗੰਢੀ ਸਤੁ ਵਟੁ ॥`, Sri Guru Granth Sahib Ji, Ang 471, BaniDB verse 21166, shabad 1732. The BaniDB API at `https://api.banidb.com/v2/angs/471/G` was consulted during this revision. The guide paraphrases compassion, contentment, self-restraint and truth; it does not invent a new quotation or claim that the verse independently proves the childhood ceremony.
- For Hindu context, [Sri Sathya Sai Seva Organisations India's Upanayana explanation](https://static.ssssoindia.org/wp_uploads/2018/10/02215353/Samoohika-Upanayana-Mahotsavam-converted.pdf) describes initiation into learning/Gayatri and responsibilities toward parents, knowledge/teacher and society. The guide acknowledges this meaning. Avoid the former implication that the thread is merely a physical string whose wearers expect it alone to guarantee virtue.
- Removed blanket phrasing about all Hindu boys, broad claims about present-day eligibility and mocking rhetorical questions. The Sikh teaching is retained with its own context.

### Haridwar

- [Macauliffe, vol. I, chapter IV](https://sacred-texts.com/book/the-sikh-religion-volume-1/life-of-guru-nanak-chapter-iv), pp. 50–51, records east-facing ancestral offerings, Guru Nanak cupping water toward the west, his field explanation and the dialogue about distance. The episode is labelled a Janamsakhi story. The precise scene is not independently established by the consulted material.
- The original telling's polemical assertions and hostile language are not adopted as editorial statements. The guide recounts the water/field exchange without asserting that it disproves Hindu belief.
- [BAPS, Shraaddh](https://www.baps.org/Article/2011/Shraaddh-2084.aspx) describes ancestral offerings in terms of faith, remembrance, prayer and benefit to the departed. Its Hindu theological account is not reducible to ordinary physical transport of water. The short reader-facing context acknowledges that the dialogue within the sakhi is not a complete account of Hindu beliefs. No claim is made that all ancestral rites are only symbolic, or that all Hindu traditions practise them identically.
- The scene is not a ritual instruction diagram. Direction, form and interpretation of real Hindu rites vary; the illustration follows this particular narrative's east/west contrast.

### Lalo and Mecca

- Macauliffe chapter IV, pp. 43–44, supports Lalo's hospitality, Bhago's summons, the two foods and their miraculous milk/blood contrast. The new image shows the earlier meal, not graphic liquids. No invented repentance, conversion or private thoughts were added. The separate Ang 722 reference is not used as proof of the feast miracle.
- [Macauliffe, chapter XV](https://en.wikisource.org/wiki/The_Sikh_Religion/Volume_1/Life_of_Guru_Nanak#Chapter_XV), pp. 174–175, recounts the Mecca feet/Kaaba episode and also notes a spiritual interpretation. The narrative clearly identifies it as a traditional account and the optional note preserves the interpretive difference. It is not presented as a verdict against Islam or its reverence for the Kaaba.
- Macauliffe's 1909 volume is public domain. Its accounts are used as traditional narrative sources; it is not treated as neutral contemporary verification of every biographical detail. Preferred modern Sikh-studies sources listed in the original research notes were not all consulted afresh.

## Date

[Official Accountant General (Audit-I), Punjab, holiday list](https://www.cag.gov.in/ag/punjab/en/page-ag-punjab-holiday-list), Gazetted Holidays 2026, item 16: Guru Nanak's Birthday, 24 November, Tuesday. This corroborates the reference civil date. No muhurat or automatic reader-location adjustment is invented.

## Videos supplied by the owner

The final folder contains two H.264/AAC 1920×1080, 25 fps masters: English 368.200 seconds / 361,999,544 bytes; Hindi 389.480 seconds / 353,355,653 bytes. Both decoded completely without FFmpeg errors. Sampled frames were inspected; this does not constitute a continuous viewing or a human listening/intonation approval.

Their own production configuration records Neerja English at **−6%** and Swara Hindi at **−5%**, which differ from the older Tulsi baseline. Preserve these actual episode settings for any correction. Original subtitles are matching-language. The owner's newer preference is opposite-language subtitles for future productions, with same-language captions optional; no replacement subtitles or script rewrites have been silently made here.

The flagged English term spans original subtitle cues 34–35 within **02:13.820–02:19.910**. The owner preferred Option B (Devanagari reading) in the same Neerja voice at the episode's −6% pace. A separate local English review master replaces that sentence and the subsequently approved lives/Ravi sentences and copies the original video stream. The music bed is rebuilt quietly from the same licensed track only beneath those three sentences because separate stems were not supplied; the rest of the pre-encoding PCM mix is unchanged. This still needs the owner's in-context listening check. The supplied masters/MP3s remain untouched; all audio auditions and corrected delivery renders stay in the local production workspace, not Git.

The other flagged terms have separate auditions: the single occurrence of **lives** is the verb in “message lives today” (cue 4, 00:15.640–00:21.050); **Ravi River** occurs in cue 50, 03:19.280–03:24.040. [Punjabi University's Encyclopaedia of Sikhism, Kartarpur](https://eos.learnpunjabi.org/KARTARPUR.html) spells the river **Rāvī**; use a long-aa “Raa-vee” pronunciation, not a factual rename to “Rabi”. The owner subsequently approved both auditions on 24 November 2026; both are included in the separate English review master. The original master remains untouched.

The two videos total 715,355,197 bytes (about 682.2 MiB). Neither is committed to the website. No public host, upload or embed URL has been approved. A later approved YouTube embed or another suitable external host avoids adding these masters to the Pages repository. The current guide has no empty or broken media player.

## QA and remaining approval

See `editorial-qa-2026-11-24.json` and `screenshots/` for structural/browser evidence. The repository validator now includes the Guru Nanak pair and Gurmukhi font path, without incorrectly imposing Hindu panchang lookup requirements on this Sikh guide. Scripture paragraph preservation was checked against the starting commit. Page-specific CSS/JS changes leave unrelated guides' shared assets intact.

Remaining human review: complete English/Hindi reading, Sikh cultural review, optional native Hindi proofreading, interpretation of traditional accounts, and listening to the flagged English narration. These are not replaced by passing automated checks. Review the draft PR and complete articles before merging or publishing.
