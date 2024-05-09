document.addEventListener('DOMContentLoaded', function() {
    const sliderWrapper = document.querySelector('.slider-wrapper');
    const sliderLeft = document.querySelector('.slider-left');
    const sliderRight = document.querySelector('.slider-right');

    // Function to scroll the slider left
    sliderLeft.addEventListener('click', function() {
        sliderWrapper.scrollBy({
            left: -300, // Adjust scroll distance as needed
            behavior: 'smooth'
        });
    });

    // Function to scroll the slider right
    sliderRight.addEventListener('click', function() {
        sliderWrapper.scrollBy({
            left: 300, // Adjust scroll distance as needed
            behavior: 'smooth'
        });
    });
});