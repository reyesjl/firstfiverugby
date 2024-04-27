document.addEventListener('DOMContentLoaded', function() {
        // Get all tab contents and initialize index
        var tabContents = document.querySelectorAll('.tab-content');
        var currentIndex = 0;

        // Show initial tab content
        showTab(currentIndex);

        // Function to show tab content based on index
        function showTab(index) {
            tabContents.forEach(function(content, i) {
                if (i === index) {
                    content.classList.add('active');
                } else {
                    content.classList.remove('active');
                }
            });
        }

        // Handle back button click
        document.querySelector('.tab-back').addEventListener('click', function() {
            currentIndex = (currentIndex - 1 + tabContents.length) % tabContents.length;
            showTab(currentIndex);
        });

        // Handle next button click
        document.querySelector('.tab-next').addEventListener('click', function() {
            currentIndex = (currentIndex + 1) % tabContents.length;
            showTab(currentIndex);
        });
    });