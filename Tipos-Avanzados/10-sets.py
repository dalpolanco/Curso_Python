# set significa grupo o conjunto

primer = {1, 1, 2, 2, 3, 4}
# print(primer)

# primer.add(5)
# print(primer)

# primer.remove(1)
# print(primer)

segundo = [3, 4, 5]
segundo = set(segundo)

# print(primer | segundo)  #operador de union

# print(primer & segundo)  # operardor intersección

# print(primer - segundo)  # operador de diferencia

print(primer ^ segundo)  # operador diferencia simetrica


if 5 in segundo:
    print("Hola Mundo")
