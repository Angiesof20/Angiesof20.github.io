'''Diseñe una app que al ingresar por el usuario su valor de renta anual y muestre por pantalla:
#1. El Valor por Declarar
#2. El Impuesto Calculado
Menos de 100.000.000 5%
Entre 100.000.000 y 200.000.000 15%
Entre 200.000.000 y 350.000.000 20%
Entre 350.000.000y 600.000.000 30%
Más de 600.000.000 45%'''

vrenta=int(input("Ingrese su valor de rental anual: "))

if vrenta<100.000000:
    impuesto=vrenta*0.10
    print("Su valor a declarar es: ", vrenta)
    print("Su impuesto calculado es de: ", impuesto)
elif vrenta>=100.000000 and vrenta <=200.000000:
    impuesto=vrenta*0.15
    print("Su valor a declarar es: ", vrenta)
    print("Su impuesto caculado es de : ", impuesto)
elif vrenta >=350.000000 and vrenta <=600.000000:
    print("Su valor a declarar es: ", vrenta)
    impuesto=vrenta*0.20
    print("Su impuesto caculado es de : ", impuesto)
elif vrenta>600.000000:
    print("Su valor a declarar es: ", vrenta)
    impuesto=vrenta*0.45
    print("Su impuesto caculado es de : ", impuesto)
else:
    print("Ingrese un valor valido")


