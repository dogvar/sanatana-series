from pathlib import Path
import json
from playwright.sync_api import sync_playwright

root=Path(__file__).resolve().parents[1]
tools=json.loads((root/'toolchain.local.json').read_text())
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path=tools['chrome'],headless=True)
    for lang,title,series in [('hi','तुलसी विवाह','सनातन कथावाचन'),('en','Tulsi Vivah','Sanatana Kathavachan')]:
        page=browser.new_page(viewport={'width':1920,'height':1080},device_scale_factor=1)
        page.goto(root.as_uri()+'/approval.html') if (root/'approval.html').exists() else page.goto(root.as_uri()+'/tulsi_pilot/README.md')
        page.set_content(f'''<style>
        @font-face{{font-family:Story;src:url("{(root/'assets/cormorant-garamond-latin.woff2').as_uri()}")}}
        @font-face{{font-family:Hindi;src:url("{(root/'assets/noto-serif-devanagari-devanagari.woff2').as_uri()}")}}
        @font-face{{font-family:Sans;src:url("{(root/'assets/dm-sans-latin.woff2').as_uri()}")}}
        *{{box-sizing:border-box}}body{{margin:0;background:transparent;color:#fff3dd}}
        .box{{position:absolute;right:100px;top:170px;width:800px;padding:52px 54px;background:rgba(19,40,33,.91);border-top:2px solid #d8a141}}
        .series{{font:30px/1.6 {"Hindi" if lang=="hi" else "Sans"};color:#edd2a0;margin:0}}
        h1{{font:500 {"83" if lang=="hi" else "100"}px/1.65 {"Hindi" if lang=="hi" else "Story"};margin:8px 0 0}}
        .url{{font:21px/1.5 Sans;color:#f3dfbf;margin:16px 0 0}}
        </style><div class="box"><p class="series">{series}</p><h1>{title}</h1><p class="url">dogvar.github.io/sanatana-series/tulsi-vivah.html</p></div>''')
        page.evaluate('document.fonts.ready')
        page.screenshot(path=str(root/'assets'/f'title-{lang}.png'),omit_background=True)
        page.close()
    browser.close()
