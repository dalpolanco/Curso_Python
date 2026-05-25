usuarios = [
    [4, "Chanchito"],
    [1, "Felipe"],
    [5, "Pulga"]
]

""" nombres = []
for usuario in usuarios:
    nombres.append(usuario[1])  
print(nombres) """

""" nombres = [usuario[1] for usuario in usuarios]
print(nombres)

# filtrar
menosusuarios = [usuario for usuario in usuarios if usuarios[1] > 2]
print(menosusuarios)
 """

""" nombres = list(map(lambda usuario: usuario[1], usuarios))
print(nombres) """

menosusuarios = list(filter(lambda usuario: usuario[0] > 2, usuarios))
print(menosusuarios)
