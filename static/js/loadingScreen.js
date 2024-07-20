document.addEventListener("DOMContentLoaded", function() {
    var loadingScreen = document.getElementById('loading-screen');
    var minDisplayTime = 1000; // Minimum display time in milliseconds
    var startTime;

    function showLoadingScreen() {
        startTime = Date.now();
        loadingScreen.classList.add('visible');
    }

    function hideLoadingScreen() {
        var elapsedTime = Date.now() - startTime;
        var remainingTime = minDisplayTime - elapsedTime;

        if (remainingTime > 0) {
            setTimeout(function() {
                loadingScreen.classList.remove('visible');
            }, remainingTime);
        } else {
            loadingScreen.classList.remove('visible');
        }
    }

    function handleLinkClick(event) {
        var link = event.currentTarget;
        var href = link.getAttribute('href');
        if (href && href !== '#') {
            event.preventDefault();
            showLoadingScreen();
            setTimeout(function() {
                window.location.href = href;
            }, 10); // Minimal delay to ensure loading screen is visible
        }
    }

    // Attach click event to all links
    document.querySelectorAll('a').forEach(function(link) {
        link.addEventListener('click', handleLinkClick);
    });

    // Show loading screen on initial load
    showLoadingScreen();
    window.addEventListener('load', function() {
        hideLoadingScreen();
    });

    // Hide loading screen on back/forward navigation
    window.addEventListener('popstate', function() {
        hideLoadingScreen();
    });
});
