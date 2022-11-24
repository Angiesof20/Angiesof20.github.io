#APLICACION QUE CALCULE EL AREA DEL RECTANGULO Y LUEGO SEA LLAMDA POR UN ALGORITMO 
#FUNCION CON PARAMETROS 
#Funcion area
def area(b,h):
    ar=b*h
    print("El area del rectangulo es:", ar)

#app que calcula el area del rectangulo
b=int(input("Digite la base del reactangulo:"))
h=int(input("Digite la altura del reactangulo:"))
area(b,h)#llamado de la función area