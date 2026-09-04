
/* --- table of contents: highlight where you are on the page ------------- */
(function(){
  var toc=document.querySelector('aside.toc');
  if(!toc) return;
  var arts=[].slice.call(document.querySelectorAll('article.entry'));
  if(!arts.length) return;
  var links={};
  [].forEach.call(toc.querySelectorAll('a[href^="#"]'),function(a){
    links[decodeURIComponent(a.getAttribute('href').slice(1))]=a;
  });
  var cur=null;
  function mark(id){
    if(id===cur) return;
    if(cur&&links[cur]) links[cur].classList.remove('on');
    cur=id;
    var a=links[id];
    if(!a) return;
    a.classList.add('on');
    /* keep the active row visible inside the TOC's own scroll box */
    var t=toc.getBoundingClientRect(), r=a.getBoundingClientRect();
    if(r.top<t.top||r.bottom>t.bottom) a.scrollIntoView({block:'nearest'});
  }
  /* the last entry whose top has passed under the sticky header wins */
  function pick(){
    var best=arts[0].id, y=-1e9;
    for(var i=0;i<arts.length;i++){
      var t=arts[i].getBoundingClientRect().top-96;
      if(t<=0 && t>y){ y=t; best=arts[i].id; }
    }
    mark(best);
  }
  var queued=false;
  window.addEventListener('scroll',function(){
    if(queued) return;
    queued=true;
    requestAnimationFrame(function(){ queued=false; pick(); });
  },{passive:true});
  window.addEventListener('resize',pick,{passive:true});
  pick();
})();

/* --- search ------------------------------------------------------------- */
(function(){
  var box=document.getElementById('q'), count=document.getElementById('count'),
      res=document.getElementById('results'), body=document.getElementById('pagebody'),
      toc=document.querySelector('aside.toc'), base=window.BASE||'';
  function esc(s){return s.replace(/[&<>"]/g,function(c){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  function run(){
    var t=(box.value||'').trim().toLowerCase();
    if(!t){ res.style.display='none'; body.style.display=''; count.textContent='';
            if(toc) toc.style.display=''; return; }
    /* results replace the page, so the page's contents list would be lying */
    if(toc) toc.style.display='none';
    /* every word must match, so "kafka ordering" narrows instead of finding nothing */
    var terms=t.split(/\s+/).filter(Boolean);
    var hits=window.IDX.filter(function(r){
      return terms.every(function(w){return r[6].indexOf(w)>-1;});
    });
    res.innerHTML = hits.length
      ? hits.map(function(r){
          return '<a href="'+base+r[1]+'"><span class="rn">'+esc(r[0])+'</span>'
               + '<span class="rm">'+esc(r[2])+' \u00b7 '+esc(r[3])
               + ' \u00b7 for '+esc(r[5])+'</span>'
               + '<span class="ra">'+esc(r[4])+'</span></a>';}).join('')
      : '<p class="none">No diagram type matches every word of that. Try \u201cevent\u201d, '
        + '\u201cfailover\u201d, \u201ctenancy\u201d or \u201clineage\u201d.</p>';
    res.style.display='flex'; body.style.display='none';
    count.textContent = hits.length + (hits.length===1?' match':' matches');
  }
  if(box){ box.addEventListener('input', run); if(box.value) run(); }
  var t;
  function flash(){
    if(location.hash.length<2) return;
    var el=document.getElementById(decodeURIComponent(location.hash.slice(1)));
    if(!el || el.className.indexOf('entry')<0) return;
    clearTimeout(t); el.classList.add('flash');
    t=setTimeout(function(){el.classList.remove('flash');},1600);
  }
  window.addEventListener('hashchange', flash); flash();
})();
