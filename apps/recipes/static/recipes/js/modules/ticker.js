export function initTicker() {
    const tracks = document.querySelectorAll('.ticker__track');

    window.addEventListener('scroll', () => {
        const y = window.scrollY;

        tracks.forEach((track, index) => {
            const direction = index % 2 === 0 ? 1 : -1;
            const intensity = 0.12;

            track.style.setProperty(
                '--offset',
                `${y * intensity * direction}px`,
            );
        });
    });
}
