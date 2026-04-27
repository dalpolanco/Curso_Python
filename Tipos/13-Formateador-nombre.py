Primer_Nombre = input("Ingrese primer nombre:  ")
Segundo_Nombre = input("Ingrese segundo nombre:  ")
Apellido_Paterno = input("Ingrese Apellido Paterno:  ")
Apellido_Materno = input("Ingrese Apellido Materno:  ")


Primer_Nombre = Primer_Nombre.strip().capitalize()
Segundo_Nombre = Segundo_Nombre.strip().capitalize()
Apellido_Paterno = Apellido_Paterno.strip().capitalize()
Apellido_Materno = Apellido_Materno.strip().capitalize()

salida = f"""
El nombre ingresado:  {Primer_Nombre} {Segundo_Nombre} {Apellido_Paterno} {Apellido_Materno} 
"""

print(salida)
