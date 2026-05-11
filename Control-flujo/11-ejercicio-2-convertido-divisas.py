print("Bienvenido al conversor de divisas")
cantidad = float(input("Ingrese la cantidad a convertir: "))
divisa_origen = input("Ingresa la divisa de origen (USD, EUR O MXN): ").upper()

if divisa_origen not in ["USD", "EUR", "MXN"]:
    print("Divisa origen no valida.")
    exit()

tasa_usd_a_eur = 0.95
tasa_usd_a_mxn = 20.28
tasa_eur_a_mxn = 21.36

divisa_destino = 0

if divisa_origen == "USD":
    cantidad_euros = cantidad * tasa_usd_a_eur
    cantidad_pesos = cantidad * tasa_usd_a_mxn
