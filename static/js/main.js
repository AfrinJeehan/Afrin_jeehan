(function () {
    const root = document.documentElement;
    const themeToggle = document.getElementById('theme-toggle');
    const sunIcon = document.getElementById('theme-icon-sun');
    const moonIcon = document.getElementById('theme-icon-moon');

    function syncThemeIcons() {
        if (!sunIcon || !moonIcon) return;
        const isDark = root.classList.contains('dark');
        sunIcon.classList.toggle('hidden', !isDark);
        moonIcon.classList.toggle('hidden', isDark);
    }

    if (themeToggle) {
        syncThemeIcons();
        themeToggle.addEventListener('click', () => {
            root.classList.toggle('dark');
            const currentTheme = root.classList.contains('dark') ? 'dark' : 'light';
            localStorage.setItem('color-theme', currentTheme);
            syncThemeIcons();
        });
    }

    const mobileMenu = document.getElementById('mobile-menu');
    const mobileMenuToggle = document.getElementById('mobile-menu-toggle');

    if (mobileMenu && mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', () => {
            const isOpen = !mobileMenu.classList.contains('hidden');
            mobileMenu.classList.toggle('hidden', isOpen);
            mobileMenuToggle.setAttribute('aria-expanded', String(!isOpen));
        });

        mobileMenu.querySelectorAll('a').forEach((link) => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('hidden');
                mobileMenuToggle.setAttribute('aria-expanded', 'false');
            });
        });
    }

    document.querySelectorAll('a[href*="#"]').forEach((anchor) => {
        anchor.addEventListener('click', (event) => {
            const href = anchor.getAttribute('href');
            if (!href || !href.includes('#')) return;
            const hash = href.slice(href.indexOf('#'));
            const target = document.querySelector(hash);
            if (!target) return;

            if (href.startsWith('#') || href.includes(window.location.pathname)) {
                event.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                history.replaceState(null, '', hash);
            }
        });
    });

    const sections = Array.from(document.querySelectorAll('section[id]'));
    const navLinks = Array.from(document.querySelectorAll('.nav-link'));

    if (sections.length && navLinks.length) {
        const activeObserver = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (!entry.isIntersecting) return;
                    const activeId = entry.target.getAttribute('id');
                    navLinks.forEach((link) => {
                        const targetHash = link.getAttribute('href')?.split('#')[1];
                        link.classList.toggle('active', targetHash === activeId);
                    });
                });
            },
            { threshold: 0.45 }
        );

        sections.forEach((section) => activeObserver.observe(section));
    }

    const revealItems = document.querySelectorAll('.reveal');
    if (revealItems.length) {
        const revealObserver = new IntersectionObserver(
            (entries, observer) => {
                entries.forEach((entry) => {
                    if (!entry.isIntersecting) return;
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                });
            },
            { threshold: 0.12 }
        );

        revealItems.forEach((item) => revealObserver.observe(item));
    }
})();
