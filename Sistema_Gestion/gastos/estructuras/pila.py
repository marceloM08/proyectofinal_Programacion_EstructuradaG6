def crear_pila():
    return []

def apilar(pila, dato):
    pila.append(dato)

def desapilar(pila):
    return pila.pop() if pila else None

def ver_tope(pila):
    return pila[-1] if pila else None

def esta_vacia(pila):
    return len(pila) == 0 