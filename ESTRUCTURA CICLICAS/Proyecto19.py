#App que al ingresar un numero entero positivo, muestre por pantalla todos los numeros impares desde el 1 hasta el número ingresado
n=int(input("Ingresa un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=",")