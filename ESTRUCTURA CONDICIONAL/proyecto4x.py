#presion arterial
presion=int(input("Digite la presion arterial: "))

if presion <90:
    print("El paciente tiene la presion baja")
if presion<120:
    print("El paciente tiene una presion normal")
if presion >=120 and presion <=139:
    print("El paciente tiene  Prehipertension")
if presion >=140 and presion <=159:
    print("El paciente tiene  Alta:hipertension fase 1")
if presion <=60:
    print("El paciente tiene  Alta:hipertension fase 2")
else:
    print("Digite una presion arterial valida")