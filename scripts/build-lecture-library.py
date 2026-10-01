"""Build the dated lecture list from the preserved course record and resource map."""
from pathlib import Path
import json,html,re
ROOT=Path(__file__).resolve().parents[1]
rows=json.loads((ROOT/'resources/class-record.json').read_text())
ICONS={'notes':'book','slides':'easel','cheat':'file-earmark-text','code':'code-square','recording':'camera-video','short':'play-btn','summary':'stopwatch'}
def esc(x):return html.escape(str(x),quote=True)
def icon(kind):return f'<i class="bi bi-{ICONS[kind]}" aria-hidden="true"></i>'
def duration(s):
 m=re.fullmatch(r'PT(?:(\d+)M)?(?:(\d+)S)?',s)
 return f'{int(m[1] or 0)}:{int(m[2] or 0):02}' if m else ''
def link(x,kind,button=False):
 cls='resource-button' if button else 'resource-text-link';dur=duration(x.get('duration',''))
 return f'<a class="{cls} resource-{kind}" href="{esc(x["url"])}" title="{esc(x["title"])}" target="_blank" rel="noopener noreferrer">'+(icon(kind) if button else '')+f'<span class="resource-name">{esc(x["title"])}</span>'+ (f'<span class="resource-duration">{dur}</span>' if dur else '')+'</a>'
def cluster(title,items,kind):
 if not items:return ''
 return f'<div class="resource-cluster resource-{kind}"><h4 class="resource-cluster-title">{icon(kind)} {title}</h4><ul class="resource-links">'+''.join('<li>'+link(x,kind)+'</li>' for x in items)+'</ul></div>'
groups=[('foundations','Foundations',1,3),('trees','Trees and ensembles',4,7),('regression','Regression and optimization',8,13),('classification','Logistic regression',14,17),('neural-networks','Neural networks and autograd',18,23),('recap','Final recap',24,24)]
head='''---
title: "Lectures and revision"
pagetitle: "Lectures and revision · EM 619"
page-layout: full
css: lecture-library.css
---

```{=html}
<div class="library-intro"><p>The class record, with slides, notebooks and videos beside each topic.</p><div class="library-playlists"><a href="https://nipunbatra.github.io/ml-in-1-minute.html"><i class="bi bi-play-btn" aria-hidden="true"></i> All 1-minute Shorts</a><a href="https://www.youtube.com/playlist?list=PLftoLyLEwECCHBep8LyFJ_9LKlabPHmUZ"><i class="bi bi-stopwatch" aria-hidden="true"></i> 3-Minute ML</a><a href="https://nipunbatra.github.io/dl-in-3-minutes.html"><i class="bi bi-stopwatch" aria-hidden="true"></i> 3-Minute DL</a></div></div>
<div class="recap-strip"><div><strong>Final lecture · Friday, 2 October</strong><p>A 55-minute recap of the topics taught.</p></div><div class="recap-actions"><a href="lectures/recap/index.html?present"><i class="bi bi-easel" aria-hidden="true"></i> Present recap</a><a href="lectures/recap/em619-course-recap.pdf"><i class="bi bi-file-earmark-pdf" aria-hidden="true"></i> PDF</a></div></div>
'''
head+='<nav class="lecture-jump" aria-label="Lecture modules"><button type="button" data-module="all" aria-pressed="true" data-active="true" hidden>All lectures</button>'+''.join(f'<a href="#{id}" data-module="{id}">{esc(name)} <span class="jump-range">{str(lo) if lo==hi else str(lo)+"–"+str(hi)}</span></a>' for id,name,lo,hi in groups)+'</nav>'
head+='''<div class="library-tools" hidden><label class="library-search" for="lecture-query"><span>Search lectures and resources</span><span class="library-search-input"><i class="bi bi-search" aria-hidden="true"></i><input type="search" id="lecture-query" placeholder="Topic, date, lecture number or video" autocomplete="off"></span></label><label class="library-format" for="lecture-format"><span>Show lectures with</span><select id="lecture-format"><option value="all">Any resource</option><option value="slides">Slides</option><option value="cheat">Cheatsheets</option><option value="code">Notebooks</option><option value="recording">Class recordings</option><option value="short">1-minute Shorts</option><option value="summary">3-minute videos</option></select></label></div>
<div class="resource-key" aria-label="Resource icon key">'''+''.join(f'<span>{icon(k)} {v}</span>' for k,v in [('slides','Slides'),('cheat','Cheatsheets'),('code','Notebooks'),('recording','Class recordings'),('short','1-minute Shorts'),('summary','3-minute videos')])+'''</div><div class="library-result-row" hidden><p id="lecture-result-count" aria-live="polite"></p><button type="button" id="lecture-reset" hidden>Show all lectures</button></div><div class="lecture-library">'''
body=[]
for gid,name,lo,hi in groups:
 body.append(f'<section class="lecture-section" id="{gid}" aria-labelledby="{gid}-title"><header class="lecture-section-head"><h2 id="{gid}-title">{esc(name)}</h2><span>{("Lecture "+str(lo)) if lo==hi else ("Lectures "+str(lo)+"–"+str(hi))}</span></header><div class="lecture-section-list">')
 for row in rows[lo-1:hi]:
  n=row['number'];types=set(x['type'] for x in row['materials']);types.update(k for k,key in [('cheat','sheets'),('short','shorts'),('summary','videos')] if row[key])
  actions=''.join(link(x,x['type'],True) for x in row['materials'] if x['type']!='recording')
  if row['sheets']:
   for i,s in enumerate(row['sheets']):actions+=link(dict(s,title='Cheatsheet'+(f' {i+1}' if len(row['sheets'])>1 else '')+' · '+s['title']),'cheat',True)
  extras=cluster('Class recording',[x for x in row['materials'] if x['type']=='recording'],'recording')+cluster('3-minute videos',row['videos'],'summary')+cluster('1-minute Shorts',row['shorts'],'short')
  if n==24:extras='<p class="lecture-planned">Slides include worked examples, questions and answers. Use the resources attached to the earlier lectures for revision.</p>'
  body.append(f'<article class="lecture-row" id="lecture-{n}" data-resource-types="{" ".join(sorted(types))}" aria-labelledby="lecture-{n}-title"><div class="lecture-number"><span class="visually-hidden">Lecture </span>{n:02}</div><div class="lecture-body"><div class="lecture-topic-line"><div class="lecture-topic"><h3 id="lecture-{n}-title">{esc(row["title"])}</h3><p class="lecture-date"><time>{esc(row["date"])} 2026</time></p></div><div class="resource-actions" aria-label="Lecture {n} materials">{actions}</div></div><div class="lecture-extras">{extras}</div></div></article>')
 body.append('</div></section>')
end='''</div><div class="library-empty" hidden><p>No lectures match. Try a different topic or clear the filters.</p></div><p class="library-format-note">The 1-minute and 3-minute labels name the video series; episode lengths vary. Cheatsheets and short videos are revision resources and may include extra examples. Class recordings are listed separately.</p>
```

## Course dates

- Classes began on 27 June. The final lecture is on **Friday, 2 October 2026**.
- Examination 1: 10–16 August. Mid-module break: 17–23 August. Classes resumed on 24 August.
- Examination 2: 5–11 October. Make-up exam: 13 October.
- Grade submission: 15 October. Grades disclosed: 16 October.
'''
(ROOT/'schedule.qmd').write_text(head+'\n'.join(body)+end)
print(f'Built {len(rows)} dated lecture entries with visible, labeled resources.')
