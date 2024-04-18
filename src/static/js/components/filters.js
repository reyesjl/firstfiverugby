document.addEventListener('DOMContentLoaded', function() {
    const toggleFiltersButton = document.getElementById('toggle-filters');
    const filterFormWrapper = document.getElementById('filter-form-wrapper');

    // Add event listener to the toggle button
    toggleFiltersButton.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default link behavior
        filterFormWrapper.classList.toggle('collapsed'); // Toggle the 'collapsed' class
        console.log('collapsed')
    });
});