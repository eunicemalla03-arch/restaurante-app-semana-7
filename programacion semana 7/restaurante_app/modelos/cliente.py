from dataclasses import dataclass

@dataclass
class Cliente:
    """
    Clase Cliente implementada con @dataclass.
    """

    id_cliente: str
    nombre: str
    correo: str