document.addEventListener('DOMContentLoaded', (event) => {
    const themeToggle = document.getElementById('theme-toggle');

    // Apply the saved theme on page load
    const savedTheme = localStorage.getItem('theme') || 'default';
    document.body.classList.add(`${savedTheme}-theme`);
    themeToggle.value = savedTheme;

    themeToggle.addEventListener('change', () => {
        document.body.classList.remove('default-theme', 'cool-blue-theme', 'nature-green-theme', 'forest-theme');
        const selectedTheme = themeToggle.value;
        document.body.classList.add(`${selectedTheme}-theme`);
        // Save the selected theme to localStorage
        localStorage.setItem('theme', selectedTheme);
    });
});
