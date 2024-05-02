palabra = 'python'
lista = [letra for letra in palabra]
lista = [n for n in range(0,21,2)  if n * 2 >10] ## con condición
pies = [10,20,30,40,50]
metros = [ p / 3.281 for p in pies]

##for letra in palabra:
  ##  lista.append(letra)

print(lista)
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n**2 for n in valores]


valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [valor for valor in valores if valor%2 == 0]

print(valores_pares)


temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(grados_fahrenheit-32)*(5/9) for grados_fahrenheit in temperatura_fahrenheit]
