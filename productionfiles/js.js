const searchInput = document.getElementById('searchInput');
const tableRows = document.querySelectorAll('#vehicleTable tbody tr');

const rowsPerPage = 10; // adjust this value to change the number of rows per page
let currentPage = 1;

searchInput.addEventListener('input', (e) => {
  const searchTerm = e.target.value.toLowerCase();
  tableRows.forEach((row) => {
    const rowText = row.textContent.toLowerCase();
    if (rowText.includes(searchTerm)) {
      row.style.display = '';
    } else {
      row.style.display = 'none';
    }
  });
});

