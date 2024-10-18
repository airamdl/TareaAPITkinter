from dataclasses import dataclass
from typing import List

from model.dimension import Dimensions
from model.meta import Meta
from model.review import Review

@dataclass
class Product:
    id : str
    title : str
    description : str
    category : str
    price : float
    discountPercentage : float
    rating : float
    stock : int
    tags : List[str]
    sku : str
    weight : float
    dimensions : Dimensions
    warrantyInformation : str
    shippingInformation : str
    availabilityStatus : str
    reviews: List[Review]
    returnPolicy: str
    minimumOrderQuantity : int
    meta : Meta
    images : List[str]
    thumbnail : str
    brand: str = None


