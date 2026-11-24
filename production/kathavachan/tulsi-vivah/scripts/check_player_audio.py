from playwright.sync_api import sync_playwright
from pathlib import Path
import json,argparse
parser=argparse.ArgumentParser();parser.add_argument('--base-url',default='http://127.0.0.1:8771/');parser.add_argument('--cdp-url',default='http://127.0.0.1:9333');args=parser.parse_args()
out=Path(__file__).resolve().parents[1]/'qa';records=[]
with sync_playwright() as p:
 browser=p.chromium.connect_over_cdp(args.cdp_url,timeout=15000)
 for width in (390,1440):
  for name in ('tulsi-vivah','tulsi-vivah-hi'):
   page=browser.new_page(viewport={'width':width,'height':1000});errors=[];requests=[]
   page.on('pageerror',lambda e:errors.append(str(e)));page.on('request',lambda r:requests.append(r.url))
   page.goto(args.base_url.rstrip('/')+'/'+name+'.html');page.evaluate('document.fonts.ready');page.wait_for_timeout(800)
   print(name,width,flush=True)
   assert not any(x.endswith(('.mp3','.mp4')) for x in requests),requests
   assert page.locator('audio').evaluate('(e)=>e.paused && e.preload==="none" && !e.autoplay')
   assert page.locator('[data-format]').count()==4
   assert page.locator('[data-format][aria-pressed="true"]').get_attribute('data-language')==('hi' if name.endswith('-hi') else 'en')
   assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
   page.locator('.kathavachan').scroll_into_view_if_needed();page.screenshot(path=str(out/f'player-{name}-{width}.png'))
   page.locator('audio').evaluate('(e)=>e.muted=true');page.locator('[data-play]').click();page.wait_for_function('document.querySelector("audio").currentTime>0',timeout=20000)
   page.locator('select').last.select_option('1.25');assert page.locator('audio').evaluate('(e)=>e.playbackRate')==1.25
   page.locator('[data-play]').click();assert page.locator('audio').evaluate('(e)=>e.paused')
   for lang in ('hi','en'):
    print('switch',lang,flush=True)
    page.locator(f'[data-format="audio"][data-language="{lang}"]').click();page.locator('audio').evaluate('(e)=>e.muted=true');page.locator('[data-play]').click();page.wait_for_timeout(1500);print(page.locator('audio').evaluate('(e)=>({src:e.src,paused:e.paused,time:e.currentTime,ready:e.readyState,error:e.error?.message})'),page.locator('.katha-status').inner_text(),flush=True);page.wait_for_function('document.querySelector("audio").currentTime>0',timeout=20000);page.locator('[data-play]').click()
   records.append({'page':name,'width':width,'noAutoplay':True,'noInitialMediaDownload':True,'bothAudioLanguages':True,'speed':True,'overflow':False,'errors':errors})
   assert not errors;page.close()
 browser.close()
(out/'player-preview-check.json').write_text(json.dumps(records,indent=2));print(json.dumps(records,indent=2))
