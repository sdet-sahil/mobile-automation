
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Product:
    name: str
    price: Decimal
    description: str = ""
    quantity: int = 1
