def crear_lista():
    return {"cabeza": None, "cola": None, "actual": None, "tamaño": 0}

def insertar_final(lista, dato):
    nodo = {"dato": dato, "ant": lista["cola"], "sig": None}
    if lista["cola"] is None:
        lista["cabeza"] = nodo
        lista["actual"] = nodo
    else:
        lista["cola"]["sig"] = nodo
    lista["cola"] = nodo 
    lista["tamaño"] += 1
    return nodo

def eliminar(lista, nodo):
    if nodo ["ant"]:
        nodo["ant"]["sig"] = nodo["sig"]
    else:
        lista["cabeza"] = nodo["sig"]
    if nodo["sig"]:
        nodo["sig"]["ant"] = nodo["ant"]
    else:
        lista["cola"] = nodo["ant"]
    if lista["actual"] is nodo:
        lista ["actual"] = nodo["sig"] or nodo["ant"]
    lista["tamaño"] -= 1

def avanzar(lista):
    if lista["actual"] and lista["actual"]["sig"]:
        lista["actual"] = lista["actual"]["sig"]
    return lista["actual"]

def a_lista(lista):
    datos, nodo = [], lista["cabeza"]
    while nodo:
        datos.append(nodo["dato"])
        nodo = nodo["sig"]
    return datos

