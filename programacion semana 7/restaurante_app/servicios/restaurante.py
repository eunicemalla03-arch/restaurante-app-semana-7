class Restaurante:
    """
    Clase de servicio encargada de administrar
    productos y clientes.
    """

    def __init__(self):
        self.productos = []
        self.clientes = []

    # ===============================
    # PRODUCTOS
    # ===============================

    def registrar_producto(self, producto):
        self.productos.append(producto)

    def listar_productos(self):
        return self.productos

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    # ===============================
    # CLIENTES
    # ===============================

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        return self.clientes

    def buscar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None