from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_menu():
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("----------------------------------------")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("----------------------------------------")
    print("7. Salir")


def main():
    restaurante = Restaurante()

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        # =============================
        # Registrar producto
        # =============================

        if opcion == "1":

            try:
                nombre = input("Nombre del producto: ")
                categoria = input("Categoría: ")
                precio = float(input("Precio: "))

                disponible = input("¿Disponible? (s/n): ").lower()

                disponible = disponible == "s"

                producto = Producto(
                    nombre,
                    categoria,
                    precio,
                    disponible
                )

                restaurante.registrar_producto(producto)

                print("\nProducto registrado correctamente.")

            except ValueError as error:
                print("Error:", error)

        # =============================
        # Listar productos
        # =============================

        elif opcion == "2":

            productos = restaurante.listar_productos()

            if len(productos) == 0:
                print("\nNo existen productos registrados.")

            else:
                print("\nLISTA DE PRODUCTOS\n")

                for producto in productos:
                    print(producto.mostrar_informacion())
                    print("-" * 35)

        # =============================
        # Buscar producto
        # =============================

        elif opcion == "3":

            nombre = input("Nombre del producto: ")

            producto = restaurante.buscar_producto(nombre)

            if producto:
                print()
                print(producto.mostrar_informacion())
            else:
                print("Producto no encontrado.")

        # =============================
        # Registrar cliente
        # =============================

        elif opcion == "4":

            id_cliente = input("ID del cliente: ")
            nombre = input("Nombre: ")
            correo = input("Correo: ")

            cliente = Cliente(
                id_cliente=id_cliente,
                nombre=nombre,
                correo=correo
            )

            restaurante.registrar_cliente(cliente)

            print("\nCliente registrado correctamente.")

        # =============================
        # Listar clientes
        # =============================

        elif opcion == "5":

            clientes = restaurante.listar_clientes()

            if len(clientes) == 0:
                print("\nNo existen clientes registrados.")

            else:

                print("\nLISTA DE CLIENTES\n")

                for cliente in clientes:
                    print(f"ID: {cliente.id_cliente}")
                    print(f"Nombre: {cliente.nombre}")
                    print(f"Correo: {cliente.correo}")
                    print("-" * 35)

        # =============================
        # Buscar cliente
        # =============================

        elif opcion == "6":

            id_cliente = input("Ingrese el ID: ")

            cliente = restaurante.buscar_cliente(id_cliente)

            if cliente:
                print("\nCliente encontrado")
                print(f"ID: {cliente.id_cliente}")
                print(f"Nombre: {cliente.nombre}")
                print(f"Correo: {cliente.correo}")
            else:
                print("Cliente no encontrado.")

        # =============================
        # Salir
        # =============================

        elif opcion == "7":

            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()