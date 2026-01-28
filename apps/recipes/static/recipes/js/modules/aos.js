import Aos from 'https://esm.sh/aos';

export function AOS() {
    Aos.init({
        duration: 800,
        once: true,
        easing: 'ease-in-out',
    });
}
