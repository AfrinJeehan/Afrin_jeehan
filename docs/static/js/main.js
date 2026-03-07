/* ══════════════════════════════════════════════════════
   AFRIN JEEHAN — Dynamic Portfolio JS
   Scroll reveals, stagger animations, mobile menu
   ══════════════════════════════════════════════════════ */

(function () {
  'use strict';

  /* ── Mobile Menu ── */
  const toggle = document.getElementById('mobile-toggle');
  const menu = document.getElementById('mobile-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', () => {
      menu.classList.toggle('open');
      const icon = toggle.querySelector('i');
      if (icon) {
        icon.classList.toggle('fa-bars');
        icon.classList.toggle('fa-times');
      }
    });
    // Close on link click
    menu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        menu.classList.remove('open');
        const icon = toggle.querySelector('i');
        if (icon) { icon.classList.add('fa-bars'); icon.classList.remove('fa-times'); }
      });
    });
  }

  /* ── Smooth Scroll ── */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', e => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    });
  });

  /* ── Scroll Reveal (IntersectionObserver) ── */
  const revealEls = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .stagger');

  if ('IntersectionObserver' in window && revealEls.length) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );

    revealEls.forEach(el => observer.observe(el));
  } else {
    // Fallback: show everything
    revealEls.forEach(el => el.classList.add('visible'));
  }

  /* ── Counter Animation for Stat Numbers ── */
  const statEls = document.querySelectorAll('.stat-number[data-target]');

  if ('IntersectionObserver' in window && statEls.length) {
    const counterObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            animateCounter(entry.target);
            counterObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.3 }
    );

    statEls.forEach(el => counterObserver.observe(el));
  }

  function animateCounter(el) {
    const target = parseInt(el.getAttribute('data-target'), 10);
    const suffix = el.getAttribute('data-suffix') || '';
    const prefix = el.getAttribute('data-prefix') || '';
    const duration = 1200;
    const start = performance.now();

    function step(now) {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
      const current = Math.round(target * eased);
      el.textContent = prefix + current + suffix;
      if (progress < 1) requestAnimationFrame(step);
    }

    requestAnimationFrame(step);
  }

  /* ── Active Nav Highlight ── */
  const homeHref = document.querySelector('a.logo')?.getAttribute('href') || '/';
  const currentPath = window.location.pathname;
  document.querySelectorAll('.nav-link, .mobile-link').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath ||
        href === currentPath.replace(/\/$/, '') ||
        href + '/' === currentPath ||
        (currentPath.startsWith(href) && href !== homeHref)) {
      link.classList.add('active');
    }
  });

})();
