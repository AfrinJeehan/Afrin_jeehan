(function () {
  'use strict';

  /* ── Theme Toggle ── */
  const root = document.documentElement;
  const toggle = document.getElementById('theme-toggle');
  const sunIcon = document.getElementById('icon-sun');
  const moonIcon = document.getElementById('icon-moon');

  function syncIcons() {
    if (!sunIcon || !moonIcon) return;
    const dark = root.classList.contains('dark');
    sunIcon.classList.toggle('hidden', !dark);
    moonIcon.classList.toggle('hidden', dark);
  }

  if (toggle) {
    syncIcons();
    toggle.addEventListener('click', () => {
      root.classList.toggle('dark');
      localStorage.setItem('color-theme', root.classList.contains('dark') ? 'dark' : 'light');
      syncIcons();
    });
  }

  /* ── Mobile Menu ── */
  const mobileMenu = document.getElementById('mobile-menu');
  const menuBtn = document.getElementById('mobile-menu-btn');

  if (mobileMenu && menuBtn) {
    menuBtn.addEventListener('click', () => {
      const open = mobileMenu.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', String(open));
    });
    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
        menuBtn.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ── Smooth Scroll for hash links ── */
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

  /* ── Active nav highlight ── */
  const sections = Array.from(document.querySelectorAll('section[id]'));
  const navLinks = Array.from(document.querySelectorAll('.nav-link'));

  if (sections.length && navLinks.length) {
    const obs = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        const id = entry.target.getAttribute('id');
        navLinks.forEach(link => {
          const h = link.getAttribute('href')?.split('#')[1];
          link.classList.toggle('active', h === id);
        });
      });
    }, { threshold: 0.35 });
    sections.forEach(s => obs.observe(s));
  }

  /* ── Scroll Reveal ── */
  const revealItems = document.querySelectorAll('.reveal, .reveal-left, .reveal-scale');
  if (revealItems.length) {
    const revealObs = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.08 });
    revealItems.forEach(el => revealObs.observe(el));
  }

  /* ── Typing Effect ── */
  const typingEl = document.getElementById('typing-text');
  if (typingEl) {
    const phrases = [
      'Business Analysis',
      'Data-Driven Strategy',
      'Stakeholder-Centered Design',
      'Process Optimization',
      'AI & Machine Learning'
    ];
    let phraseIdx = 0;
    let charIdx = 0;
    let deleting = false;
    const typeSpeed = 70;
    const deleteSpeed = 40;
    const pauseEnd = 2000;
    const pauseStart = 500;

    function tick() {
      const current = phrases[phraseIdx];
      if (!deleting) {
        typingEl.textContent = current.substring(0, charIdx + 1);
        charIdx++;
        if (charIdx === current.length) {
          deleting = true;
          setTimeout(tick, pauseEnd);
          return;
        }
      } else {
        typingEl.textContent = current.substring(0, charIdx - 1);
        charIdx--;
        if (charIdx === 0) {
          deleting = false;
          phraseIdx = (phraseIdx + 1) % phrases.length;
          setTimeout(tick, pauseStart);
          return;
        }
      }
      setTimeout(tick, deleting ? deleteSpeed : typeSpeed);
    }
    setTimeout(tick, 1000);
  }

  /* ── Counter Animation ── */
  const counters = document.querySelectorAll('[data-count]');
  if (counters.length) {
    const countObs = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        const target = el.getAttribute('data-count');
        const suffix = el.getAttribute('data-suffix') || '';
        const numTarget = parseInt(target, 10);
        const duration = 1800;
        const start = performance.now();

        function step(now) {
          const progress = Math.min((now - start) / duration, 1);
          const ease = 1 - Math.pow(1 - progress, 3); // easeOutCubic
          el.textContent = Math.floor(ease * numTarget) + suffix;
          if (progress < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
        observer.unobserve(el);
      });
    }, { threshold: 0.5 });
    counters.forEach(c => countObs.observe(c));
  }

  /* ── Stagger reveal children ── */
  document.querySelectorAll('.stagger').forEach(parent => {
    Array.from(parent.children).forEach((child, i) => {
      child.style.setProperty('--i', i);
    });
  });

})();
