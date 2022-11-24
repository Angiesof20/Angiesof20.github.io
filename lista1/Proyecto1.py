#Array Lista: Añade un elemento al vector
print("Lista de Clases de Libros:")
Libros=["Cien años de soledad,de Gabriel García Márquez", "El señor de los anillos (Trilogía), de J. R. R. Tolkien.", "Un mundo feliz, de Aldous Huxley.", "Orgullo y prejuicio, de Jane Austen", "Crimen y castigo, de Fiódor Dostoyevski.", "Olita, de Vladimir Nabokov", "Ulises, de James Joyce. Ulises, de James Joyce. " ]
#Añadimos un elemento a la Lista
Libros.append("Las Alams Muestras de Nicolai Goloi")
Libros.pop(1)
#Recorremos la Lista
for x in Libros:
    print(x)
#Definimos la Longitud de la Lista
Longitud= len(Libros)
print("El tamaño o longitud es: ", Longitud)