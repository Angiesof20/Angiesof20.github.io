//Definir variables
var base,altura,perimetro

//Capturar los datos del rectangulo..entrada
base=parseFloat(prompt("Ingrese la base del rectangulo"));
altura=parseFloat(prompt("Ingrse la altura del rectangulo"));

//Proceso del perimetro
perimetro=(base+altura)*2;

//Mensaje de Salida
document.write ("El perimetro del rectangulo es:" +perimetro);
