window.onload = function () {
    const btnDelete = document.querySelectorAll('.btnDelete');

    btnDelete.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmDelete = confirm('Deseas eliminar este usuario?');

            if (!confirmDelete) {
                e.preventDefault();
            }
        });
    })
};


function filterEmail() {
    let input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("filterEmail");
    filter = input.value.toUpperCase();
    table = document.getElementById("tableUser");
    tr = table.getElementsByTagName("tr");

    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[3];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
};