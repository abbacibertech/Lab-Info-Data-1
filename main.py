import json
import os
import platform
import re
import datetime
import uuid

# limpiar la pantalla
def limpiar_pantalla():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# validar tipo de producto
def validar_tipo_producto(tipo):
    tipos_validos = ["electronico", "alimenticio"]
    return tipo.lower() in tipos_validos

# validar formato de fecha
def validar_fecha(fecha):
    try:
        datetime.datetime.strptime(fecha, '%d/%m/%Y')
        return True
    except ValueError:
        return False

# validar formato de precio
def validar_precio(precio):
    try:
        precio = float(precio)
        return precio > 0
    except ValueError:
        return False

# validar formato de cantidad
def validar_cantidad(cantidad):
    try:
        cantidad = int(cantidad)
        return cantidad >= 0
    except ValueError:
        return False

# Clase inicial
class Producto:
    def __init__(self, nombre, precio, cantidad, fecha_vencimiento, garantia):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.fecha_vencimiento = fecha_vencimiento
        self.garantia = garantia

    def __repr__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}, Vencimiento: {self.fecha_vencimiento}, Garantía: {self.garantia}"

# Clase derivada
class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_vencimiento, garantia, marca, modelo):
        super().__init__(nombre, precio, cantidad, fecha_vencimiento, garantia)
        self.marca = marca
        self.modelo = modelo

# Clase derivada
class ProductoAlimenticio(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_vencimiento, garantia, tipo_alimento):
        super().__init__(nombre, precio, cantidad, fecha_vencimiento, garantia)
        self.tipo_alimento = tipo_alimento

def cargar_datos():
    try:
        with open("inventario.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_datos(datos):
    with open("inventario.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

def agregar_producto(productos):
    nombre = input("Nombre del producto: ")
    precio = input("Precio: ")
    while not validar_precio(precio):
        precio = input("Precio inválido. Ingrese un valor numérico positivo: ")
    cantidad = input("Cantidad: ")
    while not validar_cantidad(cantidad):
        cantidad = input("Cantidad inválida. Ingrese un número entero no negativo: ")
    fecha_vencimiento = input("Fecha de vencimiento (dd/mm/aaaa): ")
    while not validar_fecha(fecha_vencimiento):
        fecha_vencimiento = input("Fecha inválida. Ingrese la fecha en formato dd/mm/aaaa: ")
    garantia = input("Garantía (meses): ")
    tipo = input("Tipo de producto (electronico/alimenticio): ")
    while not validar_tipo_producto(tipo):
        tipo = input("Tipo de producto inválido. Ingrese 'electronico' o 'alimenticio': ")

    if tipo == "electronico":
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        producto = ProductoElectronico(nombre, float(precio), int(cantidad), fecha_vencimiento, int(garantia), marca, modelo)
    else:
        tipo_alimento = input("Tipo de alimento: ")
        producto = ProductoAlimenticio(nombre, float(precio), int(cantidad), fecha_vencimiento, int(garantia), tipo_alimento)

    productos.append(producto.__dict__)
    guardar_datos(productos)
    print("Producto agregado exitosamente.")

def listar_productos(productos):
    if not productos:
        print("No hay productos en el inventario.")
    else:
        for producto in productos:
            print(f"ID: {producto['id']}, {producto['nombre']}")

def modificar_producto(productos):
    id_producto = input("Ingrese el ID del producto a modificar: ")
    for producto in productos:
        if producto['id'] == id_producto:
            # Implementar lógica para modificar los atributos del producto
            print("Producto encontrado. Implementa la lógica para modificar los atributos.")
            return
    print("Producto no encontrado.")

def eliminar_producto(productos):
    id_producto = input("Ingrese el ID del producto a eliminar: ")
    productos[:] = [producto for producto in productos if producto['id'] != id_producto]
    guardar_datos(productos)
    print("Producto eliminado exitosamente.")

# Mostrar menu
def menu():
    productos = cargar_datos()
    while True:
        # limpiar_pantalla()
        print("Menú de Inventario")
        print("1. Agregar producto")
        print("2. Lista de productos")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_producto(productos)
        elif opcion == '2':
            listar_productos(productos)
        elif opcion == '3':
            modificar_producto(productos)
        elif opcion == '4':
            eliminar_producto(productos)
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
