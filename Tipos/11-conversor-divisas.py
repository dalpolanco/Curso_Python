Moneda_local = float(input("Ingrese el valor en moneda local:  "))

USD = Moneda_local * 0.050
EUR = Moneda_local * 0.047
GBP = Moneda_local * 0.039
JPY = Moneda_local * 7.71


conversion = f"""
Para el monto en modena local {Moneda_local},
la conversion a USD es: {USD}.
la conversion a EUR es: {EUR}.
la conversion a GBP es: {GBP}.
la conversion a JPY es: {JPY}.
"""

print(conversion)
