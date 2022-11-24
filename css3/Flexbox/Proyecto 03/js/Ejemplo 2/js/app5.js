//Definir las variables
var ingreso,gasto;

//Capturar
ingreso=prompt("Ingrese el valor del ingreso");
gasto=prompt ("Ingrese el valor del gasto")


//Evaluamos el proceso de ganacia y perdida
if (ingreso>gasto) {
    document.write(" Es ganacia <img src='img/ganancias.png' height= '30px'>");
        
    } else {
    document.write(" Es perdida <img src='img/perdida.png' height= '30px'>");
        
    }