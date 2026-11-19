# Complete episode production and hosting

## Approved baseline and editorial control

The owner approved both Hindi and English pilots and requested the complete supplied scripts without rewriting or shortening. The approved narrator is an adult Indian woman in a terracotta sari with emerald edge. Her original character sheet, open-eye and blink layers are retained in the separately delivered workspace, with lossless WebP references in Git. Existing courtyard, preparation, ceremony, Shaligram and twilight guide artwork is reused.

Read only `<!-- START -->` through `<!-- END -->` in the two unchanged script files. All 25 Hindi and 29 English paragraphs are present. Source SHA256 and cue text are recorded in `timing/timings.json`. The original seven-file ZIP is retained separately. No headings, markup, new dialogue or shortened passages were narrated.

The approved free online voices are `hi-IN-SwaraNeural` and `en-IN-NeerjaNeural`, both at `-8%` rate via the already installed edge-tts 7.3.1 client. No voice cloning, paid speech/video API, new package or model installation was used. Existing FFmpeg, Pillow, NumPy and browser tools perform production. These are online service voices, not offline models; future endpoint availability and service distribution terms are separate from the client software license. Keep that distinction in the final publication review. [edge-tts](https://github.com/rany2/edge-tts)

## Visual production

Built-in ImageGen generated the new story artwork, with prompts in `art-prompts.json`. Scene timing follows each language's measured paragraph boundaries. The host appears at the opening, question and close; most of the story uses varied subject-matched illustrations. Gentle breathing, blinking, environmental movement, different camera moves and crossfades retain the approved illustrated storytelling format. The animation draws at 12 fps and is delivered at 24 fps. No continuous lip sync is implied.

Review every selected illustration at full resolution before rendering. Initial drafts incorrectly included extra characters; they were rejected. The owner rejected two battlefield versions for the trident-arm anatomy and static staging. The final scene was completely redrawn: Shiva advances with two clearly separate arms and an unobstructed grip, while Shankhachuda is in a moving chariot with distant opposing forces. Both episodes were rerendered with that replacement. The handover and disguised arrival were also corrected so the protective amulet is not duplicated or still worn after being given away. The full-resolution selected images and actual rendered shots were inspected again. Rejected variants remain outside Git for provenance.

The narrator, costumes, deity iconography and story objects remain consistent. Kavacha is represented as a neck amulet, following the guide's source. The battlefield avoids invented combat choreography, and the deception is staged without intimate imagery. The supplied scripts compress the source account; they were preserved rather than expanded. The Gandaki sequence is symbolic landscape, not a speculative literal transformation.

The script claims were checked against [Devi Bhagavata Purana 9.23](https://www.wisdomlib.org/hinduism/book/devi-bhagavata-purana/d/doc57336.html) and [9.24](https://www.wisdomlib.org/hinduism/book/devi-bhagavata-purana/d/doc57337.html), with the existing guide as context. The original production notes document the distinction between the script's abbreviated reception episode and the fuller primary account.

## Sound and captions

The approved speech has independent language timing, an opening 0.8-second lead, half-second paragraph gaps and a short closing tail. The owner rejected the initial synthetic tone bed as echo-like. It has been removed completely. The replacement uses the locally available bansuri, sitar and tabla instrumental from the earlier Diwali production, identified and licensed in `MUSIC-LICENSE.md`. Music is set around -32 LUFS before a further 4 dB reduction beneath speech; short fades and a four-second overlap extend the source if needed. Narration uses the exact original speech, centred in stereo, with no delay, echo, reverb or time stretching. Two-pass mastering targets -16 LUFS and -2 dBTP for safe encoded peaks. Actual encoded measurements and hashes are in `qa/complete-report.json`.

Every script word appears in the corresponding captions. Short cues use at most two wrapped lines. Their timing is proportionally segmented within measured paragraph speech boundaries, not a forced alignment of individual words. The 1080p masters burn readable captions with shaped Noto Serif Devanagari in Hindi and Arial in English, white on a dark box. Website copies use default-on, switchable WebVTT. Fine subtitle synchronization and full-episode pronunciation/naturalness still require the owner's listening review. No assistant listening review is claimed.

## Website component

`kathavachan.js` keeps episode media paths in one catalogue. Add a `[data-kathavachan][data-episode="slug"]` section and an episode entry to reuse it. Both guide pages default to their own language and offer all four audio/video modes. Controls include large play/pause and ten-second skip buttons, native media controls, speed adjustment, fullscreen video and matching-language MP3 download. No autoplay. Media sources attach after user interaction; initial page load requests no MP3/MP4. Switching modes pauses the previous media. The written article and existing SEO remain byte-for-byte unchanged after removing the new component and its two assets.

## Delivery size and hosting

The website media totals approximately 47 MiB: Hindi video 21,132,434 bytes, English video 20,221,613 bytes, Hindi MP3 3,695,112 bytes and English MP3 3,556,106 bytes, plus small poster and captions. All delivery files are below GitHub's 50 MiB warning and 100 MiB single-file block. Both 1080p masters (approximately 86 and 85 MiB) and raw artwork remain outside the site repository. Video copies use 720p, H.264 CRF 28 capped at 1.2 Mbps, 96 kbps AAC and fast-start metadata; MP3 is 128 kbps.

The existing site is about 65 MiB before this addition. This episode fits the [GitHub Pages 1 GB site limit and soft 100 GB/month bandwidth limit](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits). That transfer allowance is shared with the whole site; roughly 5,000 complete plays of one 20 MB video alone would use around 100 GB. This is a budget illustration, not a traffic guarantee. Repeated binary revisions permanently grow Git history, so do not use Git as the archive for full masters or a growing video catalogue. [Repository file limits](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)

For future episodes, prefer owner-approved unlisted YouTube hosting for free video delivery with a click-to-load embed; it supports captions and fullscreen, while MP3 playback/download can remain separate. Internet Archive is an alternative for openly downloadable public media, subject to its terms. External uploads require the owner's account and approval. No external media was uploaded and nothing was published during this task. [YouTube embedding](https://support.google.com/youtube/answer/171780?hl=en) · [Internet Archive uploading](https://help.archive.org/help/uploading-a-basic-guide/)

## Rebuilding and checking

Restore the separate full production workspace, or copy its `assets/`, `audio/` and `source-pack.zip` into this directory. Copy `toolchain.example.json` to `toolchain.local.json` and point it to already available tools. Keep private machine paths out of Git. Production configuration is in `production.json`.

1. Run `scripts/generate_complete_audio.py` using the installed edge-tts package. Cached paragraph audio preserves the approved output; regeneration depends on the online service.
2. Run `scripts/finish_audio.py`, then `scripts/export_complete_subtitles.py`.
3. Keep the approved title PNGs, or rebuild them with `scripts/render_titles.py` and the existing browser/font environment.
4. Run `scripts/render_episode.py hi` and `scripts/render_episode.py en`.
5. Run `scripts/export_complete_video.py`, then `scripts/verify_complete_exports.py`.
6. Inspect every final shot, subtitles and motion, and listen to both complete episodes for approval.
7. Copy only optimized MP4/MP3/VTT and poster delivery files to the website media folder. Run site validation and the player browser checks.
8. Use `scripts/serve_preview.py --directory PATH --port 8771` for a localhost preview with byte-range support. The standard Python simple server lacks the range support needed for representative video seeking tests.

Prepare a draft PR. Preserve the guide text. Publish only after final owner approval.
