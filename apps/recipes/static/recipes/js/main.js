import { authForm } from './modules/auth-form.js';
import { handlePasswordDisplay } from './modules/handle-password-display.js';
import { initMobileMenu } from './modules/menu.js';
import { AOS } from './modules/aos.js';
import { lucideDev } from './modules/lucide.js';
import { initFeaturedCarousel } from './modules/carousel.js';

document.addEventListener('DOMContentLoaded', () => {
    lucideDev();
    AOS();
    initFeaturedCarousel();
    initMobileMenu();
    authForm();
    handlePasswordDisplay();
});
