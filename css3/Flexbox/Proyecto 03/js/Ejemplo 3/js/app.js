//Definir variables
var op;
var n1, n2, resultado;

op=parseInt(prompt(" Escoja un opción del menú:"));
switch (op) {
    case 1:
        n1=parseInt(prompt("Digite el primer número:"));
        n2=parseInt(prompt("Digite el segundo número:"));
        resultado=n1+n2;
        document.write(" La suma de: " +n1+ " + " +n2+ " es: " +resultado);
    break;
    
    case 2:
        n1=parseInt(prompt("Digite el primer número:"));
        n2=parseInt(prompt("Digite el segundo número:"));
        resultado=n1-n2;
        document.write(" La resta  de: " +n1+ " + " +n2+ " es: " +resultado);
    break;
    
    case 3:
        n1=parseInt(prompt("Digite el primer número:"));
        n2=parseInt(prompt("Digite el segundo número:"));
        resultado=n1*n2;
        document.write(" La multiplicación  de: " +n1+ " + " +n2+ " es: " +resultado); 
    break;
    
    case 4:
        n1=parseFloat(prompt("Digite el primer número:"));
        n2=parseFloat(tprompt("Digite el segundo número:"));
        resultado=n1/n2;
        document.write(" La división  de: " +n1+ " + " +n2+ " es: " +resultado); 
    break;
    
    

    default:
       //document.write("Seleccione una opción del menú");
    break;
}