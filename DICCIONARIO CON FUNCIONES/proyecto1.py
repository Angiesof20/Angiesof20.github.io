#1. Diseñe un App que permita al ussuario ingresar: nombre, direccion, edad y telefono, estos datos se deben almacenar en un diccionario llamado persona. 
# Estos datos se deben mostrar por pantalla de forma concatenada, ejemplo: Juan tiene 17 años, vive em la calle 8 #27 18A y su número de telfono es 1234567 

nombre=input("Digite su nombre: ")
edad=input("Digite su edad: ")
direccion=input("Digite su dirección: ")
telefono=input("Digite su teléfono: ")

persona={"nombre":nombre, "edad":edad, "direccion":direccion,"telefono":telefono}

print(persona["nombre"], "Tiene: ", persona["edad"],"años",", y vive en:", persona["direccion"], "y su número de teléfono es:", persona["telefono"])


