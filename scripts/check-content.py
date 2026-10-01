"""Narrow checks for the worked arithmetic, class resources and preservation of recordings."""
import math,json,re,subprocess,html
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
r=[F(y)-F(3,2)*x-F(1,3) for x,y in [(1,2),(2,3),(3,5)]]
assert r==[F(1,6),F(-1,3),F(1,6)] and sum(x*x for x in r)==F(1,6)
h=-(.75*math.log2(.75)+.25*math.log2(.25));assert abs(1-h-.1887218755)<1e-9
probs=[math.exp(x)/sum(math.exp(t) for t in [2,1,0]) for x in [2,1,0]];assert abs(sum(probs)-1)<1e-12
for x,y in [(0,0),(0,1),(1,0),(1,1)]:assert max(0,x+y)-2*max(0,x+y-1)==(x!=y)
assert 27*4+(5*4)*64+64+64*27+27==3207
assert ((2.01+3)*4-(2+3)*4)-.04<1e-12
s=(ROOT/'schedule.qmd').read_text();old=subprocess.check_output(['git','show','5ef10f6:schedule.qmd'],cwd=ROOT,text=True)
recordings=lambda text:set(re.findall(r'https://iitgnacin-my\.sharepoint\.com/[^)\"<>]+',html.unescape(text)))
assert recordings(old)==recordings(s),'Existing recording URLs must be retained'
assert not re.search(r'\]\(\)',s)
assert 'Wed 23 Sep' in s and 'MLP continued' in s and 'Fri 2 Oct' in s
r=json.loads((ROOT/'resources/lecture-resources.json').read_text())['lectures']
assert len(r)==23 and all(x['sheets'] and x['shorts'] and x['videos'] for x in r)
for row in r:
 for x in row['sheets']:assert (ROOT/x['url']).read_bytes().startswith(b'%PDF')
slides=json.loads((ROOT/'lectures/recap/slide-manifest.json').read_text())
assert len(slides)==49 and sum(s['seconds'] for s in slides)==3300
print(f'Content passed: arithmetic; {len(recordings(s))} preserved recording URLs; 23 matched lecture entries; 49 slides / 55 minutes.')
