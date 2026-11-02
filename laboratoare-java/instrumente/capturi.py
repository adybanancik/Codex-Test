from pathlib import Path
from playwright.sync_api import sync_playwright
import json,html
R=Path(__file__).resolve().parents[1]
r=json.loads((R/'rezultate/teste.json').read_text())
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1100,'height':800},device_scale_factor=1.5)
 for lab,tests in r.items():
  for j,t in enumerate(tests[:3],1):
   inp=t['intrare'];out=t['iesire']
   if lab=='9':
    # Transcrierea completă rămâne disponibilă în rezultatele brute.
    inp=inp if len(inp.splitlines())<14 else '\n'.join(inp.splitlines()[:10])+'\n[… intrarea completă în fișierul TXT …]'
    lines=out.splitlines();out='\n'.join(lines[-19:])
    out='[Ultimele 19 linii din jurnalul real; jurnal integral în TXT]\n'+out
   comanda=f'java -cp clase Lab{int(lab):02}' + (f' rezultate/studenti_caz{j}.tsv' if lab=='9' else '')
   body=f'''<html lang="ro"><meta charset="utf-8"><style>
   body{{margin:0;background:#10202d;color:#e7edf5;font:20px 'DejaVu Sans Mono',monospace}}
   header{{padding:22px;background:#18354b;font:22px sans-serif}}main{{padding:24px}}
   h3{{font:20px sans-serif;color:#7cdcca;margin:10px 0}}pre{{white-space:pre-wrap;overflow-wrap:anywhere;line-height:1.4;margin:10px 0 22px}}
   small{{font:16px sans-serif;color:#b9cbd9}}</style>
   <header>Alexa Adrian · TI-262-21 · Lab {lab} · Varianta 1 · Caz {j}</header>
   <main><small>Captură a jurnalului de execuție Java — date reale, verificate automat</small>
   <h3>Comandă</h3><pre>{comanda}</pre>
   <h3>Intrare standard</h3><pre>{html.escape(inp)}</pre>
   <h3>Ieșire standard</h3><pre>{html.escape(out)}</pre>
   <small>Cod de ieșire: {t['exit']} · Rezultat așteptat verificat: {html.escape(t['asteptat'])}</small></main></html>'''
   page.set_content(body)
   page.screenshot(path=str(R/'capturi'/f'Lab{int(lab):02}_{j}.png'),full_page=True)
 b.close()
print('27 de capturi de ecran salvate.')
