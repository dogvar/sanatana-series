from playwright.sync_api import sync_playwright
from pathlib import Path
import json,argparse
parser=argparse.ArgumentParser();parser.add_argument('--base-url',default='http://127.0.0.1:8771/');parser.add_argument('--cdp-url',default='http://127.0.0.1:9333');args=parser.parse_args()
out=Path(__file__).resolve().parents[1]/'qa';report=[]
with sync_playwright() as p:
 browser=p.chromium.connect_over_cdp(args.cdp_url,timeout=15000)
 for width in (390,1440):
  for name in ('tulsi-vivah','tulsi-vivah-hi'):
   page=browser.new_page(viewport={'width':width,'height':1000});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
   page.goto(args.base_url.rstrip('/')+'/'+name+'.html');page.evaluate('document.fonts.ready')
   for lang in ('hi','en'):
    page.locator(f'[data-format="video"][data-language="{lang}"]').click()
    assert page.locator('audio').evaluate('(e)=>e.paused && e.hidden')
    page.locator('video').evaluate('(e)=>e.muted=true')
    page.locator('[data-play]').click();page.wait_for_function('document.querySelector("video").currentTime>0',timeout=25000)
    page.wait_for_function('document.querySelector("video").textTracks.length===1 && document.querySelector("video").textTracks[0].cues?.length>0',timeout=20000)
    assert page.locator('video').evaluate('(e)=>e.textTracks[0].language')==lang
    page.locator('video').evaluate('(e)=>e.currentTime=100');page.wait_for_function('document.querySelector("video").currentTime>=100',timeout=15000)
    page.locator('[data-play]').click();assert page.locator('video').evaluate('(e)=>e.paused')
    page.locator('[data-seek="-10"]').click();assert page.locator('video').evaluate('(e)=>e.currentTime')<100
    page.locator('[data-seek="10"]').click();assert page.locator('video').evaluate('(e)=>e.currentTime')>=100
    page.locator('select').last.select_option('1.5');assert page.locator('video').evaluate('(e)=>e.playbackRate')==1.5
    page.locator('[data-fullscreen]').click();page.wait_for_function('!!document.fullscreenElement',timeout=10000);page.evaluate('document.exitFullscreen()')
    page.locator('.kathavachan').scroll_into_view_if_needed();page.screenshot(path=str(out/f'video-player-{name}-{width}-{lang}.png'))
    page.locator(f'[data-format="audio"][data-language="{lang}"]').click();assert page.locator('video').evaluate('(e)=>e.paused && e.hidden')
    assert page.locator('[data-download]').get_attribute('href').endswith(f'{lang}.mp3')
   assert not errors
   assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
   report.append({'page':name,'width':width,'bothVideoLanguages':True,'captionsLoaded':True,'seek':True,'speed':True,'fullscreen':True,'audioSwitchPausesVideo':True,'downloadLanguage':True,'jsErrors':errors,'browserAudioMutedForDeviceIsolation':True});page.close()
 browser.close()
(out/'player-video-check.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
