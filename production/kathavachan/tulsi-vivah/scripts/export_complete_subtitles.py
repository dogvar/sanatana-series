"""Exact-word, short two-line captions, timed within measured speech paragraphs."""
from pathlib import Path
import json,textwrap,math
ROOT=Path(__file__).resolve().parents[1]
def stamp(t,ass=False):
 ms=round(t*(100 if ass else 1000));h,ms=divmod(ms,(360000 if ass else 3600000));m,ms=divmod(ms,6000 if ass else 60000);s,ms=divmod(ms,100 if ass else 1000)
 return f'{h}:{m:02}:{s:02}.{ms:02}' if ass else f'{h:02}:{m:02}:{s:02},{ms:03}'
records=json.loads((ROOT/'audio/timings.json').read_text()); result={}
for lang,r in records.items():
 cues=[]
 for p in r['cues']:
  words=p['text'].split(); chunks=[];current=[]
  for w in words:
   trial=' '.join(current+[w]);lines=textwrap.wrap(trial,width=42,break_long_words=False,break_on_hyphens=False)
   if current and (len(lines)>2 or len(current)>=12):chunks.append(current);current=[w]
   else:current.append(w)
  if current:chunks.append(current)
  weights=[sum(len(w)+1 for w in c) for c in chunks];total=sum(weights);offset=0
  for chunk,weight in zip(chunks,weights):
   start=p['start']+(p['end']-p['start'])*offset/total;offset+=weight;end=p['start']+(p['end']-p['start'])*offset/total
   cues.append({'start':start,'end':end,'text':' '.join(chunk),'paragraph':p['paragraph']})
 assert ' '.join(c['text'] for c in cues)==' '.join(r['fullText'].split())
 srt=[];vtt=['WEBVTT\n'];ass=['[Script Info]','ScriptType: v4.00+','PlayResX: 1920','PlayResY: 1080','WrapStyle: 2','ScaledBorderAndShadow: yes','','[V4+ Styles]','Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding',f'Style: Default,{"Noto Serif Devanagari" if lang=="hi" else "Arial"},46,&H00FFFFFF,&H00FFFFFF,&H00191512,&H50191512,0,0,0,0,100,100,0,0,3,10,0,2,100,100,52,1','','[Events]','Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text']
 for i,c in enumerate(cues,1):
  lines='\n'.join(textwrap.wrap(c['text'],width=42,break_long_words=False,break_on_hyphens=False));a,b=stamp(c['start']),stamp(c['end']);srt.append(f'{i}\n{a} --> {b}\n{lines}\n');vtt.append(f'{a.replace(",",".")} --> {b.replace(",",".")}\n{lines}\n');ass.append('Dialogue: 0,'+stamp(c['start'],True)+','+stamp(c['end'],True)+',Default,,0,0,0,,'+lines.replace('\n',r'\N'))
 for ext,content in [('srt','\n'.join(srt)),('vtt','\n'.join(vtt)),('ass','\n'.join(ass))]:(ROOT/f'renders/tulsi-vivah-{lang}.{ext}').write_text(content)
 result[lang]=cues
(ROOT/'audio/caption-cues.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print({k:len(v) for k,v in result.items()})
