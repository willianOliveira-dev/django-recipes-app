export function recipeRatings() {
    const stars = document.querySelectorAll('.star-placeholder');
    stars.forEach((star, index) => {
        star.addEventListener('mouseover', () => {
            stars.forEach((s, i) =>
                i <= index
                    ? (s.style.fill = '#ffa000')
                    : (s.style.fill = 'none'),
            );
        });
        star.addEventListener('click', () => {
            alert(`Você selecionou ${index + 1} estrelas!`);
            // Aqui enviar para o Service
        });
    });
}
