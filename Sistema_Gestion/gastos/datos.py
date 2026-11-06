#Aqui se marcan las clasificaciones de cada gasto.
from estructuras.cola import crear_cola
from estructuras.pila import crear_pila
from estructuras.lista_doble import crear_lista
categories = ["Comida", "Transporte", "Servicios", "Ocio", "Salud", "Otros"]

contador = {"id": 0}

def crear_gasto(monto, descripcion, fecha, categorias = None):
    contador["id"] += 1
    return {
        "id": contador["id"],
        "monto": monto,
        "descripcion": descripcion,
        "fecha": fecha,
        "categoria": categorias,
}

def crear_estado():
    return {
        "pendientes": crear_cola(),
        "recientes": crear_pila(),
        "gastos": crear_lista(),
    }
