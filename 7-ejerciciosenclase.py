conversion= """
    (1) - 1. Fahrenheit a Celsius
    (2) - 2. Fahrenheit a Kelvin
    (3) - 3. Fahrenheit a Rankine
    (4) - 4. Fahrenheit a Réaumur
    (5) - 5. Celsius a Fahrenheit
    (6) - 6. Celsius a Kelvin
    (7) - 7. Celsius a Rankine
    (8) - 8. Celsius a Réaumur
    (9) - 9. Kelvin a Fahrenheit
    (10) - 10. Kelvin a Celsius
    (11) - 11. Kelvin a Rankine
    (12) - 12. Kelvin a Réaumur
    (13) - 13. Rankine a Fahrenheit
    (14) - 14. Rankine a Celsius
    (15) - 15. Rankine a Kelvin
    (16) - 16. Rankine a Réaumur
    (17) - 17. Réaumur a Fahrenheit
    (18) - 18. Réaumur a Celsius
    (19) - 19. Réaumur a Kelvin
    (20) - 20. Réaumur a Rankine
    """
conversion = int(input("Seleccione la conversión de temperatura:"))

temperatura = float(input("Ingrese la temperatura a convertir: "))

if conversion == 1:
        resultado = (temperatura - 32) / 1.8
        unidad_resultado = "Celsius"
elif conversion == 2:
        resultado = (temperatura + 459.67) / 1.8
        unidad_resultado = "Kelvin"
elif conversion == 3:
        resultado = temperatura + 459.67
        unidad_resultado = "Rankine"
elif conversion == 4:
        resultado = (temperatura - 32) / 2.25
        unidad_resultado = "Réaumur"
elif conversion == 5:
        resultado = temperatura * 1.8 + 32
        unidad_resultado = "Fahrenheit"
elif conversion == 6:
        resultado = temperatura + 273.15
        unidad_resultado = "Kelvin"
elif conversion == 7:
        resultado = temperatura * 1.8 + 32 + 459.67
        unidad_resultado = "Rankine"
elif conversion == 8:
        resultado = temperatura * 0.8
        unidad_resultado = "Réaumur"
elif conversion == 9:
        resultado = temperatura * 1.8 - 459.67
        unidad_resultado = "Fahrenheit"
elif conversion == 10:
        resultado = temperatura - 273.15
        unidad_resultado = "Celsius"
elif conversion == 11:
        resultado = temperatura * 1.8
        unidad_resultado = "Rankine"
elif conversion == 12:
        resultado = (temperatura - 273.15) * 0.8
        unidad_resultado = "Réaumur"
elif conversion == 13:
        resultado = temperatura - 459.67
        unidad_resultado = "Fahrenheit"
elif conversion == 14:
        resultado = (temperatura - 32) / 1.8
        unidad_resultado = "Celsius"
elif conversion == 15:
        resultado = temperatura / 1.8
        unidad_resultado = "Kelvin"
elif conversion == 16:
        resultado = (temperatura - 32) / 2.25
        unidad_resultado = "Réaumur"
elif conversion == 17:
        resultado = temperatura * 2.25 + 32
        unidad_resultado = "Fahrenheit"
elif conversion == 18:
        resultado = temperatura * 1.25
        unidad_resultado = "Celsius"
elif conversion == 19:
        resultado = temperatura * 1.25 + 273.15
        unidad_resultado = "Kelvin"
elif conversion == 20:
        resultado = temperatura * 2.25 + 32 + 459.67
        unidad_resultado = "Rankine"
else:
        print("Opción no válida")

print("El resultado de la conversión es:", resultado, unidad_resultado)