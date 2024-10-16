from dataclasses import dataclass

from model.product import Product


@dataclass
class APIResponse:
    products : [Product]
    total: int
    skip : int
    limit : int