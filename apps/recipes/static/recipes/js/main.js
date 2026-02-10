import { lucideDev } from './modules/lucide.js';
import { AOS } from './modules/aos.js';
import { initMobileMenu } from './modules/menu.js';
import { initFeaturedCarousel } from './modules/featured-carousel.js';
import { recipeCopy } from './modules/recipe-copy.js';
import { recipeRatings } from './modules/recipe-ratings.js';
import { authForm } from './modules/auth-form.js';
import { initCategories } from './modules/categories.js';
import { initTicker } from './modules/ticker.js';
import { initMostViewedCarousel } from './modules/most-viewed-carousel.js';
import { handlePasswordDisplay } from './modules/handle-password-display.js';
import { initScrollToTop } from './modules/init-scroll-to-top.js';

document.addEventListener('DOMContentLoaded', () => {
    lucideDev();
    AOS();
    initMobileMenu();
    initFeaturedCarousel();
    initMostViewedCarousel();
    initTicker();
    initCategories();
    initScrollToTop();
    recipeCopy();
    recipeRatings();
    authForm();
    handlePasswordDisplay();
});
