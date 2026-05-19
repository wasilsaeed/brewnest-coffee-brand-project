document.addEventListener("DOMContentLoaded", () => {
    const navToggle = document.querySelector(".nav-toggle");
    const navLinks = document.querySelector(".nav-links");

    if (!navToggle || !navLinks) {
        console.warn("Navigation elements not found.");
        return;
    }

    navToggle.addEventListener("click", () => {
        navLinks.classList.toggle("is-open");
        navToggle.classList.toggle("is-active");
    });
});