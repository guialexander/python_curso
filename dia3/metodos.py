texto = "Este es el texto de Prueba"
resultado = texto.upper()
resultado = texto.lower()
resultado = texto.split(" ")
#resultado = resultado.join(" ")
resultado =  texto.find("texto")
resultado =  texto.replace("texto","Cambio")

print(resultado)

a = "Aprender"
b = "Python"
c = "En MAyo"
d = "Genial"

e = " ".join([a,b,c,d])

print(e)



nombre = "Carina"
print(len(nombre)) #cantidad de caracteres

###
### Listas -- array

mi_lista = ["r","v","j","a","b","c"]
resultado = mi_lista[0]*9
mi_lista.append("d") # agregar
eliminado = mi_lista.pop(3) # eliminar elemento , si no se pone indice elimina el último
mi_lista.sort() # ordenar no devuelve nada
mi_lista.reverse() # lo ultimo primero

print(mi_lista)
print(eliminado)

## Diccionarios similar objetos
diccionario = {
    'c1': "valor 1",
    'c2': "Valor 2"
}
print(diccionario["c1"])

cliente = {
   'nombre': "Alex",
    'edad': 19,
    'profesion' : "Estudiante"
}

print(cliente.keys())
print(cliente.values())
consulta= (cliente['edad'])
print(consulta)


##Tuples
mi_tuple = (1,2,3,4)
print(type(mi_tuple))
print(mi_tuple.count(1))## cuantas veces esta el número
print(mi_tuple.index(3)) ## indice
lista = list(mi_tuple)
print(type(lista))


## Set
mi_set = set([0,1,2,3,4,5,6])
mi_set2 = {0,1,2,3,4,5,6}
print(mi_set,mi_set2)

print(mi_set.pop())
Práctica
Método
Index()
1

palabra = "ordenador"

print(palabra[4])
Práctica
Método
Index()
2

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

print(frase.index("práctica"))
Práctica
Método
Index()
3

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

print(frase.rindex("práctica"))
Práctica
Sub - Strings
1

frase = "Controlar la complejidad es la esencia de la programación"

print(frase[:9])
Práctica
Sub - Strings
2

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"

print(frase[8::3])
Práctica
Sub - Strings
3

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"

print(frase[::-1])
Práctica
Métodos
de
String
1

frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."

print(frase.upper())
Práctica
Métodos
de
String
2

lista_palabras = ["La", "legibilidad", "cuenta."]

frase = " ".join(lista_palabras)

print(frase)
Práctica
Métodos
de
String
3

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."

print(frase.replace("difícil", "fácil").replace("mala", "buena"))
Práctica
Propiedades
de
Strings
1

palabra = "Repetición"

print(palabra * 15)
Práctica
Propiedades
de
Strings
2

haiku = '''
Tierra mojada
mis recuerdos de viaje,
entre las lluvias
'''

print("agua" not in haiku)
Práctica
Propiedades
de
Strings
3

palabra = "electroencefalografista"

print(len(palabra))
Práctica
Listas
1

mi_lista = ["uno", 2, 3.33, "four", True]
Práctica
Listas
2

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
Práctica
Listas
3

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]

eliminado = frutas.pop(2)
Práctica
Diccionarios
1

mi_dic = {"nombre": "Karen", "apellido": "Jurgens", "edad": 35, "ocupacion": "Periodista"}
Práctica
Diccionarios
2

mi_dict = {"valores_1": {"v1": 3, "v2": 6}, "puntos": {"points1": 9, "points2": [10, 300, 15]}}
print(mi_dict["puntos"]["points2"][1])
Práctica
Diccionarios
3

mi_dic = {"nombre": "Karen", "apellido": "Jurgens", "edad": 35, "ocupacion": "Periodista"}

mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
mi_dic["pais"] = "Colombia"
Práctica
Tuples
1

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

print(mi_tupla.count(2))
Práctica
Tuples
2

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)

mi_lista = list(mi_tupla)
Práctica
Tuples
3

mi_tupla = (1, 2, 3, 4)

a, b, c, d = mi_tupla
Práctica
Sets
1

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)
Práctica
Sets
2

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()
Práctica
Sets
3

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")
Práctica
Booleanos
1

prueba = 1 == 2
Práctica
Booleanos
2

print((17834 / 34) > 87 * 56)
Práctica
Booleanos
3

print(25 ** 0.5 == 5)