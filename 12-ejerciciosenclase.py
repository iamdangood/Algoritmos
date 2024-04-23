cantidad = int(input("Ingrese la cantidad de artículos: "))
precio_unitario_original = float(input("Ingrese el precio unitario original: "))

if cantidad <= 5:
    descuento = 0
elif cantidad < 10:
    descuento = 0.05  
else:
    descuento = 0.08  


precio_unitario_descuento = precio_unitario_original * (1 - descuento)


precio_total = cantidad * precio_unitario_descuento


print("El precio total a pagar es: $", precio_total)
