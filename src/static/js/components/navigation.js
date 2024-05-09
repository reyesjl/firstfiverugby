document.addEventListener('DOMContentLoaded', function() {
    // Get references to the navmenu and menulink elements
    const navmenu = document.querySelector('.navmenu');
    const menulink = document.querySelector('.menulink');
    const body = document.querySelector('body');

    // Add click event listener to menulink
    menulink.addEventListener('click', function() {
        if (menulink.textContent === 'Menu') {
            menulink.textContent = 'Close';
        } else {
            menulink.textContent = 'Menu';
        }
        menulink.classList.toggle('is-red');
        navmenu.classList.toggle('show');
        body.classList.toggle('body-scroll-lock');
    });
});