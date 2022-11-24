#App que al ingresar una nota; Si la nota es mayor igual a
#3 entonces es APROBADO, sino, REPROBADO.

nota=int(input("Digite su nota: "))

if nota>=3:
    print("Aprobó")
else:
    print("Reprobó")