def get_product(**datos):
    print(datos)


get_product(id="ide",
            name="Iphone",
            desc="Esto es una iphone")


def get_product(**datos):
    print(datos["name"], datos["desc"])


get_product(id="ide",
            name="Iphone",
            desc="Esto es una iphone")
