"""Synthesize an exact prefix of the locked script with an existing local Kokoro model."""
from pathlib import Path
import hashlib
import json
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

ROOT=Path(__file__).resolve().parents[1]
TOOLS=json.loads((ROOT/'toolchain.local.json').read_text())
MODEL=Path(TOOLS['model_dir'])
k=Kokoro(str(MODEL/'kokoro-v1.0.onnx'),str(MODEL/'voices-v1.0.bin'))
all_runs={}
for lang, filename, voice, locale, speed in (
    ('hi','01_Hindi_Script.md','hf_alpha','hi',.94),
    ('en','02_English_Script.md','bf_emma','en-gb',.91),
):
    original=ROOT/'tulsi_pilot'/filename
    full=original.read_text().split('<!-- START -->')[1].split('<!-- END -->')[0].strip()
    paragraphs=full.split('\n\n')[:6]
    (ROOT/'audio'/f'pilot-{lang}-text.txt').write_text('\n\n'.join(paragraphs)+'\n')
    parts=[np.zeros(19200,dtype=np.float32)]
    cues=[]
    cursor=.8
    for index, text in enumerate(paragraphs):
        a,sr=k.create(text,voice=voice,lang=locale,speed=speed)
        assert sr==24000
        sf.write(ROOT/'audio'/f'{lang}-{index+1:02}.wav',a,sr,subtype='PCM_24')
        duration=len(a)/sr
        cues.append(dict(paragraph=index+1,start=cursor,end=cursor+duration,text=text))
        parts.extend([a,np.zeros(12000,dtype=np.float32)])
        cursor+=duration+.5
        print(lang,index+1,round(duration,3),flush=True)
    audio=np.concatenate(parts+[np.zeros(12000,dtype=np.float32)])
    sf.write(ROOT/'audio'/f'pilot-{lang}-raw.wav',audio,sr,subtype='PCM_24')
    all_runs[lang]=dict(voice=voice,locale=locale,speed=speed,sampleRate=sr,duration=len(audio)/sr,cues=cues,
        source=str(original.relative_to(ROOT)),sourceSHA256=hashlib.sha256(original.read_bytes()).hexdigest())
(ROOT/'audio'/'timings.json').write_text(json.dumps(all_runs,ensure_ascii=False,indent=2)+'\n')
print('DONE',[(lang,record['duration']) for lang,record in all_runs.items()],flush=True)
