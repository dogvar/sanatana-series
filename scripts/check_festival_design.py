from pathlib import Path
from playwright.sync_api import sync_playwright
import json
import argparse
parser=argparse.ArgumentParser(description='Check narrow reflow, no-JS reading and local fonts')
parser.add_argument('--chrome',help='Optional installed Chrome executable')
parser.add_argument('--base-url',default='http://127.0.0.1:8765/')
args=parser.parse_args()
r=Path(__file__).resolve().parents[1];report=[]
base=args.base_url.rstrip('/')+'/'
with sync_playwright() as p:
 b=p.chromium.launch(executable_path=args.chrome,headless=True)
 for js in [True,False]:
  ctx=b.new_context(java_script_enabled=js,viewport={'width':320 if js else 390,'height':900},reduced_motion='reduce')
  external=[]
  def route(req):
   if not req.request.url.startswith(base):
    external.append(req.request.url);req.abort()
   else:req.continue_()
  ctx.route('**/*',route)
  for name in ['dhanteras','dhanteras-hi','diwali','diwali-hi']:
   pg=ctx.new_page();bad=[];pg.on('response',lambda response:bad.append(response.url) if response.status>=400 else None)
   pg.goto(base+name+'.html');pg.evaluate('document.fonts.ready')
   assert pg.evaluate('getComputedStyle(document.documentElement).getPropertyValue("--night").trim()')=='#101722'
   assert pg.locator('.chapter-index').evaluate_all('(items)=>items.every(e=>e.getBoundingClientRect().height<75)'),(name,'Wrapped chapter number')
   assert pg.evaluate('document.documentElement.scrollWidth<=innerWidth'),(name,js,'overflow')
   if not js:
    assert pg.locator('.toc-disclosure').get_attribute('open') is not None
    assert pg.locator('.toc-links a').first.is_visible()
   else:
    assert pg.evaluate('getComputedStyle(document.documentElement).scrollBehavior')=='auto'
   assert not bad,(name,bad)
   report.append({'page':name,'javascript':js,'width':320 if js else 390,'overflow':False,'reducedMotion':'pass','localAssets':'pass','noJsContents':'pass' if not js else 'n/a'})
   pg.close()
  assert not external,external
  ctx.close()
 b.close()
(r/'docs/redesign/progressive-enhancement-check.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS: 320px reflow, reduced motion, local-only assets and no-JavaScript reading/contents')
