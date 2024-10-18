from dataclasses import dataclass
from typing import List

from model.product import Product


@dataclass
class APIResponse:
    products : List[Product]
    total: int
    skip : int
    limit : int