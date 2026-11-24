#!/usr/bin/env python3
"""Dependency-free structural validation for the bilingual festival guide workflow."""
import html.parser
import json
import pathlib
import re
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parents[1]
REFERENCE_DATES = {'dhanteras': '6', 'diwali': '8', 'chhath-puja': '13–16', 'tulsi-vivah': '21'}
CHHATH_DAYS = {'nahay-khay': '13', 'kharna': '14', 'sandhya-arghya': '15', 'usha-arghya': '16'}
errors = []

class Page(html.parser.HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.refs, self.images, self.alternates = path, [], [], [], {}
        self.lang = None
        self.feed(path.read_text(encoding='utf-8'))
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html': self.lang = a.get('lang')
        if 'id' in a: self.ids.append(a['id'])
        for key in ('href', 'src'):
            if key in a: self.refs.append(a[key])
        if tag == 'img': self.images.append(a)
        if tag == 'meta' and a.get('property') == 'og:image':
            prefix = 'https://dogvar.github.io/sanatana-series/'
            if a.get('content', '').startswith(prefix):
                self.refs.append(a['content'][len(prefix):])
        if tag == 'link' and a.get('rel') == 'alternate':
            self.alternates[a.get('hreflang')] = a.get('href')

cache = {}
def parse(path):
    if path not in cache: cache[path] = Page(path)
    return cache[path]

for slug, reference_day in REFERENCE_DATES.items():
    pair = []
    for lang in ('en', 'hi'):
        name = slug + ('-hi' if lang == 'hi' else '') + '.html'
        p = parse(ROOT / name); pair.append(p)
        if p.lang != lang: errors.append(f'{name}: incorrect language')
        if len(p.ids) != len(set(p.ids)): errors.append(f'{name}: duplicate IDs')
        if p.alternates != {'en': slug+'.html', 'hi': slug+'-hi.html'}:
            errors.append(f'{name}: incomplete language alternates')
        for im in p.images:
            if 'alt' not in im or not im.get('width') or not im.get('height'):
                errors.append(f'{name}: missing image accessibility/dimensions')
        for ref in p.refs:
            u = urllib.parse.urlsplit(ref)
            if u.scheme or u.netloc: continue
            target = (p.path.parent / urllib.parse.unquote(u.path)).resolve() if u.path else p.path
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f'{name}: missing local reference {ref}'); continue
            if u.fragment and target.suffix == '.html' and urllib.parse.unquote(u.fragment) not in parse(target).ids:
                errors.append(f'{name}: missing anchor {ref}')
        text = p.path.read_text()
        expected_date = reference_day + (' नवंबर 2026' if lang == 'hi' else ' November 2026')
        if expected_date not in text or 'data-local-panchang' not in text:
            errors.append(f'{name}: missing reference date or local panchang action')
        if 'year=2026' not in text:
            errors.append(f'{name}: missing sourced 2026 reference')
        if slug == 'chhath-puja':
            if 'drikpanchang.com/chhath/chhath-puja-calendar.html' not in text:
                errors.append(f'{name}: missing Chhath calendar source')
            cards = dict(re.findall(r'<li class="chhath-day" id="([a-z-]+)">.*?<time datetime="2026-11-([0-9]{2})"', text, re.S))
            if list(cards.items()) != list(CHHATH_DAYS.items()):
                errors.append(f'{name}: Chhath observance dates or order differ from the calendar')
        elif slug == 'tulsi-vivah':
            dates = re.findall(r'<li><time datetime="2026-11-(\d{2})">', text)
            if dates != ['20', '21', '24']:
                errors.append(f'{name}: Tulsi Vivah date sequence differs from the reference')
            for source in ('1261481', 'nakshtratak.com/en/netherlands/amsterdam/', 'doc226164', 'doc365446', 'doc57337'):
                if source not in text:
                    errors.append(f'{name}: missing source {source}')
            if len(p.images) != 7:
                errors.append(f'{name}: expected seven guide illustrations')
        else:
            if any(term in text for term in ('Amsterdam', 'एम्स्टर्डम', 'Netherlands', 'नीदरलैंड', 'CET')):
                errors.append(f'{name}: unexpected country-specific guide framing')
            if '1261481' not in text:
                errors.append(f'{name}: missing New Delhi reference')
        if re.search(r'TODO|Lorem ipsum|17:11–18:47|17:23–18:59', text):
            errors.append(f'{name}: placeholder or inherited unverified timing')
    if set(pair[0].ids) != set(pair[1].ids): errors.append(f'{slug}: bilingual section mismatch')

# Sikh guide: a gurdwara programme is not a Hindu puja-muhurat lookup.
nanak_pair = []
for lang in ('en', 'hi'):
    name = 'guru-nanak-gurpurab' + ('-hi' if lang == 'hi' else '') + '.html'
    page = parse(ROOT / name); nanak_pair.append(page)
    if page.lang != lang: errors.append(f'{name}: incorrect language')
    if len(page.ids) != len(set(page.ids)): errors.append(f'{name}: duplicate IDs')
    if page.alternates != {'en': 'guru-nanak-gurpurab.html', 'hi': 'guru-nanak-gurpurab-hi.html'}:
        errors.append(f'{name}: incomplete language alternates')
    text = page.path.read_text(encoding='utf-8')
    if 'datetime="2026-11-24"' not in text or '#source-official-date' not in text:
        errors.append(f'{name}: missing reference date or official source')
    for image in page.images:
        if not image.get('alt') or not image.get('width') or not image.get('height'):
            errors.append(f'{name}: missing image description/dimensions')
    for ref in page.refs:
        url = urllib.parse.urlsplit(ref)
        if url.scheme or url.netloc: continue
        target = (page.path.parent / urllib.parse.unquote(url.path)).resolve() if url.path else page.path
        if not target.is_relative_to(ROOT) or not target.exists():
            errors.append(f'{name}: missing local reference {ref}'); continue
        if url.fragment and target.suffix == '.html' and urllib.parse.unquote(url.fragment) not in parse(target).ids:
            errors.append(f'{name}: missing anchor {ref}')
if set(nanak_pair[0].ids) != set(nanak_pair[1].ids):
    errors.append('guru-nanak-gurpurab: bilingual section mismatch')
nanak_css = (ROOT / 'guru-nanak-gurpurab.css').read_text()
for ref in re.findall(r'url\([\'\"]?([^\)\'\"]+)', nanak_css):
    if not urllib.parse.urlsplit(ref).scheme and not (ROOT / ref).is_file():
        errors.append(f'guru-nanak-gurpurab.css: missing {ref}')

# Validate homepage data paths as well as HTML attributes (cards are generated in JS).
for filename in ('index.html', 'calendar.html'):
    text = (ROOT / filename).read_text()
    refs = re.findall(r"(?:h|hi|img):'([^']+)'", text) if filename == 'index.html' else re.findall(r'"href(?:Hi)?": "([^"]+)"', text)
    for ref in refs:
        u = urllib.parse.urlsplit(ref)
        target = ROOT / u.path
        if not target.is_file(): errors.append(f'{filename}: missing data reference {ref}')
        elif u.fragment and u.fragment not in parse(target).ids: errors.append(f'{filename}: missing data anchor {ref}')

# Cross-check the stored Amsterdam dates against the evidence reviewed for this change.
calendar = (ROOT / 'calendar.html').read_text()
highlights = json.loads(re.search(r'const highlights=(\[.*?\]);', calendar, re.S)[1])
expected = {'Dhanteras': '2026-11-06', 'Narak Chaturdashi (Amsterdam)': '2026-11-07',
            'Diwali / Lakshmi Puja': '2026-11-08', 'Govardhan Puja': '2026-11-09',
            'Bhai Dooj (Amsterdam)': '2026-11-10', 'Chhath Puja': '2026-11-15',
            'Devutthana Ekadashi': '2026-11-20', 'Tulasi Vivah': '2026-11-21',
            'Kartik Purnima / Dev Diwali': '2026-11-24'}
for title, date in expected.items():
    matches = [e for e in highlights if e['title'] == title]
    if len(matches) != 1 or matches[0]['date'] != date:
        errors.append(f'calendar.html: date mismatch for {title}')

css = (ROOT / 'festival-guide.css').read_text()
for ref in re.findall(r'url\([\'\"]?([^\)\'\"]+)', css):
    if not urllib.parse.urlsplit(ref).scheme and not (ROOT / ref).is_file(): errors.append(f'festival-guide.css: missing {ref}')

if errors:
    print('\n'.join(errors)); sys.exit(1)
print('PASS: ten guide pages, bilingual sections, anchors, local images, metadata alternates, sourced reference dates, local lookup, Guru Nanak font and homepage/calendar data references')
