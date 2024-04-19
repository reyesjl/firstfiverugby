document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('clear-button').addEventListener('click', function() {
        // Clear form fields
        document.getElementById('search').value = '';
        document.getElementById('type').value = '';
        document.getElementById('paid').value = '';
        
        // Submit the form
        document.getElementById('filter-form').submit();
    });

    // Array to store selected row data
    let selectedRows = [];

    // Click event listener for table rows
    const rows = document.querySelectorAll("#camps-table tbody tr");
    rows.forEach(function(row) {
        const recordId = row.dataset.recordId; // Get the record ID from data attribute
        row.addEventListener("click", function() {
            const rowData = getRowData(row);
            const index = selectedRows.findIndex(item => item.recordId === recordId); // Check if the row is already selected

            if (index !== -1) {
                // Row already selected, deselect it
                row.classList.remove("selected");
                selectedRows.splice(index, 1);
                console.log(rowData, "unselected");
            } else {
                // Row not selected, select it
                row.classList.add("selected");
                selectedRows.push(rowData);
                console.log(rowData, "selected");
            }
        });
    });

    // Function to get row data
    function getRowData(row) {
        const rowData = {};
        const cells = row.querySelectorAll("td");
        rowData.first_name = cells[0].innerText;
        rowData.last_name = cells[1].innerText;
        rowData.camp_title = cells[2].innerText;
        rowData.email = cells[3].innerText;
        rowData.type = cells[4].innerText;
        rowData.paid = cells[5].innerText;
        rowData.recordId = row.dataset.recordId; // Include record ID in row data
        return rowData;
    }
});