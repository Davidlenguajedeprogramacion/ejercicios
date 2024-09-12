nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (M/F): ")

if (sexo == 'F' and nombre < 'F') or (sexo == 'M' and nombre > 'O'):
    grupo = 'A'
else:
    grupo = 'B'

print(f"Tu grupo es {grupo}")
