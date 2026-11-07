/* Small progressive enhancements; the complete article works without JavaScript. */
(()=>{
 'use strict';
 const contents=document.querySelector('.toc-disclosure');
 const desktop=matchMedia('(min-width: 1050px)');
 const adapt=()=>{if(contents)contents.open=desktop.matches;};
 adapt();desktop.addEventListener('change',adapt);
 if(contents)contents.addEventListener('click',e=>{
  if(e.target.closest('a')&&!desktop.matches)contents.open=false;
 });
 const links=[...document.querySelectorAll('.toc-links a')];
 const chapters=[...document.querySelectorAll('main>section[id]')];
 if('IntersectionObserver' in window){
  const observer=new IntersectionObserver(entries=>{
   for(const entry of entries){if(!entry.isIntersecting)continue;
    for(const link of links){const active=link.hash==='#'+entry.target.id;
     link.classList.toggle('is-current',active);
     if(active)link.setAttribute('aria-current','location');else link.removeAttribute('aria-current');
    }
   }
  },{rootMargin:'-12% 0px -72% 0px',threshold:0});
  chapters.forEach(section=>observer.observe(section));
 }
})();
