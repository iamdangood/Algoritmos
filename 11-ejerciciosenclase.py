Tamaño = """
(1) - opcion 1 $15.000
(2) - opcion 2 $24.000
(2) - opcion 3 $35.000
"""

tamaño = int(input("Seleccione el tamaño de la pizza que desea pedir (1, 2 o 3): "))

ingredientes_adicionales = int(input("Ingrese el número de ingredientes adicionales: "))

if tamaño == 1:
    precio = 15000
elif tamaño == 2:
    precio = 24000
elif tamaño == 3:
    precio = 36000
else:
    print("Opción inválida.")
    exit()

precio_total = precio +ingredientes_adicionales*4000
print("El precio a pagar es: $", precio_total)