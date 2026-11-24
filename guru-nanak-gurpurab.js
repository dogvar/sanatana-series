/* Reveal optional sections reached through a contents/source link or pasted URL. */
(()=>{
  'use strict';
  const reveal=()=>{
    if(!location.hash)return;
    let id;try{id=decodeURIComponent(location.hash.slice(1));}catch{return;}
    const target=document.getElementById(id);if(!target)return;
    let parent=target.closest('details');
    while(parent){parent.open=true;parent=parent.parentElement.closest('details');}
    if(target.id==='timeline')target.querySelector('details').open=true;
  };
  addEventListener('hashchange',reveal);reveal();
})();
