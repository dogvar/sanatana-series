"""Optional free online voice audition using an already installed edge-tts client."""
import asyncio
from pathlib import Path
import json
import hashlib
import subprocess
import wave
import edge_tts

ROOT=Path(__file__).resolve().parents[1]
tools=json.loads((ROOT/'toolchain.local.json').read_text())

async def build(lang,filename,voice):
    source=ROOT/'tulsi_pilot'/filename
    full=source.read_text().split('<!-- START -->')[1].split('<!-- END -->')[0].strip()
    paragraphs=full.split('\n\n')[:5 if lang=='hi' else 6]
    (ROOT/'audio'/f'pilot-{lang}-text.txt').write_text('\n\n'.join(paragraphs)+'\n')
    cues=[]
    cursor=.8
    chunks=[]
    for i,text in enumerate(paragraphs,1):
        mp3=ROOT/'audio'/f'edge-{lang}-{i:02}.mp3'
        await edge_tts.Communicate(text,voice,rate='-8%').save(str(mp3))
        wav=ROOT/'audio'/f'edge-{lang}-{i:02}.wav'
        subprocess.run([tools['ffmpeg'],'-y','-hide_banner','-loglevel','error','-i',str(mp3),'-ar','24000','-ac','1','-c:a','pcm_s16le',str(wav)],check=True)
        with wave.open(str(wav)) as audio:
            data=audio.readframes(audio.getnframes())
            seconds=audio.getnframes()/24000
        cues.append(dict(paragraph=i,start=cursor,end=cursor+seconds,text=text))
        chunks.extend([data,bytes(24000)])
        cursor+=seconds+.5
        print(lang,i,round(seconds,2),flush=True)
    data=bytes(38400)+b''.join(chunks)+bytes(24000)
    path=ROOT/'audio'/f'pilot-{lang}-raw.wav'
    with wave.open(str(path),'wb') as audio:
        audio.setnchannels(1)
        audio.setsampwidth(2)
        audio.setframerate(24000)
        audio.writeframes(data)
    return lang,dict(voice=voice,locale='hi-IN' if lang=='hi' else 'en-IN',rate='-8%',sampleRate=24000,
        duration=len(data)/48000,cues=cues,source=str(source.relative_to(ROOT)),sourceSHA256=hashlib.sha256(source.read_bytes()).hexdigest(),
        engine='edge-tts free online audition')

async def main():
    rows=await asyncio.gather(build('hi','01_Hindi_Script.md','hi-IN-SwaraNeural'),build('en','02_English_Script.md','en-IN-NeerjaNeural'))
    (ROOT/'audio'/'timings.json').write_text(json.dumps(dict(rows),ensure_ascii=False,indent=2)+'\n')
    print([(lang,row['duration']) for lang,row in rows])
asyncio.run(main())
