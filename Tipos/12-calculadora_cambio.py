Valor_producto = float(input("Ingrese valor del producto:  "))
Monto_pagado = float(input("Efectivo Recibido:  "))

Vuelto = Monto_pagado - Valor_producto
Vuelto = int(Vuelto)

salida = f"""
El vuelto a devolver es: {Vuelto} pesos
"""
print(salida)
