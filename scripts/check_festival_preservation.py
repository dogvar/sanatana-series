"""Compare a design change to an explicit Git baseline; no third-party dependencies."""
import argparse
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import json
import subprocess

class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.blocks=[]; self.stack=[]; self.all_text=[]; self.links=[]; self.images=[]; self.meta=[]; self.ids=[]
        self.feed(source)
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag in {'p','h1','h2','h3','li','figcaption','summary'}:
            self.stack.append([tag,[]])
        if tag=='a': self.links.append(a.get('href',''))
        if tag=='img': self.images.append((a.get('src',''),a.get('alt','')))
        if tag in {'meta','link','title'}: self.meta.append((tag,tuple(sorted(attrs))))
        if 'id' in a: self.ids.append(a['id'])
    def handle_data(self, text):
        self.all_text.append(text)
        for _, parts in self.stack: parts.append(text)
    def handle_endtag(self, tag):
        if self.stack and self.stack[-1][0]==tag:
            t,parts=self.stack.pop(); self.blocks.append((t,' '.join(''.join(parts).split())))

def git(ref,path):
    return subprocess.check_output(['git','show',f'{ref}:{path}'],text=True)

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--base-ref',required=True,help='Commit containing the content to preserve')
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
report=[]
for name in ['dhanteras.html','dhanteras-hi.html','diwali.html','diwali-hi.html']:
    old=Page(git(args.base_ref,name)); new=Page((root/name).read_text())
    text=' '.join(''.join(new.all_text).split())
    missing=[(tag,t) for tag,t in old.blocks if t and t not in text]
    assert not missing,(name,'Missing original text',missing)
    assert old.meta==new.meta,(name,'Metadata changed')
    for label,a,b in [('links',old.links,new.links),('images and alt text',old.images,new.images),('anchors',old.ids,new.ids)]:
        assert not Counter(a)-Counter(b),(name,label,Counter(a)-Counter(b))
    # Timings, dates and the global-diaspora caveat must remain verbatim.
    import re
    section=lambda s: re.search(r'<section[^>]+id="dates".*?</section>',s,re.S)[0]
    assert section(git(args.base_ref,name))==section((root/name).read_text()),(name,'Date guidance changed')
    report.append({'page':name,'original_text_blocks':len(old.blocks),'original_links':len(old.links),'original_images':len(old.images),'metadata':'unchanged','date_guidance':'unchanged'})
print(json.dumps({'base':args.base_ref,'preserved':report},indent=2))
