import { refreshLucide } from './lucide.js';

export function handlePasswordDisplay() {
    const passwordToggleButtons = document.querySelectorAll(
        '.auth__button-password-display',
    );

    passwordToggleButtons.forEach((toggleBtn) => {
        let isPasswordVisible = false;

        toggleBtn.addEventListener('click', () => {
            isPasswordVisible = !isPasswordVisible;

            const iconName = isPasswordVisible ? 'eye' : 'eye-closed';

            toggleBtn.innerHTML = `<i data-lucide="${iconName}" class="auth__icon-password"></i>`;
            refreshLucide();

            const passwordInput =
                toggleBtn.parentElement.querySelector('input');

            if (passwordInput) {
                passwordInput.setAttribute(
                    'type',
                    isPasswordVisible ? 'text' : 'password',
                );
            }
        });
    });
}
