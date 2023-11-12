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


//Deshabilitamos en el formulario, la opcion "elegir" del select Especialidades
document.addEventListener('DOMContentLoaded', function () { //cuando se carga toda la pagina se ejecuta esta funcion
    var medicoSelect = document.getElementById('id_medico'); //agarra el select de los medicos y lo mete en la variable medicoSelect
    medicoSelect.disabled = true; //y aca lo deshabilita a ese select
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
    var especialidadSelect = document.getElementById('id_especialidad'); //toma el campo id, proveniente de la tabla Especialidad, de la especialidad elegida y lo pone en especialidadSelect
    var medicoSelect = document.getElementById('id_medico'); //toma el campo id, proveniente de la tabla Medico, pero veo que aparece vacio, es decir, no toma nada, porque todavia no se selecciono ningun medico en el input de medicos
    console.log("especialidadSelect: " + especialidadSelect.value);
    console.log("medicoSelect: " + medicoSelect.value);
    
    var especialidadId = especialidadSelect.value; //mete el id de la especialidad elegida en especialidadId, lo hace utilizando el .value para que le de el valor, si no le ponemos el .value tira un objectHTML, con el .value tira directamente el valor del id, por ejemplo "7"
    medicoSelect.innerHTML = '<option value="">Seleccione un médico</option>'; //Limpia el input de medicos, y pone una opcion donde dice que seleccione un medico

    if (especialidadId) { //si especialidadId no es una cadena vacia o nula, entonces que haga lo siguiente (esto sera asi cuando se haya seleccionado algo en especialidades, por ejemplo, cuando tenga un 7, siguiendo el ejemplo de que el usuario elija una especialidad con el id 7)
        console.log('Especialidad seleccionada:', especialidadId); // Agrega este mensaje de depuración
        fetch('/cargar_medicos/?especialidad_id=' + especialidadId)
            .then(response => response.json())
            .then(data => {
                console.log('Respuesta de cargar_medicos:', data); // Agrega este mensaje de depuración
                //data tiene la respuesta de la vista cargar_medicos()
                //un ejemplo de esa respuesta seria: un json, con este diccionario clave-valor:
                //{ id = 001 , nombre = "Martin Alejandro Nuñez" }
                //en este caso devuelve el unico medico que tiene la especialidad seleccionada
                if (data.length > 0){
                data.forEach(function(medico) { //se hace un foreach en data, donde en cada iteracion, cada elemento actual va a tener el nombre de "medico"
                    var option = document.createElement('option'); //Se crea un nuevo elemento HTML <option> utilizando el método createElement del objeto document. Este elemento de opción se utilizará para representar a un médico en un menú desplegable.
                    option.value = medico.id; //Se establece el valor del option, dandole de valor el id del medico. Esto se hace para que cuando el usuario seleccione este médico, se use el id de ese medico como valor 
                    option.textContent = medico.nombre; // Esto es lo que se mostrará en el menú desplegable para representar al médico. Lo que ve el usuario. Le asignamos el nombre del medico
                    medicoSelect.appendChild(option); //El elemento de opción creado se agrega como hijo al elemento <select>, en este caso representado por la variable medicoSelect. El médico ahora estará disponible como una opción en el menú desplegable. Digamos que aca insertamos esa opcion que creamos, en el select
                });
                medicoSelect.disabled = false; //aca habilitamos el select de medicos, para que se pueda elegir
                }
                else{   //en caso de que no haya medicos para especialidad:
                    medicoSelect.disabled = true; //Deshabilitamos la opcion de elegir medico
                    medicoSelect.innerHTML = '<option value="">No hay medicos disponibles para esta especialidad</option>'; 
                }
            })
            .catch(error => console.error(error)); //Captura cualquier error que ocurra durante la ejecución de la operación asíncrona y lo imprime en la consola. 
    }
    else{
        medicoSelect.disabled = true; //Deshabilitamos la opcion de elegir medico, en caso de que especialidadId sea una cadena vacia o nula, esta linea de codigo sirve por si se vuelve a poner "seleccione una especiliadad" en el input de arriba
    }
}

