#app que pregunte al usuario la edad y muestre por pantalla todos los años que ha cumplido (desde uno hasta su edad)

edad=int(input("¿Cúantos años tienes?: " ))
for i in range(edad):
   print("Usted ha cumplido:" + str(i+1) + " años de edad")

