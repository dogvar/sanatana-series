# Sanatana Series · Premium Guide Template (v1)

A reusable **static HTML/CSS/JS** article design. Works on GitHub Pages with no server or paid hosting.

## Preview

- `bengali-durga-puja-premium-preview.html`: Bengali Durga Puja, English sample
- `bengali-durga-puja-premium-hi-preview.html`: Hindi sample
- `premium-guide-template.html`: base page to duplicate and adapt for a new guide
- `premium-guide.css`: shared responsive design system
- `premium-guide.js`: reading progress, image viewer, link-sharing
- `images/`: existing article imagery reused from the supplied Bengali guide packages

## To publish this preview

Upload the 3 HTML pages, CSS and JS to the **repository root**; upload all WebP files to the repository `images/` directory. Preview URL becomes `https://dogvar.github.io/sanatana-series/bengali-durga-puja-premium-preview.html`.

**These preview filenames do not overwrite your live Bengali guide or homepage.** Once satisfied, rename/copy the desired preview over the official article file(s), and adjust its alternate-language links accordingly.

## Make a new guide

1. Duplicate `premium-guide-template.html` to `your-guide.html`.
2. Change the `<title>`, metadata, `<h1>`, locale, related links, and article text.
3. Replace the hero and sectional image paths with WebP illustrations. Change alt text accordingly.
4. Add or delete `<section class="panel" id="...">` blocks. Keep section links and IDs synchronized in navigation.
5. Keep HTML, CSS, and JS on GitHub Pages. Use width-appropriate WebP images, `loading="lazy"` for lower images, and make a separate OG preview.

## Built-in behavior

- Responsive 1380px max content area; sidebar on large screens, single-column on tablets and phones
- Real anchors for table of contents and sticky navigation
- Accessible image enlargement (click/Enter, Escape to close)
- Reading-progress bar and native mobile share where supported
- No embedded media player pretending audio exists. Add real, approved recordings later.

## Editorial notes

Content carried forward from the existing Bengali Durga Puja English and Hindi guides in this conversation. Festival dates and ritual timing should be checked against the relevant regional panjika before each annual reuse. Images are visual interpretations, not documentary photographs of a specific artisan or pandal.
