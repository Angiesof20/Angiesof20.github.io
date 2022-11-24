#Diseñe una app que, al ingresar el Nombre, la Edad, el Sueldo, debe mostrar por pantalla un mensaje concatenando todos los valores
nombre=(input("Ingrese su nombre: "))
edad=int(input("Ingrese su edad: "))
sueldo=int(input("Ingrese su sueldo: "))

print("-------Mensaje---------")
print( "Su nombre es", nombre) 
print("Tiene" , edad , " años de edad ") 
print("Su sueldo es de: " , sueldo ,"$")
print("-----------------------")