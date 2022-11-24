//Definir variables
var peso,estatura,imc
//capturamos entradas
peso=parseFloat(prompt("Digite el peso en Kg"));
estatura=parseFloat(prompt("Digite la estatura en Mts"));
//Proceso--Calculamos
imc=peso/(estatura*estatura);

//Proceso Slida
if (imc<18.5) {
    document.write("<p style='color:#FFAE6D;'>"+"Bajo Peso"+"</p>");
    document.write("<p style='color:#FFAE6D;'>"+"Mantener un bajo peso puede causar una pobre condición física y un sistema inmunológico débil, haciéndolos propensos a las infecciones."+" <br> <img src='img/bajopeso.png' height= '90px'>");
} 
else if(imc>=18.5 && imc <=24.9){
    document.write("<p style='color:#3CCF4E;'>"+"Peso Normal"+"</p>");
    document.write("<p style='color:#3CCF4E;'>"+"Mantener un peso saludable puede reducir el riesgo de enfermedades crónicas asociadas al sobrepeso y la obesidad."+" <br> <img src='img/pesonormal.png' height= '70px'>");
}
else if(imc>=25 && imc <=29.9){
    document.write("<p style='color:#EF5B0C;'>"+"Sobrepeso"+" </p>");
    document.write("<p style='color:#EF5B0C;'>"+"Las personas que tienen sobrepeso o tienen un mayor riesgo de afecciones crónicas, tales como hipertensión arterial, diabetes y colesterol alto."+" <br> <img src='img/sobrepeso.png' height= '90px'>");
}
else if(imc>=30 && imc <=34.9){
    document.write("<p style='color:#E74C3C;'>"+"Obesidad I"+"</p>");
    document.write("<p style='color:#E74C3C;'>"+" La obesidad tipo I es una enfermedad crónica tratable que aparece cuando existe un exceso de grasa en el cuerpo.Además, la obesidad se asocia a problemas ortopédicos, incluyendo lumbalgia y agravamiento de la artrosis. "+" <br> <img src='img/obesidad1.png' height= '90px'>");
}
else if(imc>=35 && imc <=39.9){
    document.write("<p style='color:#C0392B;'>"+"Obesidad II"+"</p>");
    document.write("<p style='color:#C0392B;'>"+"La obesidad de grado II se caracteriza por una mayor acumulación de grasa a nivel del abdomen. Se considera de riesgo moderado; sin embargo se evidencia un rango de IMC de 35 a 39.9."+"<br> <img src='img/obesidad2.png' height= '90px'>");
}
else if(imc>=40 && imc <=49.9){
    document.write("<p style='color:#A93226;'>"+"Obesidad III"+"</p>");
    document.write("<p style='color:#A93226;'>"+"Obesidad III"+" La obesidad de grado III recibe el nombre de obesidad mórbida.La obesidad de tipo 3 debe ser tratada con un especialista multidisciplinario pues abarca tanto la perspectiva de un dietista como endocrinólogo."+" <br> <img src='img/obesidad3.png' height= '90px'>");
}
else if(imc>=50){
    document.write("<p style='color:#922B21;'>"+"Obesidad Iv"+"</p)");
    document.write("<p style='color:#922B21;'>"+" las personas con obesidad grado IV tienen un mayor riesgo de morir a una edad más joven debido al cáncer y a muchas otras causas, entre ellas, enfermedades cardíacas, accidentes cerebrovasculares, diabetes y enfermedades del hígado y de los riñones."+" <br> <img src='img/obesidad4.png' height= '70px'> ");
}
else{
document.write("Escriba los valores numericos esperados...");
}

 