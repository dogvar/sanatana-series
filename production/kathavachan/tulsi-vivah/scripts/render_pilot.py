"""Reusable 2D motion-story renderer, driven by narration paragraph timings."""
from pathlib import Path
import argparse
import json
import math
import subprocess

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps

ROOT=Path(__file__).resolve().parents[1]
TOOLS=json.loads((ROOT/'toolchain.local.json').read_text())
FFMPEG=TOOLS['ffmpeg']
SIZE=(1920,1080)
FPS=24
parser=argparse.ArgumentParser()
parser.add_argument('language',choices=['hi','en'])
parser.add_argument('--frame',type=float,help='Preview a single timestamp')
args=parser.parse_args()
record=json.loads((ROOT/'audio'/'timings.json').read_text())[args.language]
cues=record['cues']
duration=record['duration']
assets=ROOT/'assets'

def source(name):
    return Image.open(assets/name).convert('RGB')

background=source('opening-courtyard.png')
courtyard=source('tulsi-courtyard.webp')
preparation=source('tulsi-preparation.webp')
host=Image.open(assets/'host-open.png').convert('RGBA')
blink=Image.open(assets/'host-blink.png').convert('RGBA')
assert host.size==blink.size
# Only the closed eyelids are used from the alternate drawing.
eye_mask=Image.new('L',host.size,0)
ImageDraw.Draw(eye_mask).ellipse((host.width*.48,host.height*.17,host.width*.70,host.height*.245),fill=255)
eye_mask=eye_mask.filter(ImageFilter.GaussianBlur(8))
host_closed=Image.composite(blink,host,eye_mask)
host=host.resize((640,960),Image.Resampling.LANCZOS)
host_closed=host_closed.resize(host.size,Image.Resampling.LANCZOS)
title=Image.open(assets/f'title-{args.language}.png').convert('RGBA')
first_cut=cues[0]['end']+.25
wedding_cut=cues[2]['start']-.25
prep_cut=cues[3 if args.language=='hi' else 4]['start']-.25
question_cut=cues[4 if args.language=='hi' else 5]['start']-.25
shots=[
    ('host',0,first_cut),
    ('plant',first_cut,wedding_cut),
    ('wedding',wedding_cut,prep_cut),
    ('preparation',prep_cut,question_cut),
    ('question',question_cut,duration),
]

def smooth(value):
    value=max(0,min(1,value))
    return value*value*(3-2*value)

def camera(image, zoom, cx=.5, cy=.5):
    width,height=image.size
    ratio=SIZE[0]/SIZE[1]
    if width/height>ratio:
        crop_h=height/zoom
        crop_w=crop_h*ratio
    else:
        crop_w=width/zoom
        crop_h=crop_w/ratio
    left=max(0,min(width-crop_w,width*cx-crop_w/2))
    top=max(0,min(height-crop_h,height*cy-crop_h/2))
    return image.resize(SIZE,Image.Resampling.BICUBIC,box=(left,top,left+crop_w,top+crop_h)).convert('RGBA')

def environment(frame,t,flame):
    overlay=Image.new('RGBA',SIZE)
    draw=ImageDraw.Draw(overlay)
    # Quiet sunlit motes, with motion independent of camera.
    for index in range(16):
        x=180+(index*117+t*(2+index%3))%1570
        y=130+(index*67-t*(3+index%4))%760
        alpha=int(16+15*(1+math.sin(t*.65+index))/2)
        draw.ellipse((x,y,x+3,y+3),fill=(255,233,180,alpha))
    if flame:
        x,y=flame
        flicker=1+.10*math.sin(t*11)+.055*math.sin(t*17)
        draw.ellipse((x-20,y-12,x+20,y+30),fill=(255,198,70,12))
        draw.ellipse((x-4,y-10*flicker,x+4,y+7),fill=(255,229,129,110))
    return Image.alpha_composite(frame,overlay)

def shot_frame(shot,t):
    kind,start,end=shot
    progress=smooth((t-start)/max(.1,end-start))
    if kind in ('host','question'):
        frame=camera(background,1.025+.015*progress,.5,.5)
        frame=environment(frame,t,(1470,870))
        # Calm breathing and shoulder movement around a fixed lower anchor.
        breath=1+.003*math.sin(t*1.4)
        picture=host_closed if any(abs(t-p)<.065 for p in (2.6,6.8,12.4,18.7,25.4,29.2,33.1,37.0)) else host
        picture=picture.resize((round(640*breath),round(960*breath)),Image.Resampling.BICUBIC)
        x=110+round(3*math.sin(t*.43))
        y=1080-picture.height+round(2*math.sin(t*.7))
        frame.alpha_composite(picture,(x,y))
        if kind=='host':
            opacity=smooth(t/.45)*(1-smooth((t-(end-1.0))/.6))
            if opacity>0:
                layer=title.copy()
                layer.putalpha(layer.getchannel('A').point(lambda a:round(a*opacity)))
                frame.alpha_composite(layer)
        elif t>end-1.7:
            opacity=.8*smooth((t-(end-1.7))/.65)
            layer=title.copy()
            layer.putalpha(layer.getchannel('A').point(lambda a:round(a*opacity)))
            frame.alpha_composite(layer)
        return frame
    if kind=='plant':
        # Approach the ordinary household plant from the wider courtyard.
        frame=camera(background,1.03+.22*progress,.52+.11*progress,.53+.02*progress)
        return environment(frame,t,None)
    if kind=='wedding':
        # Reveal the canopy from the decorated base with a gentle pull back.
        frame=camera(courtyard,1.12-.08*progress,.52,.58-.08*progress)
        return environment(frame,t,(1000,914))
    frame=camera(preparation,1.06,.46+.07*progress,.5)
    return environment(frame,t,None)

def frame_at(t):
    for i,shot in enumerate(shots):
        if t<shot[2] or i==len(shots)-1:
            if i and t<shot[1]+.65:
                mix=smooth((t-shot[1])/.65)
                return Image.blend(shot_frame(shots[i-1],t),shot_frame(shot,t),mix).convert('RGB')
            return shot_frame(shot,t).convert('RGB')

if args.frame is not None:
    path=ROOT/'qa'/f'{args.language}-frame-{args.frame:.1f}.jpg'
    frame_at(args.frame).save(path,quality=92)
    print(path)
else:
    target=ROOT/'renders'/f'tulsi-pilot-{args.language}.mp4'
    command=[FFMPEG,'-y','-hide_banner','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s','1920x1080','-r',str(FPS),'-i','pipe:0','-i',str(ROOT/'audio'/f'pilot-{args.language}.wav'),'-c:v','libx264','-preset','fast','-crf','21','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-af','alimiter=limit=0.891:level=false','-movflags','+faststart','-shortest',str(target)]
    with subprocess.Popen(command,stdin=subprocess.PIPE) as process:
        for index in range(math.ceil(duration*FPS)):
            process.stdin.write(frame_at(index/FPS).tobytes())
            if index%240==0:
                print(args.language,round(index/FPS,1),'seconds rendered',flush=True)
        process.stdin.close()
        if process.wait()!=0:
            raise RuntimeError('FFmpeg render failed')
    print(target,flush=True)
