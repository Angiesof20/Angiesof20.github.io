//Aplicacion para evaluar si un numero esta entre 10 y 100
var n;

//Capturando la Entrada 
n=parseInt(prompt("Digite el número entero"));


//Evaluamos el proceso numero
if (n>=10 && n<=100) {
document.write(" El número: " +n+ " esta entre 10 y 100 <img src='img/aprobado.png' height= '40px'>");
    
} else {
document.write(" El número : " +n+ " no esta entre 10 y 100 <img src='img/rechazado.png' height= '40px'>");
    
}