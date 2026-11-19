"""Measure real exports and verify exact complete narration/captions, not just prefixes."""
from pathlib import Path
import hashlib,json,re,subprocess,zipfile
ROOT=Path(__file__).resolve().parents[1];tools=json.loads((ROOT/'toolchain.local.json').read_text());timings=json.loads((ROOT/'audio/timings.json').read_text());captions=json.loads((ROOT/'audio/caption-cues.json').read_text())
report={'date':'2026-11-19','pilotApproval':'Both voices, narrator and storytelling approved by owner','fullEpisodeListening':'Owner final review pending; assistant audio listening unavailable','languages':{}}
with zipfile.ZipFile(ROOT/'source-pack.zip') as archive:
 for n in archive.namelist():
  if n.endswith('.md'):assert archive.read(n)==(ROOT/n).read_bytes(),n
for lang,data in timings.items():
 source=ROOT/data['source'];assert hashlib.sha256(source.read_bytes()).hexdigest()==data['sourceSHA256']
 full=source.read_text().split('<!-- START -->')[1].split('<!-- END -->')[0].strip()
 assert full=='\n\n'.join(c['text'] for c in data['cues'])
 assert ' '.join(full.split())==' '.join(c['text'] for c in captions[lang])
 previous=0
 for c in captions[lang]:
  assert previous<=c['start']<c['end']<=data['duration'];previous=c['end']
 exports=[]
 for suffix,resolution in [('-1080p.mp4',(1920,1080)),('.mp4',(1280,720)),('.mp3',None)]:
  path=ROOT/'renders'/f'tulsi-vivah-{lang}{suffix}'
  probe=json.loads(subprocess.check_output([tools['ffprobe'],'-v','quiet','-show_streams','-show_format','-of','json',str(path)]))
  duration=float(probe['format']['duration']);assert abs(duration-data['duration'])<.2
  if resolution:
   stream=next(x for x in probe['streams'] if x['codec_type']=='video');assert (stream['width'],stream['height'])==resolution;assert stream['codec_name']=='h264' and stream['r_frame_rate']=='24/1';assert next(x for x in probe['streams'] if x['codec_type']=='audio')['codec_name']=='aac'
  subprocess.run([tools['ffmpeg'],'-v','error','-i',str(path),'-f','null','-'],check=True)
  measured=subprocess.run([tools['ffmpeg'],'-hide_banner','-i',str(path),'-af','loudnorm=I=-16:TP=-1:LRA=7:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
  levels=json.loads(re.findall(r'\{[^{}]+\}',measured.stderr,re.S)[-1]);assert -17<=float(levels['input_i'])<=-15;assert float(levels['input_tp'])<=-1,(path,levels)
  exports.append({'file':path.name,'seconds':duration,'bytes':path.stat().st_size,'resolution':resolution,'integratedLUFS':levels['input_i'],'truePeakDBTP':levels['input_tp'],'decode':'pass','sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
 shots=json.loads((ROOT/'qa'/f'shots-{lang}.json').read_text())
 for i,(kind,start,end) in enumerate(shots):
  second=(start+end)/2
  subprocess.run([tools['ffmpeg'],'-y','-v','error','-ss',str(second),'-i',str(ROOT/'renders'/f'tulsi-vivah-{lang}-1080p.mp4'),'-frames:v','1',str(ROOT/'qa'/f'{lang}-scene-{i:02}-{kind}.jpg')],check=True)
 report['languages'][lang]={'exactCompleteScript':'pass','paragraphs':len(data['cues']),'subtitleCues':len(captions[lang]),'subtitleWordCoverage':'pass','sceneCount':len(shots),'exports':exports}
(ROOT/'qa/complete-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
