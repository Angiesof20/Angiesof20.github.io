#Diseñe una app que permita al usuario ingresar fruta y el precio unitario y lo almacene en un diccionario llamado factura.
# Despues debe mostrar un mensaje concatenado donde aparece el nombre a fruta, su valor, la acntidad y el total.

fruta=input("Digite el nombre de la fruta: ")
precio=int(input("Digite el precio de la fruta: "))
cantidad=int(input("Digite la cantidad de frutas compradas: "))


factura={"fruta":fruta, "precio":precio }


print("---------------FACTURA-----------------")
print( "Producto:",factura["fruta"]) 
print("Precio unitario:", factura["precio"]) 
print("Cantidad:", cantidad)
print("Total:",(cantidad*precio))
print("----------------------------------------")











