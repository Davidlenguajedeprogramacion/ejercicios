edad = int(input("Introduce tu edad: "))
ingresos = float(input("Introduce tus ingresos mensuales: "))

if edad > 18 and ingresos >= 3000:
    print("Debes tributar.")
else:
    print("No debes tributar.")
