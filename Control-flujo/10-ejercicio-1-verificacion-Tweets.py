tweet = input("Ingrese tweet: ")

# largo = len(tweet)
# print(largo)

if len(tweet) > 20:
    print("Ha sobrepasado el límite de su publicación")
elif not tweet:
    print("No se puede publicar un tweet vacío.")
else:
    print("Su tweet a sigo publicado.")
