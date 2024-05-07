document.addEventListener("DOMContentLoaded", function() {
    // Get references to the left and right arrow icons
    var leftArrow = document.getElementById("leftArrow");
    var rightArrow = document.getElementById("rightArrow");
    var images = document.querySelectorAll(".carousel img");
    
    // Initialize current index
    var currentIndex = 0;

    // Add click event listeners to the left and right arrow icons
    leftArrow.addEventListener("click", function() {
        navigateCarousel("left");
    });
    
    rightArrow.addEventListener("click", function() {
        navigateCarousel("right");
    });

    // Function to navigate the carousel based on the direction
    function navigateCarousel(direction) {
        // Hide the current image
        images[currentIndex].classList.remove("show");

        // Update the current index based on the direction
        if (direction === "left") {
            currentIndex = (currentIndex - 1 + images.length) % images.length;
        } else {
            currentIndex = (currentIndex + 1) % images.length;
        }

        // Show the next image
        images[currentIndex].classList.add("show");
    }
});