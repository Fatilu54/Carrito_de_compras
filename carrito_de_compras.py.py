import os
codigo=0

productos = {
    "2001": {"codigo": "2001", "nombre": "Pincel", "marca": "CBX", "precio": 599.99, "color": "Azul", "stock": 50, "caracteristicas": "Son de trazo fino"},
    "2002": {"codigo": "2002", "nombre": "Acrilicos", "marca": "EQ", "precio": 399.99, "color": "negro", "stock": 30, "caracteristicas": "240ml"},
    "2003": {"codigo": "2003", "nombre": "Bastidor", "marca": "Canvas Paint", "precio": 3099.99, "color": "blanco", "stock": 20, "caracteristicas": "Es de 30x30"},
    "2004": {"codigo": "2004", "nombre": "Atril de madera", "marca": "Turk", "precio": 4849.99, "color": "Marron", "stock": 7, "caracteristicas": "Altura 130m"}
}

carrito = []


def mostrar_productos_detalle(productos):
    os.system("cls")
    print("-------- PRODUCTOS DISPONIBLES --------")
    print("\n")
    for codigo, producto in productos.items():
        print("Código:", producto["codigo"])
        print("Nombre:", producto["nombre"])
        print("Marca:", producto["marca"])
        print("Precio:", producto["precio"])
        print("Color:", producto["color"])
        print("Stock:", producto["stock"])
        print("Características:", producto["caracteristicas"])
        print("-----------------------------")


def mostrar_informacion_breve(productos):
    os.system("cls")
    print("-------- INFORMACIÓN BREVE DE LOS PRODUCTOS --------")
    for codigo, producto in productos.items():
        print("Código:", producto["codigo"])
        print("Nombre:", producto["nombre"])
        print("Precio:", producto["precio"])
        print("Stock disponible:", producto["stock"])
        print("-----------------------------")


def buscar_producto_codigo(codigo, productos):
    os.system("cls")
    codigo = input("Ingresa el código del producto: ")
    if codigo in productos:
        producto = productos[codigo]
        print("-------- INFORMACIÓN DEL PRODUCTO --------")
        print("Código:", producto["codigo"])
        print("Nombre:", producto["nombre"])
        print("Marca:", producto["marca"])
        print("Precio:", producto["precio"])
        print("Stock:", producto["stock"])
        print("Color:", producto["color"])
        print("Características:", producto["caracteristicas"])
        print("-----------------------------")
    else:
        print("El código ingresado no pertenece a ningún producto disponible.")


def comprar_producto(productos, carrito):
    os.system("cls")
    while True:
        codigo = input("Ingresar el código del producto a comprar: ")
        if codigo not in productos:
            print("El código ingresado no corresponde a ningún producto.")
            continuar = input("¿Desea comprar otro producto? (SI/NO): ")
            if continuar.lower() == "no":
                break
            else:
                continue

        producto = productos[codigo]
        print("------- DETALLE DEL PRODUCTO --------")
        print("Nombre:", producto["nombre"])
        print("Precio:", producto["precio"])
        print("Stock disponible:", producto["stock"])
        cantidad = int(input("Ingresa la cantidad a comprar: "))
        if cantidad > producto["stock"]:
            print("La cantidad ingresada supera el stock disponible. ")
            continuar = input("¿Desea comprar otro producto? (SI/NO):")
            if continuar.lower() == "no":
                break
            else:
                continue

        costo_total = round(producto["precio"] * cantidad, 2)
        item = {
            "nombre": producto["nombre"],
            "cantidad": cantidad,
            "precio_unitario": producto["precio"],
            "costo_total": costo_total
        }

        carrito.append(item)
        producto["stock"] -= cantidad
        print("Producto añadido al carrito.")
        continuar = input("¿Desea comprar otro producto? (SI/NO)")
        if continuar.lower() == "no":
            break
        else:
            continue


def mostrar_carrito(carrito):
    if len(carrito) > 0:
  
        os.system("cls")
        total_a_pagar = 0
        print("-------- PRODUCTOS EN EL CARRITO --------")
        for producto in carrito:
            nombre = producto["nombre"]
            cantidad = producto["cantidad"]
            precio_unitario = producto["precio_unitario"]
            costo_total = producto["costo_total"]

            print("Nombre: ", nombre)
            print("Cantidad comprada: ", cantidad)
            print("Precio unitario: ", precio_unitario)
            print("Costo total: ", costo_total)
            print("----------------------------------------")

            total_a_pagar += costo_total

        print("Total a pagar: ", total_a_pagar)
        
        print("\n")
    else:
        print("El carrito esta vacio.")
    


def modificar_carrito(carrito):
    os.system("cls")
    print("-------- MODIFICAR CARRITO DE COMPRAS --------")
    for i, item in enumerate(carrito):
        print(i + 1, item["nombre"])
    opcion = int(input("Selecciona el número del producto a modificar (0 para cancelar): "))
    if opcion == 0:
        return

    if opcion < 1 or opcion > len(carrito):
        print("Opción inválida.")
        return


    item = carrito[opcion - 1]
    print("Producto seleccionado:", item["nombre"])
    print("Cantidad actual:", item["cantidad"])
    nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
    if nueva_cantidad < 0:
        print("La cantidad no puede ser negativa.")
        return

    item["cantidad"] = nueva_cantidad
    item["costo_total"] = round(item["precio_unitario"] * nueva_cantidad, 2)
    print("Producto modificado en el carrito.")
    print("\n")
    print("¿Desea modificar algún otro producto?")


def finalizar_compra(carrito):
    os.system("cls")
    print("-------- DETALLE DE LA COMPRA --------")
    mostrar_carrito(carrito)


salir = False


while not salir:
    print("-------- MENÚ --------")
    print("\n")
    print("1) Ver los Productos")
    print("2) Mostrar breve información de los productos")
    print("3) Buscar productos")
    print("4) Comprar productos")
    print("5) Mostrar carrito")
    print("6) Salir")



    opcion = input("Seleccione una opción: ")



    if opcion == "1":
        print()
        mostrar_productos_detalle(productos)
    elif opcion == "2":
        mostrar_informacion_breve(productos)
    elif opcion == "3":
        buscar_producto_codigo(codigo, productos)
    elif opcion == "4":
        comprar_producto(productos, carrito)
    elif opcion == "5":
        mostrar_carrito(carrito)
        modificar = input("¿Desea modificar el carrito? (SI/NO): ")
        if modificar.lower() == "si":
            modificar_carrito(carrito)
        finalizar_compra(carrito)
        break
    elif opcion == "6":
        print("Gracias por su visita. Que tenga un lindo día.")
        salir = True
    else:
        print("Opción inválida. Inténtalo nuevamente.")
