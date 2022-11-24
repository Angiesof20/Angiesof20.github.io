#Diseñe una app que permita almacenar la información de los clientes de una empresa. Los cleintes se guardaran en un diccionario llamado clientes.
#los datos deben ser ingresados por el usuarios, identificacin del cliente, nombre, dirección, teléfono, correo y empresa. La app debe
#1. Pregutar alususario por una opción del menú
#2. Mostrar clientes
#3. Eliminar clientes
#4. Salir
cliente={}
op=""

while op !=4:

    if op==1:
        identificacion=input("Digite su identificación: ")
        nombre=input("Digite el nombre: ")
        direccion=input("Digite la dirección: ")
        telefono=input("Digite el número de teléfono:")
        correo=input("Digite el correo: ")
        empresa=input("Digite el nombre de la empresa: ")
        cliente={
              "identificacion": identificacion,
              "nombre":nombre,
              "direccion":direccion, 
              "telefono":telefono,
              "correo": correo,
             "empresa":empresa 
            }
            

    if op==2:
        print("Identificación del cliente")
        print("----------------------------")
        print("Identificación: ", cliente["identificacion"])
        print("Nombre completo:", cliente["nombre"])
        print("Direccion:", cliente["direccion"])
        print("Teléfono:", cliente["telefono"])
        print("Correo:", cliente["correo"] )
        print("Empresa:", cliente["empresa"])

    if op==3:
        del cliente["identificacion"]
        print("-------------------------")
        print("Cliente eliminado con exito!")
    if op==4:
        exit()
    
    print("-----MENÚ------")
    print("1. Añadir cliente")
    print("2. Mostrar cliente")
    print("3. Eliminar cliente")
    print("4. Salir")

    op=int(input("Digite la opción seleccionada: "))