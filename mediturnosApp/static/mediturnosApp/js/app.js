// Validaciones

function validarEmail(email) {
    // Expresión regular para validar el email
    let regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    // Comprueba si el email coincide con la expresión regular
    return regex.test(email);
}

document.addEventListener('input', function (e) {
    // Validacion del input DNI:
    if (e.target.classList.contains('dni-input')) {
        // Permite solo números en el campo DNI
        e.target.value = e.target.value.replace(/[^0-9]/g, '');

        // Limita la longitud del campo a 8 caracteres
        if (e.target.value.length > 8) {
            e.target.value = e.target.value.slice(0, 8);
        }
    }

    // Validación de inputs que solo llevan Letras
    if (e.target.classList.contains('solo-letras')) {
        // Permitimos solo letras (mayúsculas, minúsculas y la letra "ñ")
        e.target.value = e.target.value.replace(/[^a-zA-ZáéíóúüÁÉÍÓÚñÑ\s]/g, '');
    }

    // Validaciones adicionales, si no son válidas, agrega la clase 'input-no-valido'
    if (e.target.name === 'nombre' && e.target.value.length < 3) {
        e.target.classList.add('input-no-valido');
    } else if (e.target.name === 'apellido' && e.target.value.length < 2) {
        e.target.classList.add('input-no-valido');
    } else if (e.target.name === 'dni' && e.target.value.length < 7) {
        e.target.classList.add('input-no-valido');
    } else if (e.target.name === 'email' && !validarEmail(e.target.value)) {
        e.target.classList.add('input-no-valido');
    } else {
        // Si el campo es válido, quita la clase 'input-no-valido':
        e.target.classList.remove('input-no-valido');
    }

});

//Deshabilita en el formulario, la opcion "elegir" del select Especialidades
document.addEventListener('DOMContentLoaded', function () {
    var especialidadSelect = document.getElementById('id_especialidad');
    var optionElegir = especialidadSelect.querySelector('option[value=""]');

    // Cambia el color de la opción "Elegir"
    optionElegir.style.color = 'gray';

    // Deshabilita la opción "Elegir"
    optionElegir.disabled = true;
});


document.addEventListener("DOMContentLoaded", function () {
    var especialidadSelect = document.getElementById("id_especialidad");
    var medicoSelect = document.getElementById("id_medico");

    // Define un objeto que mapea especialidades a médicos
    var medicosPorEspecialidad = {
        Pediatría: ["Carlos López", "Laura García", "Diego Fernández"],
        Traumatología: ["María Rodríguez", "Pepe Argento", "Sofía Torres"],
        Clínica: ["Juan Perez", "Laura García", "Ana Martinez"]
    };

    // Escucha el cambio en el select de especialidad
    especialidadSelect.addEventListener("change", function () {
        var especialidadSeleccionada = especialidadSelect.value;
        var medicos = medicosPorEspecialidad[especialidadSeleccionada] || [];

        // Limpiar el campo de selección de médicos
        medicoSelect.innerHTML = "";

        // Agregar opción predeterminada
        var defaultOption = document.createElement("option");
        defaultOption.value = "";
        defaultOption.text = "Seleccione un médico";
        medicoSelect.appendChild(defaultOption);

        // Agregar opciones de médicos
        medicos.forEach(function (medico) {
            var option = document.createElement("option");
            option.value = medico;
            option.text = medico;
            medicoSelect.appendChild(option);
        });
    });

    window.addEventListener("DOMContentLoaded", function () {
        // Obtén referencias a los controles select
        var especialidadSelect = document.getElementById("id_especialidad");
        var medicoSelect = document.getElementById("id_medico");
        var opcionMedico = document.getElementById("id_medico");
        medicoSelect.disabled = true;
        if (opcionMedico){
            var optionIndex = 0;
            opcionMedico.options[optionIndex].text = "Elija una especialidad";
        }

        // Agrega un evento "change" al select de especialidad
        especialidadSelect.addEventListener("change", function () {
            // Verifica si el valor de especialidadSelect no es vacío
            if (especialidadSelect.value !== "") {
                // Habilita el select de médicos
                medicoSelect.disabled = false;
            }
        });
    });
    
});

