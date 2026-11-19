"""Check actual exported formats, locked narration, levels and rendered review frames."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import zipfile

ROOT=Path(__file__).resolve().parents[1]
tools=json.loads((ROOT/'toolchain.local.json').read_text())
timings=json.loads((ROOT/'audio'/'timings.json').read_text())
report={'date':'2026-11-19','listeningReview':'not performed; human approval required','languages':{}}
with zipfile.ZipFile(ROOT/'source-pack.zip') as archive:
    for member in archive.namelist():
        if member.endswith('.md'):
            assert archive.read(member)==(ROOT/member).read_bytes(),member
for lang,data in timings.items():
    source=ROOT/data['source']
    assert hashlib.sha256(source.read_bytes()).hexdigest()==data['sourceSHA256']
    full=source.read_text().split('<!-- START -->')[1].split('<!-- END -->')[0].strip()
    sampled='\n\n'.join(cue['text'] for cue in data['cues'])
    assert full.startswith(sampled)
    video=ROOT/'renders'/f'tulsi-pilot-{lang}.mp4'
    probe=json.loads(subprocess.check_output([tools['ffprobe'],'-v','quiet','-show_streams','-show_format','-of','json',str(video)]))
    stream=next(s for s in probe['streams'] if s['codec_type']=='video')
    audio=next(s for s in probe['streams'] if s['codec_type']=='audio')
    assert (stream['width'],stream['height'],stream['codec_name'],stream['pix_fmt'],stream['r_frame_rate'])==(1920,1080,'h264','yuv420p','24/1')
    assert audio['codec_name']=='aac'
    duration=float(probe['format']['duration'])
    assert 30<=duration<=45,(lang,duration)
    subprocess.run([tools['ffmpeg'],'-v','error','-i',str(video),'-f','null','-'],check=True)
    measured=subprocess.run([tools['ffmpeg'],'-hide_banner','-i',str(video),'-af','loudnorm=I=-16:TP=-1:LRA=7:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
    levels=json.loads(re.findall(r'\{[^{}]+\}',measured.stderr,re.S)[-1])
    assert -17<=float(levels['input_i'])<=-15
    assert float(levels['input_tp'])<=-1
    for sec in (1.8,2.6,11,21,duration-1):
        subprocess.run([tools['ffmpeg'],'-y','-v','error','-ss',str(sec),'-i',str(video),'-frames:v','1',str(ROOT/'qa'/f'{lang}-frame-{sec:.1f}.jpg')],check=True)
    for cue in data['cues']:
        assert cue['start']<cue['end']<=duration
    report['languages'][lang]={'video':str(video.relative_to(ROOT)),'duration':duration,'bytes':video.stat().st_size,'videoCodec':'h264','resolution':'1920x1080','fps':24,'audioCodec':'aac','LUFS':levels['input_i'],'truePeakDBTP':levels['input_tp'],'lockedNarrationPrefix':'pass','fileDecode':'pass','humanVoiceApproval':'pending'}
(ROOT/'qa'/'final-report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
