from random import *
print(randint(1, 10))
aleatoreo= random()
aleatoreo= round(uniform(1,100),2)
colors=['azul','rojo','verde','blanco','negro']
aleatoreo = choice(colors)
rango_inicio=1
rango_fin = 100
aleatoreo = round(rango_inicio + (rango_fin - rango_inicio) * random())
print(aleatoreo)

num_list = list(range(5,50,5))
shuffle(num_list)
print(num_list)
