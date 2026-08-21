
(function(){
  var MQ = window.matchMedia('(max-width: 768px)');
  var logoHidden = false;
  var leftPct = 32;
  var dragging = false;
  var moved = false;
  var startX = 0;
  var startPct = 32;
  var bar = null;
  var TAP_PX = 10;
  var MIN_PCT = 0;
  var MAX_PCT = 42;

  function isMobile(){ return MQ.matches; }
  function clamp(v, a, b){ return Math.max(a, Math.min(b, v)); }

  function popupLeftFor(pct, hidden){
    if (hidden) return 12;
    var t = pct / MAX_PCT;
    return Math.round(48 + t * 68);
  }

  function syncFormPopups(leftPx){
    var pr = document.querySelector('.panel-right');
    if (!pr) return;
    var nodes = pr.querySelectorAll('div');
    for (var i = 0; i < nodes.length; i++){
      var el = nodes[i];
      var st = el.style;
      if (!st) continue;
      // absolute form panel (token id / admin lock)
      if (st.position === 'absolute' && (st.left === '116px' || st.left === '116' || el.dataset.lnrtPopup === '1' ||
          (parseFloat(st.left) >= 90 && parseFloat(st.left) <= 130 && st.right === '0px'))){
        el.dataset.lnrtPopup = '1';
        st.left = leftPx + 'px';
        st.right = '0px';
      }
      // balloon helper padding that was locked to 116px
      if (st.paddingLeft === '116px' || el.dataset.lnrtPad === '1'){
        el.dataset.lnrtPad = '1';
        st.paddingLeft = leftPx + 'px';
      }
    }
  }

  function apply(){
    var root = document.documentElement;
    if (!isMobile()){
      root.classList.remove('lnrt-logo-hidden');
      root.style.removeProperty('--lnrt-left-w');
      root.style.removeProperty('--lnrt-popup-left');
      root.style.removeProperty('--lnrt-popup-right');
      root.style.removeProperty('--lnrt-gap-w');
      syncFormPopups(116);
      return;
    }
    var leftPx;
    if (logoHidden){
      root.classList.add('lnrt-logo-hidden');
      root.style.setProperty('--lnrt-left-w', '0%');
      leftPx = 12;
      root.style.setProperty('--lnrt-popup-left', leftPx + 'px');
      root.style.setProperty('--lnrt-popup-right', '0px');
    } else {
      root.classList.remove('lnrt-logo-hidden');
      root.style.setProperty('--lnrt-left-w', leftPct + '%');
      leftPx = popupLeftFor(leftPct, false);
      root.style.setProperty('--lnrt-popup-left', leftPx + 'px');
      root.style.setProperty('--lnrt-popup-right', '0px');
    }
    syncFormPopups(leftPx);
  }

  function findBar(){ return document.querySelector('.gap-mid'); }

  function clientX(e){
    if (e.touches && e.touches[0]) return e.touches[0].clientX;
    if (e.changedTouches && e.changedTouches[0]) return e.changedTouches[0].clientX;
    return e.clientX;
  }

  function onDown(e){
    if (!isMobile()) return;
    bar = findBar();
    if (!bar) return;
    var t = e.target;
    if (!(t === bar || bar.contains(t))) return;
    dragging = true;
    moved = false;
    startX = clientX(e);
    startPct = logoHidden ? 0 : leftPct;
    bar.classList.add('is-dragging');
    var pl = document.querySelector('.panel-left');
    if (pl) pl.style.transition = 'none';
    bar.style.transition = 'none';
    if (e.cancelable) e.preventDefault();
  }

  function onMove(e){
    if (!dragging) return;
    var x = clientX(e);
    var dx = x - startX;
    if (Math.abs(dx) > TAP_PX) moved = true;
    var panels = document.querySelector('.panels');
    var pw = panels ? panels.clientWidth : window.innerWidth;
    var deltaPct = (dx / pw) * 100;
    var next = clamp(startPct + deltaPct, MIN_PCT, MAX_PCT);
    if (logoHidden && moved) logoHidden = false;
    leftPct = next;
    if (leftPct <= 1) leftPct = 0;
    apply();
    if (e.cancelable) e.preventDefault();
  }

  function onUp(){
    if (!dragging) return;
    dragging = false;
    if (bar) bar.classList.remove('is-dragging');
    var pl = document.querySelector('.panel-left');
    if (pl) pl.style.transition = '';
    if (bar) bar.style.transition = '';

    if (!moved){
      logoHidden = !logoHidden;
      if (!logoHidden && leftPct < 12) leftPct = 28;
    } else {
      if (leftPct < 6){ logoHidden = true; leftPct = 0; }
      else logoHidden = false;
    }
    apply();
  }

  function bind(){
    document.addEventListener('touchstart', onDown, { passive: false });
    document.addEventListener('touchmove', onMove, { passive: false });
    document.addEventListener('touchend', onUp, { passive: true });
    document.addEventListener('touchcancel', onUp, { passive: true });
    document.addEventListener('mousedown', function(e){ if (isMobile()) onDown(e); });
    document.addEventListener('mousemove', function(e){ if (dragging) onMove(e); });
    document.addEventListener('mouseup', onUp);
    apply();
    // keep token popup sized when React toggles guest/admin panels
    try {
      var obs = new MutationObserver(function(){ if (isMobile()) apply(); });
      obs.observe(document.body, { childList: true, subtree: true, attributes: true, attributeFilter: ['style', 'class'] });
    } catch (err) {}
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', bind);
  else bind();

  var tries = 0;
  var boot = setInterval(function(){
    tries++;
    if (findBar() || tries > 40){ clearInterval(boot); apply(); }
  }, 250);

  if (MQ.addEventListener) MQ.addEventListener('change', function(){ apply(); });
  else if (MQ.addListener) MQ.addListener(function(){ apply(); });
})();


