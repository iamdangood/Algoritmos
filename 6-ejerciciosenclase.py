opcion = """
(1) - opcion 1 Rectángulo
(2) - opcion 2 Cuadrado
(3) - opcion 3 Paralelogramo
(4) - opcion 4 Rombo
(5) - opcion 5 Trapecio
(6) - opcion 6 Triangulo
(7) - opcion 7 Triángulo equilatero
(8) - opcion 8 Triángulo Rectangulo
(9) - opcion 9 Poligono Regular
"""
opcion = int(input("Ingrese el número de la figura deseada: "))
 
if opcion == 1:
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    area = base * altura
    print("El área del rectángulo es:", area)
elif opcion == 2:
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = lado ** 2
    print("El área del cuadrado es:", area)
elif opcion == 3:
    base = float(input("Ingrese la base del paralelogramo: "))
    altura = float(input("Ingrese la altura del paralelogramo: "))
    area = base * altura
    print("El área del paralelogramo es:", area)
elif opcion == 4:
    diagonal_mayor = float(input("Ingrese la longitud de la diagonal mayor del rombo: "))
    diagonal_menor = float(input("Ingrese la longitud de la diagonal menor del rombo: "))
    area = (diagonal_mayor * diagonal_menor) / 2
    print("El área del rombo es:", area)
elif opcion == 5:
    base_mayor = float(input("Ingrese la base mayor del trapecio: "))
    base_menor = float(input("Ingrese la base menor del trapecio: "))
    altura = float(input("Ingrese la altura del trapecio: "))
    area = ((base_mayor + base_menor) * altura) / 2
    print("El área del trapecio es:", area)
elif opcion == 6:
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = (base * altura) / 2
    print("El área del triángulo es:", area)
elif opcion == 7:
    lado = float(input("Ingrese el lado del triángulo equilátero: "))
    area = (lado ** 2 )*(3 ** 0.5)/4
    print("El área del triángulo equilátero es:", area)
elif opcion == 8:
    base = float(input("Ingrese la base del triángulo rectángulo: "))
    altura = float(input("Ingrese la altura del triángulo rectángulo: "))
    area = (base * altura) / 2
    print("El área del triángulo rectángulo es:", area)
elif opcion == 9:
    perimetro = float(input("Ingrese el perímetro del polígono regular: "))
    apotema = float(input("Ingrese la apotema del polígono regular: "))
    area = (perimetro * apotema) / 2
    print("El área del polígono regular es:", area)
else:
        print("Opción no válida")

print("El resultado de la area es:", area)
