//Aplicacion para evaluar la Fiebre de una persona
var temp;

//Capturar los datos de entrada
temp=parseFloat(prompt("Ingrese su temperatura en grados °C:"));

//Proceso para evaluar la Fiebre
if (temp >=38) {
document.write(" La temperatura " +temp+ " °C indica Fiebre <img src='img/enfermo.png' height= '30px'> " );
    
} else {
document.write(" La temperatura " +temp+ " °C indica paciente sin Fiebre <img src='img/fiebre.png' height= '30px'>");

}

