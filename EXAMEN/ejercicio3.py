#Diseñe una app que, al ingresar una contraseña, valide si la contraseña introducida
#coincide con la contraseña del sistema, si es verdadero que muestre un mensaje de
#bienvenida, sino que muestre un mensaje indicando la contraseña es errónea.


c=input("Ingresa una contraseña: ")
consistema="12345"

while c !=consistema:
    print("La contraseña no coincide con la del sistema!")
else:
    print("--BIENVENIDO A LA PLATAFORMA--")
