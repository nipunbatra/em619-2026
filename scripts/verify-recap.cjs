const puppeteer=require('puppeteer');
const fs=require('node:fs');const path=require('node:path');const assert=require('node:assert/strict');
(async()=>{
 const root=path.resolve(__dirname,'..'),out=path.join(root,'work/recap-review');fs.mkdirSync(out,{recursive:true});
 const browser=await puppeteer.launch({headless:true});
 try{
  const page=await browser.newPage();await page.setViewport({width:1280,height:740});
  const errors=[];page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('file://'+path.join(root,'lectures/recap/index.html')+'?present',{waitUntil:'load'});
  await page.evaluate(()=>document.fonts.ready);
  const n=await page.evaluate(()=>recap.meta.length);assert.equal(n,49);
  const issues=[];
  for(let i=0;i<n;i++){
   await page.evaluate(i=>recap.go(i),i);
   const result=await page.evaluate(()=>{
    const s=document.querySelector('.slide.active'),r=s.getBoundingClientRect(),svg=s.querySelector('svg');
    const boundaries=[...s.querySelectorAll('header,.visual,.idea,.demo')].map(e=>({name:e.className||e.tagName,r:e.getBoundingClientRect()})).filter(o=>o.r.width&&o.r.height).filter(o=>o.r.bottom>r.bottom-15||o.r.right>r.right+1||o.r.left<r.left-1).map(o=>o.name);
    const svgOverflow=[...svg.querySelectorAll('text')].filter(t=>{const b=t.getBBox();return b.x<0||b.x+b.width>1120||b.y<0||b.y+b.height>411}).map(t=>t.textContent);
    const text=[...svg.querySelectorAll('text')];const collisions=[];
    for(let a=0;a<text.length;a++)for(let b=a+1;b<text.length;b++){
     const x=text[a].getBBox(),y=text[b].getBBox();
     if(Math.min(x.x+x.width,y.x+y.width)-Math.max(x.x,y.x)>3 && Math.min(x.y+x.height,y.y+y.height)-Math.max(x.y,y.y)>3)collisions.push([text[a].textContent,text[b].textContent]);
    }
    return {id:s.id,boundaries,svgOverflow,collisions,scroll:s.scrollHeight>s.clientHeight+2};
   });
   if(result.boundaries.length||result.svgOverflow.length||result.collisions.length||result.scroll)issues.push(result);
   await (await page.$('.slide.active')).screenshot({path:path.join(out,String(i+1).padStart(2,'0')+'.png')});
  }
  await page.evaluate(()=>recap.go(22));await page.click('[data-rate="1.1"]');assert((await page.$eval('.slide.active .visual',e=>e.textContent)).includes('-4.80'));
  await page.keyboard.press('a');assert(await page.$eval('#dialog',e=>e.open));await page.keyboard.press('Escape');
  await page.keyboard.press('o');await page.click('[data-go="39"]');await page.click('#gen-next');assert.equal(await page.$eval('#gen-state',e=>e.textContent),'Trace step 2');await page.click('#gen-reset');
  await page.keyboard.press('s');assert(await page.$eval('#dialog',e=>e.open));await page.keyboard.press('Escape');
  await page.evaluate(()=>{document.querySelectorAll('.generation-muted').forEach(e=>e.classList.remove('generation-muted'));recap.go(0);});
  await page.pdf({path:path.join(root,'lectures/recap/em619-course-recap.pdf'),printBackground:true,preferCSSPageSize:true});
  await page.setViewport({width:390,height:844});await page.goto('file://'+path.join(root,'lectures/recap/index.html'));
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
  await page.screenshot({path:path.join(out,'mobile.png')});
  const report={slides:n,minutes:55,issues,browserErrors:errors};fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));
  assert.equal(errors.length,0);assert.equal(issues.length,0,'Slide layout issues require inspection');
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});
