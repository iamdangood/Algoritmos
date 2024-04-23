monto_cuenta = float(input("Ingrese el monto de la cuenta: "))

if monto_cuenta < 150000:
    print("Se recomienda pagar en efectivo.")
elif 150000 <= monto_cuenta <= 300000:
    print("Se recomienda pagar con celular (dinero electrónico).")
elif 300000 < monto_cuenta <= 600000:
    print("Se recomienda pagar con tarjeta de débito.")
else:
    print("Se recomienda pagar con tarjeta de crédito.")
