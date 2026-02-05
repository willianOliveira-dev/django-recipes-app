export function initFeaturedCarousel() {
    const items = document.querySelectorAll('.featured__item');
    const dots = document.querySelectorAll('.featured__dot');
    const carousel = document.querySelector('.featured__carousel');
    const [prevBtn, nextBtn] = [
        document.querySelector('.featured__nav--prev'),
        document.querySelector('.featured__nav--next'),
    ];

    if (!items.length || !carousel) return;

    let currentIndex = 0;
    let startX = 0;
    let timer;

    const updateUI = (index) => {
        currentIndex = (index + items.length) % items.length;

        items.forEach((item, i) => {
            const isActive = i === currentIndex;
            item.classList.toggle('featured__item--active', isActive);
            if (dots[i])
                dots[i].classList.toggle('featured__dot--active', isActive);
        });

        startTimer();
    };

    const startTimer = () => {
        clearInterval(timer);
        timer = setInterval(() => updateUI(currentIndex + 1), 10000);
    };

    carousel.addEventListener(
        'touchstart',
        (e) => {
            startX = e.touches[0].clientX;
            clearInterval(timer);
        },
        { passive: true },
    );

    carousel.addEventListener(
        'touchend',
        (e) => {
            const diff = startX - e.changedTouches[0].clientX;
            if (Math.abs(diff) > 70) {
                updateUI(currentIndex + (diff > 0 ? 1 : -1));
            }
        },
        { passive: true },
    );

    nextBtn?.addEventListener('click', () => updateUI(currentIndex + 1));
    prevBtn?.addEventListener('click', () => updateUI(currentIndex - 1));
    dots.forEach((dot, i) => dot.addEventListener('click', () => updateUI(i)));

    startTimer();
}
