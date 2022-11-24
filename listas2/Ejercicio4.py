#Creamos la Lista vacia
codigo=[]
cliente=[]
nombre=[]
fecha=[]
descripción=[]
preciou=[]
cantidad=[]
total=[]

#Definimos un tamaño para las listas
Tamaño=int(input(" Tamaño de la Lista? : "))
#Recorrimos la lista hasta el tamaño definido
for i in range(Tamaño):
    print("Ingrese los datos del producto: ", i+1)
    co=input("Código de la factura: ")
    cli=input("Código del cliente: ")
    nom=input("Nombre del cliente: ")
    fac=input("Fecha de factura: ")
    precio=int(input("Precio unitario del producto:"))
    des=input("Descripción del producto: ")
    can=int(input("Cantidad del producto: "))


    codigo.append(co)
    cliente.append(cli)
    nombre.append(nom)
    fecha.append(fac)
    descripción.append(des)
    preciou.append(precio)
    cantidad.append(can)
    total.append(cantidad[i] * preciou[i])


print("---------------------------------------------")   
print("             FACTURA           "              )
print("---------------------------------------------")   
#Ahora mostresmos las listas
for i in range(Tamaño):
    print("CODIGO DE FACTURA: ",codigo[i])  
    print("----------------------------------")
    print("CODIGO DEL CLIENTE: ", cliente[i])
    print("----------------------------------")
    print("FACTURAR A: ", nombre[i])
    print("----------------------------------")
    print("FECHA: ", fecha[i])
    print("----------------------------------")
    print("PRECIO UNITARIO: ", preciou[i])
    print("----------------------------------")
    print("DESCRIPCIÓN: ", descripción[i])
    print("----------------------------------")
    print("CANT.: ", cantidad[i])
    print("----------------------------------")
    print("TOTAL: ", total[i],)
    print("---------------------------")
    
