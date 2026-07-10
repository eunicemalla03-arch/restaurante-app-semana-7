# Sistema Restaurante

## Estudiante

Nombre completo: EUNICE BELEN MALLA CORO

## Descripción

Este proyecto corresponde a un sistema de gestión de restaurante desarrollado en Python utilizando Programación Orientada a Objetos.

El sistema permite registrar, listar y buscar productos y clientes mediante un menú interactivo desde la consola.

## Estructura del proyecto

```
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── cliente.py
│   └── producto.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
└── main.py
```

## Constructor

La clase Producto utiliza el constructor `__init__()` para crear objetos a partir de los datos ingresados por el usuario.

## Uso de @property y @setter

La clase Producto utiliza `@property` y `@setter` para controlar el acceso y la modificación de los atributos.

Se validan:

- Nombre no vacío.
- Categoría no vacía.
- Precio mayor que cero.

## Uso de @dataclass

La clase Cliente utiliza el decorador `@dataclass`, lo que simplifica la creación de objetos y evita escribir código repetitivo.

## Menú interactivo

El sistema permite:

- Registrar productos.
- Listar productos.
- Buscar productos.
- Registrar clientes.
- Listar clientes.
- Buscar clientes.
- Salir del programa.

## Reflexión

La Programación Orientada a Objetos permite representar elementos del mundo real mediante clases y objetos. En este proyecto, los datos ingresados por el usuario se convierten en objetos que luego son administrados por la clase Restaurante, facilitando la organización, reutilización y mantenimiento del código.
