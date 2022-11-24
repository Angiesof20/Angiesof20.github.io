#Creamos la Lista vacia
marca=[]
modelo=[]
color=[]
combustible=[]
cilindraje=[]
precio=[]
#Definimos un tamaño para las listas
Tamaño=int(input(" Tamaño de la Lista? : "))
#Recorrimos la lista hasta el tamaño definido
for i in range(Tamaño):
    print("Ingrese la marca del vehiculo: ", i+1)
    mar=input("Marca del vehiculo: ")
    mod=input("Modelo del vehiculo: ")
    col=input("Color del vehiculo: ")
    com=input("Combustible del vehiculo: ")
    cil=input("Cilindraje del vehiculo: ")
    pre=input("Precio del vehiculo: ")

    marca.append(mar)
    modelo.append(mod)
    color.append(col)
    combustible.append(com)
    cilindraje.append(cil)
    precio.append(pre)
print("------Información del Vehiculo--------- ")
print("Los datos del vehiculo son: ")
#Ahora mostresmos las listas
for i in range(Tamaño):
    print("Marca:", marca[i])  
    print("Modelo: ", modelo[i])
    print("Color:, ", color[i])
    print("Combustible: ", combustible[i])
    print("Cilindraje: ", cilindraje[i])
    print("Precio:", precio[i])
    print("---------------------------------------------------")
    


