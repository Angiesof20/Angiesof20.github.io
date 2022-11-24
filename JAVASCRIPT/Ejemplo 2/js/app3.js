//Definir variables
var n;

//Capturar la nota
n=parseInt(prompt("Digite la nota"));

//Evaluamos el proceso de la nota
if (n>=3) {
document.write("El estudiante aprobó <img src='img/aprobado.png' height= '40px'>");
    
} else {
document.write("El estudiante reprobó <img src='img/rechazado.png' height= '40px'>");
    
}
