#Array Lista: Añade un elemento al vector
print("Lista de Lenguajes de Programación :")
lenguajes=["Python", "JavaScript ", "Java", "C", "C++" ]
#Añadimos un elemento a la Lista
lenguajes.append("PHP")
lenguajes.pop(1)
#Recorremos la Lista
for x in lenguajes:
    print(x)
#Definimos la Longitud de la Lista
Longitud= len(lenguajes)
print("El tamaño o longitud es: ", Longitud)