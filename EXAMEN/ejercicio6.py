#Diseñe una app que pida un número entero mayor que cero y que escriba sus divisores
n=int(input("Digite un numero entero mayor que cero"))

if n<=0:
    print("El numero debe ser mayor a cero")
else:
    for i in range (1, n+1):
        if n % i ==0:
            print(i)
