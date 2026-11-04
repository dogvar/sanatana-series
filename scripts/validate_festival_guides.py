#!/usr/bin/env python3
"""Dependency-free structural validation for the bilingual festival guide workflow."""
import html.parser
import json
import pathlib
import re
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parents[1]
GUIDES = ['dhanteras', 'diwali']
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

for slug in GUIDES:
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
        if '17:19–18:55' not in text or 'CET (UTC+1)' not in text:
            errors.append(f'{name}: missing verified local Dhanteras window')
        if slug == 'diwali' and '17:11–18:48' not in text:
            errors.append(f'{name}: missing verified Lakshmi Puja window')
        if re.search(r'TODO|Lorem ipsum|17:11–18:47|17:23–18:59', text):
            errors.append(f'{name}: placeholder or inherited unverified timing')
    if set(pair[0].ids) != set(pair[1].ids): errors.append(f'{slug}: bilingual section mismatch')

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
            'Bhai Dooj (Amsterdam)': '2026-11-10'}
for title, date in expected.items():
    matches = [e for e in highlights if e['title'] == title]
    if len(matches) != 1 or matches[0]['date'] != date:
        errors.append(f'calendar.html: date mismatch for {title}')

css = (ROOT / 'festival-guide.css').read_text()
for ref in re.findall(r'url\([\'\"]?([^\)\'\"]+)', css):
    if not urllib.parse.urlsplit(ref).scheme and not (ROOT / ref).is_file(): errors.append(f'festival-guide.css: missing {ref}')

if errors:
    print('\n'.join(errors)); sys.exit(1)
print('PASS: four guide pages, bilingual sections, anchors, local images, metadata alternates, verified windows and homepage/calendar data references')
