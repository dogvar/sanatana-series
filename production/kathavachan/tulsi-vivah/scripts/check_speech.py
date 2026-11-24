from pathlib import Path
import json
from faster_whisper import WhisperModel
import soundfile as sf
from scipy.signal import resample_poly
root=Path(__file__).resolve().parents[1]
tools=json.loads((root/'toolchain.local.json').read_text())
model=WhisperModel(tools['whisper_model'],device='cpu',compute_type='int8',cpu_threads=4)
records={}
for language in ('hi','en'):
    samples, sr = sf.read(root/'audio'/f'pilot-{language}-raw.wav', dtype='float32')
    samples = resample_poly(samples, 16000, sr).astype('float32')
    segments,info=model.transcribe(samples,language=language,beam_size=5,condition_on_previous_text=False)
    records[language]=[{'start':s.start,'end':s.end,'text':s.text} for s in segments]
    print(language,json.dumps(records[language],ensure_ascii=False),flush=True)
(root/'qa'/'speech-transcription.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
