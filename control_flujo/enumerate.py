##enumerete- enumerador

lista = ["a","b","c","d","e"]

for item in enumerate(lista):
    print(item)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

lista_indices = list(enumerate("Python"))
print(lista_indices)


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if(nombre[0] == "M"):
         print(indice,nombre)