// Validacion del input DNI:

document.addEventListener('input', function (e) {
    if (e.target.classList.contains('dni-input')) {
        // Permite solo números en el campo DNI
        e.target.value = e.target.value.replace(/[^0-9]/g, '');

        // Limita la longitud del campo a 8 caracteres
        if (e.target.value.length > 8) {
            e.target.value = e.target.value.slice(0, 8);
        }
    }
});

// Validacion de inputs que solo llevan Letras
document.addEventListener('input', function (e) {
    if (e.target.classList.contains('solo-letras')) {
        // Permite solo letras en los campos especificados
        e.target.value = e.target.value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚ\s]/g, '');
    }
});
