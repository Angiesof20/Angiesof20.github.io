#Array Lista: Añade un elemento al vector
print("Lista de Plantas Medicinales :")
Plantas=["Manzanilla", "Aloe Vera ", "Ajo", "Eucalipto ", "Hipérico", "Jengibre ", "Tomillo", "Lavanda", "Diente de león" ]
#Añadimos un elemento a la Lista
Plantas.append("Valeriana")
Plantas.pop(2)
#Recorremos la Lista
for x in Plantas:
    print(x)
#Definimos la Longitud de la Lista
Longitud= len(Plantas)
print("El tamaño o longitud es: ", Longitud)