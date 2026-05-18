def descuento(total_cuenta, porce_descuento):
    descuento = total_cuenta * (porce_descuento/100)
    cuenta_total = total_cuenta - descuento
    return cuenta_total


# Ejemplo de uso
total_cuenta = 10000
porce_descuento = 20
total_final = descuento(total_cuenta, porce_descuento)
print(f"El total después del descuento es: {total_final}")
