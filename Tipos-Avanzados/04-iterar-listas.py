mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito Feliz"]

for mascota in mascotas:
    print(mascota)


for mascota in enumerate(mascotas):
    print(mascota)

for indice,     mascota in enumerate(mascotas):
    print(indice, mascota)
