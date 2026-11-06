def crear_cola():
    return []

def encolar(cola, dato):
    cola.append(dato)

def desencolar(cola):
    return cola.pop(0) if cola else None

def esta_vacia(cola):
    return len(cola) == 0

