#App que alingresar el valor incial(x) y el valor final(y),muetsre los datos

x=int(input("Digite el valor inicial: "))
y=int(input("Digite el valor final: "))

for i in range (x,y,1):
    print(i)
else:
    print("Los valores no son correctos")
