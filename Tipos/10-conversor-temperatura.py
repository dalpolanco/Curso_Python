celsius = float(input("Ingrese temperatura en grados Celsius:  "))

# Celsius = int(n1)

Fahrenheit = (celsius * 9/5) + 32
Kelvin = (celsius + 273.15)

conversion = f"""
Para la tempatura {celsius} grados Celsius,
la conversion a Fahrenheit es: {Fahrenheit}.
la conversion a Kelvin es: {Kelvin}.
"""

print(conversion)
