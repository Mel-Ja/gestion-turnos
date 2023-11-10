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
    var medicoSelect = document.getElementById('id_medico');
    medicoSelect.disabled = true;
});


//inicio de sesión
const passWordInput = document.querySelector
('#ingresodecontraseña')
//metemos en la variable passWordInput a el input donde se escribe
//la contraseña


//Iconos
const showPassword = document.querySelector
('#show-password')
//metemos en la variable showPassword a el icono de mostrar contraseña

const hidePassword = document.querySelector
('#hide-password')
//metemos en la variable hidePassword a el icono de ocultar contraseña


//Boton
const btnStatePassword = document.querySelector
('.btn-hide-show')
//metemos en btnStatePassword al Boton donde estan los dos iconos
//de mostrar/ocultar contraseña

// ---------------------------------------------------------------
btnStatePassword.addEventListener('click', () => {
  event.preventDefault();
  if(passWordInput.type === 'password'){
    passWordInput.type = 'text'
    showPassword.style.display = 'none'
    hidePassword.style.display = 'block'
   
  }
  else{
    passWordInput.type = 'password'
    showPassword.style.display = 'block'
    hidePassword.style.display = 'none'
  }
  
})

/* En el boton, hacemos un addEventListener, para que cuando se haga
click, se ejecute una funcion, esa funcion hace lo siguiente:
si el input (donde se escribe la contraseña), es de tipo password
(osea que no se mostrara lo que se escribe)...
entonces pasamos el tipo a texto, de esta manera se mostrara
al mismo tiempo, modificamos el css de los dos iconos, ocultando uno,
y mostrando el otro, en caso de que sea al reves, que cuando se haga click
el input este en tipo texto, se pasa a modo password, y se oculta un icono,
y se muestra el otro
*/


/* Función cargar medicos que llama a la view cargar_medicos y crea los elementos Option correspondientes en el select de Medicos */
function cargarMedicos() {
    var especialidadSelect = document.getElementById('id_especialidad');
    var medicoSelect = document.getElementById('id_medico');
    
    var especialidadId = especialidadSelect.value;
    medicoSelect.innerHTML = '<option value="">Seleccione un médico</option>';

    if (especialidadId) {
        console.log('Especialidad seleccionada:', especialidadId); // Agrega este mensaje de depuración
        fetch('/cargar_medicos/?especialidad_id=' + especialidadId)
            .then(response => response.json())
            .then(data => {
                console.log('Respuesta de cargar_medicos:', data); // Agrega este mensaje de depuración
                data.forEach(function(medico) {
                    var option = document.createElement('option');
                    option.value = medico.id;
                    option.textContent = medico.nombre;
                    medicoSelect.appendChild(option);
                });
                medicoSelect.disabled = false;
            })
            .catch(error => console.error(error));
    }
}