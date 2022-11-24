#indice de masa corporal
estatura=float(input("Digite la estatura (metros): "))
peso=int(input("Digite el peso del paciente (kg)"))
imc=peso/(estatura*estatura)

if imc <18.5:
    print("El paciente tiene bajo peso")
elif imc >=18.5 and imc <=24.9:
    print("El paciente tiene un peso normal")
elif imc >=25 and imc <=29.9:
     print("El paciente tiene sobre peso")
elif imc >=30 and imc <=34.9:
    print("El paciente tiene obesidad I")
elif imc >=35 and imc <=39.9:
    print("El paciente tiene obesidad II") 
elif imc >=40 and imc <= 49.9:
    print("El paciente tiene obesidad III")
elif imc >50:
    print("El paciente tiene obesidad IV")
else:
    print("Digite el IMC correcto")
