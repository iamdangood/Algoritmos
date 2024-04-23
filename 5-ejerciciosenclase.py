Notas = print("Bienvenid@ estudiante ingrese sus notas a continuacion: ")
not1 = float(input("Ingrese su primer nota de 0.0 a 5.0:  "))
not2 = float(input("Ingrese su segunda nota de 0.0 a 5.0:  "))
not3 = float(input("Ingrese su tercera nota de 0.0 a 5.0:  "))
not4 = float(input("Ingrese su cuarta nota de 0.0 a 5.0:  "))
not5 = float(input("Ingrese su quinta nota de 0.0 a 5.0:  "))

suma_notas = not1+not2+not3+not4+not5
promedio = suma_notas / 5

if promedio >= 3.0:
    print("Aprobó.")
else:
    print("No aprobó.")

