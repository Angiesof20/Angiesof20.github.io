#ALMACEN DE ZAPATOS

precio=int(input("Digite el precio del zapato: "))
cantidad=int(input("Digite la cantidad de zapatos comprados: "))

if cantidad<10:
    print("No obtendra ningun descuento")
elif cantidad>=10 and cantidad <20:
    descuento=precio*0.10
    print("Obtendra un 10% de descuento sobre el total de la compra")
    print("El descuento obtenido es :",descuento)
elif cantidad>20 and cantidad <30:
    descuento=precio*0.20
    print("Obtendra un 20% de descuento sobre el total de la compra")
    print("El descuento obtenido es :",descuento)
elif cantidad>=30:
     descuento=precio*0.40
     print("Obtendra un 40% de descuento sobre el total de la compra")
     print("El descuento obtenido es :",descuento)
else:
    print("Ingrese una cantidad zapatos validas")


