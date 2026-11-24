from pathlib import Path
import json
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]
TOOLS=json.loads((ROOT/'toolchain.local.json').read_text())
FFMPEG=TOOLS['ffmpeg']
records={}
for lang in ('hi','en'):
    source=ROOT/'audio'/f'pilot-{lang}-raw.wav'
    report=subprocess.run([FFMPEG,'-hide_banner','-i',str(source),'-af','loudnorm=I=-16:TP=-1.5:LRA=7:print_format=json','-f','null','-'],capture_output=True,text=True,check=True).stderr
    measured=json.loads(re.findall(r'\{[^{}]+\}',report,re.S)[-1])
    values=dict(zip(('I','TP','LRA','thresh','offset'),(measured[k] for k in ('input_i','input_tp','input_lra','input_thresh','target_offset'))))
    filt=f"loudnorm=I=-16:TP=-1.5:LRA=7:measured_I={values['I']}:measured_TP={values['TP']}:measured_LRA={values['LRA']}:measured_thresh={values['thresh']}:offset={values['offset']}:linear=true:print_format=json"
    wav=ROOT/'audio'/f'pilot-{lang}.wav'
    subprocess.run([FFMPEG,'-y','-hide_banner','-loglevel','error','-i',str(source),'-af',filt,'-ar','48000','-c:a','pcm_s24le',str(wav)],check=True)
    subprocess.run([FFMPEG,'-y','-hide_banner','-loglevel','error','-i',str(wav),'-c:a','libmp3lame','-b:a','160k',str(ROOT/'renders'/f'tulsi-pilot-{lang}.mp3')],check=True)
    records[lang]=dict(firstPass=measured)
(ROOT/'qa'/'audio-mastering.json').write_text(json.dumps(records,indent=2)+'\n')
print('Mastered both languages to -16 LUFS target')
