## operadores Logicos
##and or not
num1 = 36
num2 = 72/2
num3 = 48

mi_bool = num1 >num2 and num1<num3

num1 = 36
num2 = 72/2
num3 = 48

mi_bool = num1 >num2 or num1<num3

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool = (palabra1 not in frase) and (palabra2  not in frase)

num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))
if(num1 > num2):
    print(f"{num1} es mayor que {num2}")
elif(num2 > num1):
    print(f"{num2} es mayor que {num1}")
elif(num1 == num2):
    print(f"{num1} y {num2} son iguales")


## loops bucles
nombre_lista= ["alex","axel","georgy","camilo","herrera"]
for elemento in nombre_lista:
    print("Hola" + elemento)

palabra = "aprendiendo nuevo lenguaje de programación"

for letra in palabra:
    print(letra)



lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if(numero % 2 == 0):
        suma_pares+=numero
    else:
        suma_impares+=numero

print(suma_impares,suma_pares)

## loops while
condicion = 0

while condicion <=3:
    print("funciona")
    condicion += 1
else: print("Fin del while")
##pass  pasar
##break romper el loop
##continue continuar el loop

numero = 10

while numero >= 0:
    print(numero)
    numero -= 1


numero = 50

while numero >= 0:
    if(numero % 5 == 0):
        print(numero)
    numero -= 1

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if(numero >= 0):
        print(numero)
    else:
        break


### Rango for con indicadores

for numero in range(5):
    print(numero)