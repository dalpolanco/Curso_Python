mascotas = ["Wolf", "Pelusa", "Pulga", "Felipe", "Pulga", "Chanchito Feliz"]

mascotas.insert(1, "Melvin")
mascotas.append("Copito")
print(mascotas)

mascotas.remove("Copito")
print(mascotas)

mascotas.pop()
print(mascotas)

mascotas.pop(1)
print(mascotas)


del mascotas[0]
print(mascotas)


mascotas.clear()
print(mascotas)
