from pathlib import Path
from playwright.sync_api import sync_playwright
import json
import argparse
import datetime

parser=argparse.ArgumentParser(description="Responsive browser QA for the 2026 festival guides")
parser.add_argument("--base-url",default="http://127.0.0.1:8765/")
parser.add_argument("--chrome",help="Optional path to an installed Chromium/Chrome executable")
parser.add_argument("--output-dir", default="docs", help="Repository-relative report directory")
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
output=root/args.output_dir; output.mkdir(parents=True,exist_ok=True)
shots=output/'screenshots';shots.mkdir(parents=True,exist_ok=True)
report=[]
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path=args.chrome,headless=True)
 for width in [360,390,768,1440]:
  page=browser.new_page(viewport={'width':width,'height':1000},device_scale_factor=1,timezone_id='Europe/Amsterdam')
  page.clock.install(time=datetime.datetime(2026,11,5,12,tzinfo=datetime.timezone.utc))
  errors=[];page.on('pageerror',lambda e: errors.append(str(e)))
  for name in ['dhanteras.html','dhanteras-hi.html','diwali.html','diwali-hi.html','index.html','calendar.html']:
   page.goto(args.base_url.rstrip('/')+'/'+name);page.wait_for_timeout(200)
   page.evaluate('document.querySelectorAll("img").forEach(i=>i.loading="eager")')
   page.wait_for_function('Array.from(document.images).every(i=>i.complete)',timeout=30000)
   info=page.evaluate('''() => ({overflow:document.documentElement.scrollWidth>innerWidth,brokenImages:Array.from(document.images).filter(i=>!i.naturalWidth).map(i=>i.src),background:getComputedStyle(document.body).backgroundColor})''')
   if name=='index.html':
    assert page.locator('a[href="dhanteras.html"]').count()>0
    assert page.locator('a[href="diwali-hi.html"]').count()>0
    page.locator('#filters button').nth(1).click()
    assert page.locator('#sections').inner_text()
   elif name=='calendar.html':
    page.select_option('#city','amsterdam')
    page.locator('#todaybtn').click()
    assert page.locator('#monthtitle').inner_text()=='November 2026'
    assert page.locator('a[href="diwali-hi.html#chapter-5"]').count()==1
    page.locator('#next').click();assert 'December' in page.locator('#monthtitle').inner_text()
    page.locator('#prev').click();assert 'November' in page.locator('#monthtitle').inner_text()
   else:
    assert 'year=2026' in page.locator('[data-local-panchang]').get_attribute('href')
    assert page.locator('#when-title').count()==1
    if page.locator('.toc-disclosure').count():
     assert page.locator('.toc-disclosure').evaluate('(e)=>e.open')==(width>=1050)
     if width<1050:
      page.locator('.toc-disclosure summary').click()
      page.locator('.toc-links a[href="#dates"]').click()
      assert not page.locator('.toc-disclosure').evaluate('(e)=>e.open')
    page.locator('#dates summary').click()
    assert page.locator('#dates details').get_attribute('open') is not None
    other=name.replace('-hi','') if '-hi' in name else name.replace('.html','-hi.html')
    page.locator('nav.nav a[href="'+other+'"]').click();assert page.url.endswith(other)
    page.goto(args.base_url.rstrip('/')+'/'+name)
    page.keyboard.press('Tab');assert page.locator('.skip').evaluate('(e)=>e===document.activeElement')
    page.keyboard.press('Enter');assert page.url.endswith('#content')
   report.append({'page':name,'width':width,**info,'jsErrors':errors[:]})
   if width in [390,1440]:
    page.goto(args.base_url.rstrip('/')+'/'+name);page.evaluate('document.fonts.ready');page.wait_for_timeout(300)
    page.screenshot(path=str(shots/(name.replace('.html','')+'-'+str(width)+'.png')),full_page=False)
  page.close()
 browser.close()
(output/'browser-check-2026.json').write_text(json.dumps(report,indent=2))
print(f'Checked {len(report)} page/viewport combinations; report: {output}/browser-check-2026.json')
assert not any(r['overflow'] or r['brokenImages'] or r['jsErrors'] for r in report)
