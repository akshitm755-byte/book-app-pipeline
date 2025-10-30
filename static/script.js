var modal = document.getElementById("bookModal");
function openModal(title, synopsis) {
    document.getElementById("modalTitle").innerText = title;
    document.getElementById("modalSynopsis").innerText = synopsis;
    modal.style.display = "block";
}
function closeModal() {
    modal.style.display = "none";
}
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
