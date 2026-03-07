(function () {
  'use strict';

  /* ── Mobile Menu ── */
  const mobileMenu = document.getElementById('mobile-menu');
  const menuBtn = document.getElementById('mobile-menu-btn');

  if (mobileMenu && menuBtn) {
    menuBtn.addEventListener('click', () => {
      const open = mobileMenu.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', String(open));
      const icon = menuBtn.querySelector('i');
      if (icon) {
        icon.className = open ? 'fas fa-times' : 'fas fa-bars';
      }
    });

    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
        menuBtn.setAttribute('aria-expanded', 'false');
        const icon = menuBtn.querySelector('i');
        if (icon) icon.className = 'fas fa-bars';
      });
    });
  }

  /* ── Smooth Scroll ── */
  document.querySelectorAll('a[href*="#"]').forEach(anchor => {
    anchor.addEventListener('click', e => {
      const href = anchor.getAttribute('href');
      if (!href || !href.includes('#')) return;
      const hash = href.slice(href.indexOf('#'));
      const target = document.querySelector(hash);
      if (!target) return;
      if (href.startsWith('#') || href.includes(window.location.pathname)) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        history.replaceState(null, '', hash);
      }
    });
  });

})();
