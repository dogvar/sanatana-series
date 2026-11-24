"""Generate every marked script paragraph using approved voice and pace, with reusable cache."""
import asyncio
from pathlib import Path
import hashlib
import json
import subprocess
import wave
import edge_tts

ROOT=Path(__file__).resolve().parents[1]
TOOLS=json.loads((ROOT/'toolchain.local.json').read_text())
PILOT=ROOT.parent/'tulsi-pilot'
async def generate(language,filename,voice):
    original=ROOT/'tulsi_pilot'/filename
    paragraphs=original.read_text().split('<!-- START -->')[1].split('<!-- END -->')[0].strip().split('\n\n')
    cues=[]
    chunks=[]
    cursor=.8
    for number,text in enumerate(paragraphs,1):
        encoded=ROOT/'audio'/f'{language}-{number:02}.mp3'
        cached=PILOT/'audio'/f'edge-{language}-{number:02}.mp3'
        if cached.exists():
            encoded.write_bytes(cached.read_bytes())
        if not encoded.exists():
            for attempt in range(3):
                try:
                    await edge_tts.Communicate(text,voice,rate='-8%').save(str(encoded))
                    break
                except Exception:
                    encoded.unlink(missing_ok=True)
                    if attempt==2:raise
                    await asyncio.sleep(2)
        wav=ROOT/'audio'/f'{language}-{number:02}.wav'
        subprocess.run([TOOLS['ffmpeg'],'-y','-v','error','-i',str(encoded),'-ar','24000','-ac','1','-c:a','pcm_s16le',str(wav)],check=True)
        with wave.open(str(wav)) as stream:
            frames=stream.readframes(stream.getnframes())
            seconds=stream.getnframes()/24000
        chunks.extend([frames,bytes(24000)])
        cues.append({'paragraph':number,'start':cursor,'end':cursor+seconds,'text':text})
        cursor+=seconds+.5
        print(language,number,len(paragraphs),round(cursor,2),flush=True)
    frames=bytes(38400)+b''.join(chunks)+bytes(96000)
    with wave.open(str(ROOT/'audio'/f'episode-{language}-raw.wav'),'wb') as stream:
        stream.setnchannels(1);stream.setsampwidth(2);stream.setframerate(24000);stream.writeframes(frames)
    return language,dict(voice=voice,locale='hi-IN' if language=='hi' else 'en-IN',rate='-8%',sampleRate=24000,
        duration=len(frames)/48000,cues=cues,source=str(original.relative_to(ROOT)),sourceSHA256=hashlib.sha256(original.read_bytes()).hexdigest(),
        fullText='\n\n'.join(paragraphs),engine='edge-tts')
async def main():
    results=await asyncio.gather(generate('hi','01_Hindi_Script.md','hi-IN-SwaraNeural'),generate('en','02_English_Script.md','en-IN-NeerjaNeural'))
    (ROOT/'audio/timings.json').write_text(json.dumps(dict(results),ensure_ascii=False,indent=2)+'\n')
    print('Complete durations',[(lang,x['duration']) for lang,x in results],flush=True)
asyncio.run(main())
