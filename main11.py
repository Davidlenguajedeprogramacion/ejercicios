precio = input("Introduce el precio del producto en euros (por ejemplo, 12.34): ")

euros, centimos = precio.split('.')

print(f"Euros: {euros}")
print(f"Céntimos: {centimos}")
