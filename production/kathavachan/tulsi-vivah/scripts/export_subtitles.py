from pathlib import Path
import json
import textwrap
ROOT=Path(__file__).resolve().parents[1]
timings=json.loads((ROOT/'audio'/'timings.json').read_text())
def stamp(time):
    milliseconds=round(time*1000)
    hours,milliseconds=divmod(milliseconds,3600000)
    minutes,milliseconds=divmod(milliseconds,60000)
    seconds,milliseconds=divmod(milliseconds,1000)
    return f'{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}'
for lang,record in timings.items():
    srt=[]
    vtt=['WEBVTT\n']
    for i,cue in enumerate(record['cues'],1):
        lines=textwrap.wrap(cue['text'],width=56,break_long_words=False,break_on_hyphens=False)
        text='\n'.join(lines)
        start,end=stamp(cue['start']),stamp(cue['end'])
        srt.append(f'{i}\n{start} --> {end}\n{text}\n')
        vtt.append(f'{start.replace(",",".")} --> {end.replace(",",".")}\n{text}\n')
    (ROOT/'renders'/f'tulsi-pilot-{lang}.srt').write_text('\n'.join(srt))
    (ROOT/'renders'/f'tulsi-pilot-{lang}.vtt').write_text('\n'.join(vtt))
print('Exported paragraph-timed SRT and WebVTT for both languages')
