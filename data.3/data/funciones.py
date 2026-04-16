import json
import os
from datetime import datetime


"data/inventario.json"
"data/historial.json"
"data/bodega.json"
def cargarDatos():
    if os.path.exists("data/inventario.json"):
        with open("data/inventario.json", "r") as f:
            return json.load(f)
    if os.path.exists("data/bodega.json"):
            with open("data/bodega.json", "r") as f:
                return json.load(f)
    return []

def guardarDatos(datos):
    with open("data/inventario.json", "w") as f:
        json.dump(datos, f, indent=4)
    with open("data/bodega.json", "w") as f:
        json.dump(datos, f, indent=4)

def cargarHistorial():
    if os.path.exists("data/historial.json"):
        with open("data/historial.json", "r") as f:
            return json.load(f)
    return []

def guardarHistorial(historial):
    with open("data/historial.json", "w") as f:
        json.dump(historial, f, indent=4)
def buscarProducto(datos, codigo):
    for producto in datos:
        if producto["codigo"] == codigo:
            return producto
    return None
def fecha():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def registrarProducto(datos):
    codigo = input("Código: ")

    if buscarProducto(datos, codigo):
        print("Ya existe")
        return

    nombre = input("Nombre: ")
    proveedor = input("Proveedor: ")

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "proveedor": proveedor,
        "bodegas": {"norte": 0, "centro": 0, "oriente": 0}
    }

    

    datos.append(producto)
    guardarDatos(datos)
    print("Producto registrado")


def ingresarProducto(datos):
    codigo = input("Código: ")https://github.com/Thejos11/examen/upload/main
    producto = buscarProducto(datos, codigo)

    if not producto:
        print("No existe")
        return

    bodega = input("Bodega: ").lower()

    if bodega not in ["norte", "centro", "oriente"]:
        print("Bodega inválida")
        return

    cantidad = input("Cantidad: ")

    if not cantidad.isdigit():
        print("Cantidad inválida")
        return

    cantidad = int(cantidad)
    descripcion = input("Descripción: ")

    producto["bodegas"][bodega] += cantidad
    guardarDatos(datos)

    movimiento = {
        "codigo": codigo,
        "tipo": "entrada",
        "bodega": bodega,
        "cantidad": cantidad,
        "descripcion": descripcion,
        "fecha": fecha()
    }

    historial = cargarHistorial()
    historial.append(movimiento)
    guardarHistorial(historial)

    print("Ingreso realizado")

def sacarProducto(datos):
    codigo = input("Código: ")
    producto = buscarProducto(datos, codigo)

    if not producto:
        print("No existe")
        return

    bodega = input("Bodega: ").lower()

    if bodega not in ["norte", "centro", "oriente"]:
        print("Bodega inválida")
        return

    cantidad = input("Cantidad: ")

    if not cantidad.isdigit():
        print("Cantidad inválida")
        return

    cantidad = int(cantidad)

    if producto["bodegas"][bodega] < cantidad:
        print("No hay suficiente")
        return

    descripcion = input("Descripción: ")

    producto["bodegas"][bodega] -= cantidad
    guardarDatos(datos)

    movimiento = {
        "codigo": codigo,
        "tipo": "salida",
        "bodega": bodega,
        "cantidad": cantidad,
        "descripcion": descripcion,
        "fecha": fecha()
    }

    historial = cargarHistorial()
    historial.append(movimiento)
    guardarHistorial(historial)

    print("Salida realizada")

def buscar(datos):
    codigo = input("Código: ")
    producto = buscarProducto(datos, codigo)

    if not producto:
        print("No existe")
        return

    print("Nombre:", producto["nombre"])
    print("Proveedor:", producto["proveedor"])
    print("Bodegas:", producto["bodegas"])

def historial(datos):
    codigo = input("Código: ")

    lista_historial = cargarHistorial()

    for movimiento in lista_historial:
        if movimiento["codigo"] == codigo:
            print("=================")

            for clave,valor in movimiento.items():
                print(clave,":",valor)



def reporte(datos):

    for producto in datos:
        total = sum(producto["bodegas"].values())
        print(producto["nombre"], "-", total)

    guardar = input("¿Guardar reporte? (si/no): ")

    if guardar.lower() == "si":
        with open("reporte.txt", "w") as f:
            for producto in datos:
                total = sum(producto["bodegas"].values())
                f.write(f"{producto['nombre']} - Total: {total}")
def transferenciaProducto(datos):
    codigo = input("Código: ")
    producto = transferenciaProducto(datos, codigo)
    if not producto:
        print("No existe")
        return

    bodega = input("Bodega: ").lower()

    if bodega not in ["norte", "centro", "oriente"]:
        print("Bodega inválida")
        return

    cantidad = input("Cantidad: ")

    if not cantidad.isdigit():
        print("Cantidad inválida")
        return

    cantidad = int(cantidad)
    descripcion = input("Descripción: ")

    producto["bodegas"][bodega] += cantidad
    guardarDatos(datos)

    movimiento = {
        "codigo": codigo,
        "tipo": "entrada",
        "bodega": bodega,
        "cantidad": cantidad,
        "descripcion": descripcion,
        "fecha": fecha()
    }

    historial = cargarHistorial()
    historial.append(movimiento)
    guardarHistorial(historial)

    print("Ingreso realizado")


    
    