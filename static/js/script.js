// Custom JS for HackersClub
// Add your custom JavaScript here

document.addEventListener('DOMContentLoaded', function() {
    // Example: Animate cards on scroll (if you want to add more interactivity)
    const animatedCards = document.querySelectorAll('.animate-on-scroll');
    if (animatedCards.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('show');
                }
            });
        }, { threshold: 0.1 });
        animatedCards.forEach(card => observer.observe(card));
    }

    // Example: Focus search input on page load if present
    const searchInput = document.querySelector('.course-search input[type="text"]');
    if (searchInput) {
        searchInput.focus();
    }
});
