export function authForm() {
    const tabLogin = document.getElementById('tab-login');
    const tabRegister = document.getElementById('tab-register');
    const formLogin = document.getElementById('form-login');
    const formRegister = document.getElementById('form-register');
    const subtitle = document.getElementById('auth-subtitle');

    tabRegister.addEventListener('click', () => {
        tabRegister.classList.add('auth__tab--active');
        tabLogin.classList.remove('auth__tab--active');

        formLogin.classList.add('auth__form--hidden');
        formRegister.classList.remove('auth__form--hidden');
        subtitle.innerText = 'Crie sua conta agora!';
    });

    tabLogin.addEventListener('click', () => {
        tabLogin.classList.add('auth__tab--active');
        tabRegister.classList.remove('auth__tab--active');

        formRegister.classList.add('auth__form--hidden');
        formLogin.classList.remove('auth__form--hidden');
        subtitle.innerText = 'Bem-vindo de volta!';
    });
}
