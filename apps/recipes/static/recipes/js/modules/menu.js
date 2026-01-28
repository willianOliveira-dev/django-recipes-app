import { refreshLucide } from './lucide.js';

export function initMobileMenu() {
    const menuBtn = document.querySelector('.menu__btn');
    const mobileMenu = document.querySelector('#mobileMenu');
    const body = document.body;

    if (!menuBtn || !mobileMenu) return;

    const renderIcon = (name) => {
        menuBtn.innerHTML = `<i data-lucide="${name}"></i>`;
        refreshLucide();
    };

    renderIcon('menu');

    menuBtn.addEventListener('click', () => {
        const isOpened = mobileMenu.classList.toggle('is-active');

        body.style.overflow = isOpened ? 'hidden' : '';
        menuBtn.setAttribute('aria-expanded', isOpened);

        renderIcon(isOpened ? 'x' : 'menu');
    });
}
