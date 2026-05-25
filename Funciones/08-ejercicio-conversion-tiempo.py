def a_segundos(cantidad, unidad):
    if unidad == 'segundo':
        return cantidad
    elif unidad == 'minuto':
        return cantidad * 60
    elif unidad == 'hora':
        return cantidad * 3600
    elif unidad == 'dia':
        return cantidad * 86400
    elif unidad == 'mes':
        return cantidad * 2592000
    elif unidad == 'año':
        return cantidad * 31536000
    else:
        return "Error opcion no valida "


def de_segundos(cantidad, unidad):
    if unidad == 'segundo':
        return cantidad
    elif unidad == 'minuto':
        return cantidad / 60
    elif unidad == 'hora':
        return cantidad / 3600
    elif unidad == 'dia':
        return cantidad / 86400
    elif unidad == 'mes':
        return cantidad / 2592000
    elif unidad == 'año':
        return cantidad / 31536000
    else:
        return "Error opcion no valida "


def convertir_tiempo(cantidad, unidad_origen, unidad_destino):
    cantidad_en_segundos = a_segundos(cantidad, unidad_origen)
    if cantidad_en_segundos == "Error":
        return "Unidad de tiempo no válida"
    cantidad_convertida = de_segundos(cantidad_en_segundos, unidad_destino)
    return f"{cantidad} {unidad_origen}(s) son {cantidad_convertida} {unidad_destino}(s)"


# Ejemplo de uso
print(convertir_tiempo(2, 'hora', 'minuto'))
