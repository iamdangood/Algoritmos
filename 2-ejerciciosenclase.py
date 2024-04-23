nombre = input("Bienvenid@ ingresa tu nombre: ")
edad = int(input("Ahora ingresa tu edad: "))

if edad < 0 or edad > 100:
    print("Por favor, ingresa una edad válida.")
else:

    if edad >= 18:
        print("Hola,", nombre + ". Usted es mayor de edad.")
    else:
        print("Hola,", nombre + ". Usted es menor de edad.")
