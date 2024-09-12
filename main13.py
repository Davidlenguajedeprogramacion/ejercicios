productos = input("Introduce los productos de la cesta de la compra separados por comas: ")

for producto in productos.split(','):
    print(producto.strip())
