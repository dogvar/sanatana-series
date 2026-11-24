"""Export 1080p subtitled masters and optimized 720p web copies with external VTT."""
from pathlib import Path
import subprocess,json
ROOT=Path(__file__).resolve().parents[1];tools=json.loads((ROOT/'toolchain.local.json').read_text());ff=tools['ffmpeg'];timings=json.loads((ROOT/'audio/timings.json').read_text())
for lang in ('hi','en'):
 src=ROOT/f'renders/picture-{lang}.mp4';out=ROOT/'renders'
 subprocess.run([ff,'-y','-v','warning','-i',str(src),'-i',str(ROOT/'audio'/f'episode-{lang}.wav'),'-map','0:v:0','-map','1:a:0','-vf',f"subtitles='{out/f'tulsi-vivah-{lang}.ass'}':fontsdir='{ROOT/'assets/fonts'}'",'-c:v','libx264','-preset','fast','-crf','21','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-metadata','comment=Music: Bansuri, Sitar and Tabla - Divine Raga for Mindfulness by boopul, Pixabay Content License; adapted under narration.','-movflags','+faststart','-t',str(timings[lang]['duration']),'-shortest',str(out/f'tulsi-vivah-{lang}-1080p.mp4')],check=True)
 subprocess.run([ff,'-y','-v','warning','-i',str(src),'-i',str(ROOT/'audio'/f'episode-{lang}.wav'),'-map','0:v:0','-map','1:a:0','-vf','scale=1280:720:flags=lanczos','-c:v','libx264','-preset','slow','-crf','28','-maxrate','1200k','-bufsize','2400k','-pix_fmt','yuv420p','-c:a','aac','-b:a','96k','-metadata','comment=Music: Bansuri, Sitar and Tabla - Divine Raga for Mindfulness by boopul, Pixabay Content License; adapted under narration.','-movflags','+faststart','-t',str(timings[lang]['duration']),'-shortest',str(out/f'tulsi-vivah-{lang}.mp4')],check=True)
 print(lang,'master and web video exported',flush=True)
