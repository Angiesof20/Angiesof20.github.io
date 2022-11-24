#Creamos la Lista vacia
titulo=[]
genero=[]
duracion=[]
protagonista=[]
estreno=[]
precio=[]
idioma=[]
#Definimos un tamaño para las listas
Tamaño=int(input(" Tamaño de la Lista? : "))
#Recorrimos la lista hasta el tamaño definido
for i in range(Tamaño):
    print("Ingrese el titulo de la pelicula: ", i+1)
    ti=input("Titulo de la pelicula: ")
    ge=input("Género de la pelicula: ")
    du=input("Duración de la pelicula: ")
    pro=input("Protagonista de la pelicula: ")
    año=input("Año de estreno de la pelicula: ")
    pre=input("Precio de la pelicula: ")
    idi=input("Idioma de la pelicula: ")

    titulo.append(ti)
    genero.append(ge)
    duracion.append(du)
    protagonista.append(pro)
    estreno.append(año)
    precio.append(pre)
    idioma.append(idi)
print("------Información de la pelicula--------- ")
print("Los datos de la pelicula són: ")
#Ahora mostresmos las listas
for i in range(Tamaño):
    print("Titulo:", titulo[i])  
    print("Género: ", genero[i])
    print("Duración: ", duracion[i])
    print("Protagonista: ", protagonista[i])
    print("Año de Estreno: ", estreno[i])
    print("Precio: ", precio[i])
    print("Idioma: ", idioma[i])
    print("---------------------------------------------------")
    
