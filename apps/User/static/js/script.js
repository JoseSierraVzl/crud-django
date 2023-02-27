window.onload = function() {
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

