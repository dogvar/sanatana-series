# Sanatana Kathavachan · Tulsi Vivah approval pilot

The supplied seven-file pack is preserved in tulsi_pilot/. All seven files were read. The spoken scripts remain exactly as supplied.

## Current milestone

The principal samples use the opening five Hindi paragraphs and opening six English paragraphs, ending at complete editorial paragraph boundaries. The Hindi sample runs approximately 43 seconds and English approximately 45 seconds. The local approval page is approval.html. The renders directory holds the two videos, MP3 audio and optional subtitles. The character sheet and reusable host layers are in assets/.

The host is a recurring adult Indian woman in a terracotta sari with an emerald edge. The same face, clothing and palette are used in the turnaround sheet, transparent host and blinking pose. The opening courtyard is new artwork. The wedding courtyard and preparation views reuse the approved Tulsi Vivah guide artwork. The animation uses independent host movement, blinks, a small lamp flicker, drifting sunlight motes, a close approach to the household plant, a canopy reveal, a lateral preparation view and crossfades. It uses no continuous lip sync.

## Voices and tools

- The selected review voices are hi-IN-SwaraNeural and en-IN-NeerjaNeural at -8% rate. An already installed edge-tts 7.3.1 client generated the auditions through the free online speech endpoint. This requires network access, but no paid API, API key or voice cloning was used. The endpoint and voice access can change. The client’s software license is distinct from the service’s terms, so public voice distribution rights require confirmation before publishing complete episodes. [edge-tts project](https://github.com/rany2/edge-tts)
- An already installed Kokoro ONNX model produced local Hindi hf_alpha/hf_beta and English bf_emma/af_heart auditions. The Kokoro model card identifies Apache-2.0 licensing. The tested local version remains in auditions/kokoro/. Hindi ASR raised pronunciation concerns. These alternatives are retained for voice review. [Kokoro model](https://huggingface.co/hexgrad/Kokoro-82M) · [Voice catalogue](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md)
- macOS System Voices were inventoried but not selected for publishable media. Apple’s license restricts public sharing of the system voices. [Apple license](https://www.apple.com.cn/legal/sla/docs/macOS27.pdf)
- Existing FFmpeg, Pillow, NumPy, Playwright/Chrome and speech packages were reused. No packages or large models were installed. ImageGen’s built-in tool supplied the character sheet, opening scene and transparent poses. The prompt set is in asset-manifest.json. No paid voice, video or music API was called.
- Narration is clean, with no added music. Both language audio masters target -16 LUFS and -1.5 dBTP before the video encode. Measured final exports are recorded in qa/final-report.json.

## Script and source checks

Devi Bhagavata Purana 9.23 confirms the Brahmin disguise, transfer of the protective kavacha and Shiva’s final attack. Chapter 9.24 confirms Tulasi’s reception of the disguised Vishnu, her discovery and protest, the stone curse, Gandaki, the plant and Vishnu’s stone form. The voice sample ends before these later events.

Two points remain for full-script editorial review. Kavacha is translated in the checked edition as a protective amulet at the neck, so the storyboard should avoid depicting a speculative full suit of armour. The locked scripts compress the deception into a visit and Tulasi’s reception of Vishnu. The primary account explicitly includes intimacy obtained through the disguise. The source notes preserve that distinction for editorial consideration, and the supplied narration has not been rewritten.

Sources were rechecked on 19 November 2026. [Book 9, chapter 23](https://www.wisdomlib.org/hinduism/book/devi-bhagavata-purana/d/doc57336.html) · [Book 9, chapter 24](https://www.wisdomlib.org/hinduism/book/devi-bhagavata-purana/d/doc57337.html)

## Rebuilding

Copy toolchain.example.json to toolchain.local.json and fill in paths to existing tools and models. The current machine’s paths are already in the local file. Use the matching installed Python environment. The sample scripts read exact text from the START/END markers and record input SHA256 values.

1. Run scripts/generate_edge_pilot.py with the installed edge-tts package available on PYTHONPATH, or choose scripts/generate_pilot_audio.py for the Kokoro alternative.
2. Run scripts/master_audio.py and scripts/export_subtitles.py.
3. Run scripts/render_titles.py with the installed Playwright environment. The supplied fonts support Devanagari shaping through Chrome.
4. Run scripts/render_pilot.py hi and scripts/render_pilot.py en.
5. Run scripts/verify_exports.py and inspect the exported frames, audio and caption timing.
6. Serve this directory with python3 -m http.server 8768 --bind 127.0.0.1 and open approval.html.

The optional SRT/WebVTT cues follow paragraph-level measured synthesis boundaries. They are review captions, and dense paragraphs need finer subtitle segmentation before a final public release.

## Following approval

Voice and character approval precede complete narration. Then produce each full supplied script at its natural duration and check the remaining sacred names against the pronunciation auditions. Prepare separate MP3s and optional polished subtitles.

The website component belongs near the beginning of both guide pages and should use large labelled controls, independent language selection, playback speeds, fullscreen video, optional captions and downloads, no autoplay and lazy media loading. Episode media and URLs should come from a small manifest. No live page has been modified for this pilot.

For long-term video hosting, an unlisted YouTube upload and click-to-load embed is the first free option to consider. Internet Archive is another free option for public downloadable MP3/MP4 media, subject to its terms and the chosen publication rights. Both require the owner’s account and approval before upload. Keep manifests, small posters, transcripts and production code in Git, while keeping large render files outside the Pages repository. GitHub Pages has a 1 GB published-site cap and a soft 100 GB monthly bandwidth limit. [GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) · [YouTube embedding](https://support.google.com/youtube/answer/171780?hl=en) · [Internet Archive uploading](https://help.archive.org/help/uploading-a-basic-guide/)

## Review limitations

Visual frames and file metadata can be checked here. The environment does not supply audio listening input to the assistant. Automated transcription is an imperfect aid and did not reliably distinguish Hindi phonetic errors from ASR errors. Human listening approval is still required for naturalness and sacred-name pronunciation. Use the separate pronunciation-hi.mp3 and pronunciation-en.mp3 auditions when deciding on the final voices.
