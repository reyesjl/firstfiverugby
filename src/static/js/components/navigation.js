document.addEventListener('DOMContentLoaded', function() {
    var menuToggle = document.getElementById('menuToggle');
    var menuWrapper = document.getElementById('menuWrapper');

    menuToggle.addEventListener('click', function() {
        menuWrapper.classList.toggle('show-menu');
        if (menuWrapper.classList.contains('show-menu')) {
            menuToggle.textContent = 'Close';
            document.body.classList.add('disable-scroll');
        } else {
            menuToggle.textContent = 'Menu';
            document.body.classList.remove('disable-scroll');
        }
    });
});