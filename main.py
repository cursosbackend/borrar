import pandas as pd
import os




# Cargar CSV o crear DataFrame vacío
archivo_csv = "productos.csv"
if os.path.exists(archivo_csv):
    productos = pd.read_csv(archivo_csv)
else:
    productos = pd.DataFrame(columns=["id", "nombre", "precio", "cantidad"])


while True:
    print("\n📦 MENÚ CRUD PRODUCTOS")
    print("1. Crear producto")
    print("2. Leer productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Selecciona una opción (1-5): ")




    if opcion == "1":
        nuevo_id = int(input("ID del producto: "))
        if nuevo_id in productos["id"].values:
            print("Ese ID ya existe.")
            continue
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))

        
        nuevo = pd.DataFrame([[nuevo_id, nombre, precio, cantidad]], columns=productos.columns)
        productos = pd.concat([productos, nuevo], ignore_index=True)
        productos.to_csv(archivo_csv, index=False)
        print("Producto agregado correctamente.")


    elif opcion == "2":
        if productos.empty:
            print("No hay productos registrados.")
        else:
            print(productos)

    elif opcion == "3":
        producto_id = int(input("ID del producto a actualizar: "))
        if producto_id not in productos["id"].values:
            print("Producto no encontrado.")
            continue
        idx = productos[productos["id"] == producto_id].index[0]

        nuevo_nombre = input(f"Nuevo nombre ({productos.at[idx, 'nombre']}): ") or productos.at[idx, 'nombre']
        nuevo_precio = input(f"Nuevo precio ({productos.at[idx, 'precio']}): ") or productos.at[idx, 'precio']
        nueva_cantidad = input(f"Nueva cantidad ({productos.at[idx, 'cantidad']}): ") or productos.at[idx, 'cantidad']

        productos.at[idx, 'nombre'] = nuevo_nombre
        productos.at[idx, 'precio'] = float(nuevo_precio)
        productos.at[idx, 'cantidad'] = int(nueva_cantidad)
        productos.to_csv(archivo_csv, index=False)
        print("Producto actualizado correctamente.")

    elif opcion == "4":
        producto_id = int(input("ID del producto a eliminar: "))
        if producto_id in productos["id"].values:
            productos = productos[productos["id"] != producto_id]
            productos.to_csv(archivo_csv, index=False)
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida.")
    



    
