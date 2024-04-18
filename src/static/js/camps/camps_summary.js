document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('clear-button').addEventListener('click', function() {
        // Clear form fields
        document.getElementById('search').value = '';
        document.getElementById('type').value = '';
        document.getElementById('paid').value = '';
        
        // Submit the form
        document.getElementById('filter-form').submit();
    });
});