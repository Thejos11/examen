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
    print(" Transferencia entre Bodegas ")
    codigo = input("Ingrese el código del producto: ")

    if codigo not in inventario:
        print("Error: El producto no existe.")
        return

    bodegas_validas = ["Norte", "Centro", "Oriente"]
    print(f"Bodegas disponibles: {bodegas_validas}")
    
    origen = input("Bodega de origen: ").capitalize()
    destino = input("Bodega de destino: ").capitalize()

    if origen not in bodegas_validas or destino not in bodegas_validas:
        print("Error: Una o ambas bodegas no son válidas.")
        return
    if origen == destino:
        print("Error: La bodega de origen y destino no pueden ser la misma.")
        return

    try:
        cantidad = int(input("Cantidad a transferir: "))
        if cantidad <= 0:
            print("Error: La cantidad debe ser mayor a cero.")
            return
    except ValueError:
        print("Error: Ingrese un número válido.")
        return

    descripcion = input("Descripción de la transferencia: ")
    stock_origen = inventario[codigo]["bodegas"].get(origen, 0)
    
    if stock_origen >= cantidad:
        id_transferencia = f"TR-{codigo}-{origen[0]}{destino[0]}"
        inventario[codigo]["bodegas"][origen] -= cantidad
        inventario[codigo]["bodegas"][destino] = inventario[codigo]["bodegas"].get(destino, 0) + cantidad

        movimiento_salida = {
            "id": id_transferencia,
            "tipo": "Salida por Transferencia",
            "bodega": origen,
            "cantidad": cantidad,
            "descripcion": f"Hacia {destino}: {descripcion}"
        }
        movimiento_entrada = {
            "id": id_transferencia,
            "tipo": "Entrada por Transferencia",
            "bodega": destino,
            "cantidad": cantidad,
            "descripcion": f"Desde {origen}: {descripcion}"
        }

        historial[codigo].append(movimiento_salida)
        historial[codigo].append(movimiento_entrada)

        print(f"\n¡Éxito! Transferencia {id_transferencia} completada.")
        print(f"Stock actual - {origen}: {inventario[codigo]['bodegas'][origen]} | {destino}: {inventario[codigo]['bodegas'][destino]}")
    else:
        print(f"Error: Stock insuficiente en {origen}. Disponible: {stock_origen}")

    
    
