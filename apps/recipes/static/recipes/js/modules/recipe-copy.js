export function recipeCopy() {
    const copyBtn = document.getElementById('copyRecipe');
    if (copyBtn) {
        copyBtn.addEventListener('click', () => {
            const recipeTitle = document.querySelector(
                '.recipe-detail__title',
            ).innerText;
            const url = window.location.href;
            const textToCopy = `Confira esta receita incrível: ${recipeTitle}\nLink: ${url}`;

            navigator.clipboard.writeText(textToCopy).then(() => {
                const originalText = copyBtn.innerHTML;
                copyBtn.innerHTML = '<i data-lucide="check"></i> Copiado!';
                setTimeout(() => {
                    copyBtn.innerHTML = originalText;
                    lucide.createIcons();
                }, 2000);
            });
        });
    }
}
