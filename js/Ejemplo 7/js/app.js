//función que suma 2 números
function sumar() {
    var x,y,suma

    x=parseInt(document.getElementById("n1").value);
    y=parseInt(document.getElementById("n2").value);
  
     suma=x+y;
  
    document.getElementById("resultado_suma").innerHTML= " la suma es: " +suma
}
  
//función que resta 2 números
function restar() {
    var x,y,resta

    x=parseInt(document.getElementById("n1").value);
    y=parseInt(document.getElementById("n2").value);
  
     var resta=x-y;
  
    document.getElementById("resultado_resta").innerHTML= " la resta es: " +resta
}
//función que Multiplica 2 números
function multiplicar() {
    var x,y,multiplicacion

    x=parseInt(document.getElementById("n1").value);
    y=parseInt(document.getElementById("n2").value);
  
    multiplicacion=x*y;
  
    document.getElementById("resultado_multiplicacion").innerHTML= " la multiplicación es: " +multiplicacion
}
  
//función que Divide 2 números
function dividir() {
    var x,y,divide

    x=parseFloat(document.getElementById("n1").value);
    y=parseFloat(document.getElementById("n2").value);
  
    divide=x/y;
  
    document.getElementById("resultado_dividir").innerHTML= " la división es: " +divide
}
  