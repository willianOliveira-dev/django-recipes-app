export function initMostViewedCarousel() {
    const carousel = document.querySelector('.most-viewed__carousel');
    const wrapper = document.querySelector('.most-viewed__wrapper');
    const items = [...document.querySelectorAll('.most-viewed .recipe-card')];
    const dotsContainer = document.querySelector('.most-viewed__dots');
    const prevBtn = document.querySelector('.most-viewed__nav--prev');
    const nextBtn = document.querySelector('.most-viewed__nav--next');

    if (!wrapper || !items.length) return;

    let currentPage = 0;
    let startX = 0;
    let timer;

    const isMobile = () => window.innerWidth < 768;
    const itemsPerPage = () => (isMobile() ? 1 : 3);
    const totalPages = () => Math.ceil(items.length / itemsPerPage());

    const getItemWidth = () => {
        const gap = parseFloat(getComputedStyle(wrapper).gap) || 0;
        return items[0].offsetWidth + gap;
    };

    const renderDots = () => {
        if (!dotsContainer) return;

        dotsContainer.innerHTML = '';

        for (let i = 0; i < totalPages(); i++) {
            const dot = document.createElement('span');
            dot.className = 'most-viewed__dot';
            if (i === currentPage)
                dot.classList.add('most-viewed__dot--active');

            dot.addEventListener('click', () => updateUI(i));
            dotsContainer.appendChild(dot);
        }
    };

    const updateUI = (page) => {
        const total = totalPages();
        currentPage = ((page % total) + total) % total;

        const translateX = -currentPage * itemsPerPage() * getItemWidth();
        wrapper.style.transform = `translateX(${translateX}px)`;
        wrapper.style.transition =
            'transform 0.8s cubic-bezier(0.4, 0, 0.2, 1)';

        items.forEach((item, index) => {
            item.classList.remove('recipe-card--active');

            const start = currentPage * itemsPerPage();
            const centerIndex = isMobile() ? start : start + 1;

            if (index === centerIndex) {
                item.classList.add('recipe-card--active');
            }
        });

        renderDots();
        startTimer();
    };

    const startTimer = () => {
        clearInterval(timer);
        timer = setInterval(() => updateUI(currentPage + 1), 10000);
    };

    carousel.addEventListener(
        'touchstart',
        (e) => {
            startX = e.touches[0].clientX;
            clearInterval(timer);
            wrapper.style.transition = 'none';
        },
        { passive: true },
    );

    carousel.addEventListener(
        'touchend',
        (e) => {
            const diff = startX - e.changedTouches[0].clientX;
            if (Math.abs(diff) > 70) {
                updateUI(currentPage + (diff > 0 ? 1 : -1));
            } else {
                updateUI(currentPage);
            }
        },
        { passive: true },
    );

    nextBtn?.addEventListener('click', () => updateUI(currentPage + 1));
    prevBtn?.addEventListener('click', () => updateUI(currentPage - 1));

    window.addEventListener('resize', () => updateUI(0));

    updateUI(0);
}
