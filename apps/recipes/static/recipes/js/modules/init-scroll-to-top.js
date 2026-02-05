export function initScrollToTop({
    buttonId = 'scrollToTop',
    visibleClass = 'scroll-top--visible',
    showAfter = 400,
} = {}) {
    const scrollBtn = document.getElementById(buttonId);

    if (!scrollBtn) return;

    window.addEventListener('scroll', () => {
        if (window.scrollY > showAfter) {
            scrollBtn.classList.add(visibleClass);
        } else {
            scrollBtn.classList.remove(visibleClass);
        }
    });

    scrollBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth',
        });
    });
}
