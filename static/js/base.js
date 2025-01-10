// Get modal element
const modal = document.getElementById("editModal");
const closeModal = document.querySelector(".custom-modal-close");
const editForm = document.getElementById("editForm");
let currentRow;

// Open modal and populate form
document.querySelectorAll('.edit-btn').forEach(button => {
    button.addEventListener('click', (event) => {
        currentRow = event.target.closest('tr');
        const name = currentRow.cells[1].innerText;
        const age = currentRow.cells[2].innerText;

        // Populate the form
        document.getElementById('name').value = name;
        document.getElementById('age').value = age;

        // Show the modal
        modal.style.display = "block";
    });
});

// Close the modal
closeModal.onclick = function() {
    modal.style.display = "none";
}

// Save changes and update the table
editForm.onsubmit = function(e) {
    e.preventDefault();

    const updatedName = document.getElementById('name').value;
    const updatedAge = document.getElementById('age').value;

    // Update the row
    currentRow.cells[1].innerText = updatedName;
    currentRow.cells[2].innerText = updatedAge;

    // Close the modal
    modal.style.display = "none";
}

// Close modal when clicking outside of it
window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
}
