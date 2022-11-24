#DISEÑE UNA APP CON UNA FUNCION QUE CALCULE EL AREA DEL CIRCULO Y ESTA SEA LLAMDA POR UN ALGORITMO 
#funcion con parametros
def area(radio):
    are=pi*radio*2
    print("Area de circulo:", are)
    
#app que calcule el area del circulo
radio=int(input("Digite el  radio del circulo:"))
pi=3.1416
area(radio) #llamdo a la funcion area