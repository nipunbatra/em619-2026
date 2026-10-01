const p=require('puppeteer'),fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
(async()=>{const b=await p.launch({headless:true});try{
 const page=await b.newPage(),root=path.resolve(__dirname,'..'),report=[],errors=[];page.on('pageerror',e=>errors.push(String(e)));
 const base=process.env.COURSE_URL||'file://'+root+'/docs/';
 for(const width of [1280,390])for(const color of ['light','dark']){
  await page.setViewport({width,height:900});await page.emulateMediaFeatures([{name:'prefers-color-scheme',value:color}]);
  for(const file of ['index.html','schedule.html','grading.html','faq.html']){
   await page.goto(base+file,{waitUntil:'load'});
   assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,`${file} overflows at ${width}`);
   report.push({file,width,color,overflow:false});
   if(file==='schedule.html'){
    assert.equal(await page.$$eval('.lecture-row',x=>x.length),24);
    assert.equal(await page.$$eval('.resource-cluster.resource-short',x=>x.length),23);
    assert.equal(await page.$$eval('.resource-cluster.resource-summary',x=>x.length),23);
    assert.equal(await page.$$eval('.resource-button.resource-cheat',x=>x.length),29);
    assert.equal(await page.$eval('.library-tools',e=>e.hidden),false);
    await page.screenshot({path:root+`/work/site-${width}-${color}.png`});
    await page.type('#lecture-query','MLP');assert((await page.$$eval('.lecture-row:not([hidden])',x=>x.length))>=1);
    await page.$eval('#lecture-query',e=>{e.value='thishasnomatches';e.dispatchEvent(new Event('input'))});assert.equal(await page.$eval('.library-empty',e=>e.hidden),false);
    await page.click('#lecture-reset');assert.equal(await page.$$eval('.lecture-row:not([hidden])',x=>x.length),24);
    await page.select('#lecture-format','short');assert.equal(await page.$$eval('.lecture-row:not([hidden])',x=>x.length),23);
    await page.select('#lecture-format','summary');assert.equal(await page.$$eval('.lecture-row:not([hidden])',x=>x.length),23);
    await page.select('#lecture-format','recording');assert.equal(await page.$$eval('.lecture-row:not([hidden])',x=>x.length),19);
    await page.click('#lecture-reset');await page.click('[data-module="neural-networks"]');assert.equal(await page.$$eval('.lecture-row:not([hidden])',x=>x.length),6);
    await page.$eval('#lecture-query',e=>{e.value='lecture 22';e.dispatchEvent(new Event('input'))});assert.equal(await page.$eval('.lecture-row:not([hidden])',e=>e.id),'lecture-22');
    await page.click('#lecture-reset');await page.evaluate(()=>{location.hash='lecture-21'});await page.waitForFunction(()=>!document.getElementById('lecture-21').hidden);
    await page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>{document.getElementById('lecture-21').scrollIntoView({behavior:'instant',block:'start'});resolve()})));await page.screenshot({path:root+`/work/site-final-${width}-${color}.png`});
   }
  }
 }
 if(base.startsWith('file:')){
  const html=fs.readFileSync(root+'/docs/schedule.html','utf8'),failures=[];
  for(const m of html.matchAll(/href="([^"#?]+)(?:[?#][^"]*)?"/g)){const u=m[1];if(/^(https?:|mailto:|tel:|data:|\/)/.test(u))continue;if(!fs.existsSync(path.resolve(root,'docs',u)))failures.push(u)}
  assert.deepEqual([...new Set(failures)],[],'Local links must resolve');
 }
 assert.deepEqual(errors,[]);fs.writeFileSync(root+'/work/site-report.json',JSON.stringify(report,null,2));console.log('Passed: four pages, desktop/phone, light/dark, all resource groups, search, filters, empty state and lecture bookmarks.');
}finally{await b.close()}})().catch(e=>{console.error(e);process.exit(1)});
