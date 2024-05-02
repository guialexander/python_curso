capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinado= list(zip(paises,capitales))

for pais, capital in combinado:
    print(f"La capital de {pais} es {capital}")

numeros = list(["uno / um / one", "dos / dois / two", "tres / três / three","cuatro / quatro / four","cinco / cinco / five"])

print(numeros)