"""Clean approved speech plus quiet licensed bansuri/sitar/tabla, with phrase ducking."""
from pathlib import Path
import json,re,subprocess,hashlib
import numpy as np
import soundfile as sf
ROOT=Path(__file__).resolve().parents[1];TOOLS=json.loads((ROOT/'toolchain.local.json').read_text());ff=TOOLS['ffmpeg'];timings=json.loads((ROOT/'audio/timings.json').read_text());source=ROOT/'music/divine-raga-boopul.mp3'
CREDIT='Music: Bansuri, Sitar & Tabla - Divine Raga for Mindfulness by boopul, Pixabay Content License. Adapted with fades and narration ducking.'
def measure(path):
 result=subprocess.run([ff,'-hide_banner','-i',str(path),'-af','loudnorm=I=-16:TP=-2:LRA=7:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
 return json.loads(re.findall(r'\{[^{}]+\}',result.stderr,re.S)[-1])
def normalize(src,dest,target=-16):
 values=measure(src)
 filt=f"loudnorm=I={target}:TP=-2:LRA=7:measured_I={values['input_i']}:measured_TP={values['input_tp']}:measured_LRA={values['input_lra']}:measured_thresh={values['input_thresh']}:offset={values['target_offset']}:linear=true"
 subprocess.run([ff,'-y','-v','error','-i',str(src),'-af',filt,'-ar','24000','-c:a','pcm_s24le',str(dest)],check=True)
 return values
subprocess.run([ff,'-y','-v','error','-i',str(source),'-af','highpass=f=70,lowpass=f=9000','-ar','24000','-ac','2','-c:a','pcm_s24le',str(ROOT/'audio/music-source.wav')],check=True)
music,sr=sf.read(ROOT/'audio/music-source.wav',dtype='float32');music_levels=measure(ROOT/'audio/music-source.wav');gain=10**((-32-float(music_levels['input_i']))/20);music*=gain
# Seamless four-second overlap only if the narration extends beyond the source.
overlap=4*sr;a=np.linspace(0,1,overlap,dtype='float32')[:,None];joined=np.concatenate((music[:-overlap],music[-overlap:]*(1-a)+music[:overlap]*a,music[overlap:]))
reports={}
for lang,data in timings.items():
 normalize(ROOT/'audio'/f'episode-{lang}-raw.wav',ROOT/'audio'/f'voice-clean-{lang}.wav',target=-17)
 voice,sr=sf.read(ROOT/'audio'/f'voice-clean-{lang}.wav',dtype='float32');n=len(voice);t=np.arange(n)/sr;bed=joined[:n].copy()
 control=np.zeros(int(np.ceil(data['duration']*100))+120,dtype='float32')
 for cue in data['cues']:control[max(0,round((cue['start']-.12)*100)):round((cue['end']+.2)*100)]=1
 control=np.convolve(control,np.ones(60)/60,mode='same');control=np.interp(t,np.arange(len(control))/100,control)
 duck=10**((-4*control)/20);fade=np.clip(np.minimum(t/1.5,(data['duration']-t)/3),0,1)
 bed*=duck[:,None]*fade[:,None];sf.write(ROOT/'audio'/f'score-{lang}.wav',bed,sr,subtype='PCM_24')
 mix=voice[:,None]+bed;sf.write(ROOT/'audio'/f'mix-{lang}.wav',mix,sr,subtype='PCM_24')
 reports[lang]=normalize(ROOT/'audio'/f'mix-{lang}.wav',ROOT/'audio'/f'episode-{lang}.wav')
 subprocess.run([ff,'-y','-v','error','-i',str(ROOT/'audio'/f'episode-{lang}.wav'),'-c:a','libmp3lame','-b:a','128k','-metadata','title=Tulsi Vivah - '+('Hindi' if lang=='hi' else 'English'),'-metadata','artist=Sanatana Kathavachan','-metadata','comment='+CREDIT,str(ROOT/'renders'/f'tulsi-vivah-{lang}.mp3')],check=True)
 subprocess.run([ff,'-y','-v','error','-i',str(ROOT/'renders'/f'tulsi-vivah-{lang}.mp3'),'-t','35','-c:a','copy',str(ROOT/'qa'/f'music-revision-{lang}-35s.mp3')],check=True)
 print(lang,'instrumental remix complete',flush=True)
report={'music':{'title':'Bansuri, Sitar & Tabla – Divine Raga for Mindfulness','artist':'boopul','source':'https://pixabay.com/music/meditationspiritual-bansuri-sitar-amp-tabla-divine-raga-for-mindfulness-538679/','license':'https://pixabay.com/service/license-summary/','sourceSHA256':hashlib.sha256(source.read_bytes()).hexdigest(),'publisherLabelsAIGenerated':True,'sourceSeconds':len(music)/sr,'musicBaseLUFS':-32,'speechDuckingDB':-4,'seamOverlapSeconds':4,'fadeInSeconds':1.5,'fadeOutSeconds':3},'narration':'Exact approved raw speech, one centred signal in stereo; no delay, echo, reverb or time stretching. Per-paragraph source files unchanged.','rejectedScore':'Original synthetic three-tone bed removed completely.','mix':reports}
(ROOT/'qa/audio-mastering.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print('Both complete instrumental remixes mastered')
