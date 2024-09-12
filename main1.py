precio_por_barra = 2.5
descuento = 0.6

barras_vendidas = int(input("Introduce el número de barras no frescas vendidas: "))

precio_sin_descuento = barras_vendidas * precio_por_barra
precio_con_descuento = precio_sin_descuento * (1 - descuento)

print(f"Precio habitual: {precio_sin_descuento:.2f}€")
print(f"Descuento: {precio_sin_descuento * descuento:.2f}€")
print(f"Coste final: {precio_con_descuento:.2f}€")
