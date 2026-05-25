numeros = [2, 10, 1, 8, 3, 19]

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

numeros2 = sorted(numeros)
print(numeros2)

numeros2 = sorted(numeros, reverse=True)
print(numeros2)


usuarios = [
    [4, "Chanchito"],
    [1, "Felipe"],
    [5, "Pulga"]
]

usuarios.sort()
print(usuarios)


usuarios2 = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]


def ordena(elemento):
    return elemento[1]


usuarios2.sort(key=ordena)
print(usuarios2)

# usuarios2.sort(key=ordena, reverse=True)
# print(usuarios2)

usuarios2.sort(key=lambda el: el[1], reverse=True)
print(usuarios2)

usuarios2.sort(key=lambda el: el[1])
print(usuarios2)
