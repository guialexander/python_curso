match serie:
    case "N-01":
        print("ingresaste a N-01 ")
    case "N-02":
        print("ingresaste a N-02 ")
    case "N-03":
        print("ingresaste a N-03 ")



cliente = {'nombre': "alex",
           'edad': 45,
           'ocupacion': 'instructor'
           }

pelicula = { 'titulo': 'matrix',
             'ficha_tecnica':{'protagonista': 'keanu reeves',
                              'director':'Lana y Lilly Wachowski'}}

elementos = [cliente,pelicula, 'libro']

for e in elementos:
    match e:
        case {''}

    match objeto:
        case < patron_1 >:
    < accion_1 >
    case < patron_2 >:
< accion_2 >
case < patron_3 >:
< accion_3 >
case
_:
< accion_comodin >