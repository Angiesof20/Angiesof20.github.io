#app que  al ingresar un valor de ingreso y un valor de gastos; Si el
#ingreso es mayor al gasto es GANANCIA sino es PERDIDA.

ingreso=int(input("Digite el valor de ingreso: "))
gastos=int(input("Digite el valor de gastos: "))

if ingreso>gastos: 
    print("Es ganancia")
else:
    print(" Es perdida")
