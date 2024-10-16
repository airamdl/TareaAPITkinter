from dataclasses import dataclass

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
    tags : [str]
    brand : str
    sku : str
    weight : float
    dimensions : Dimensions
    warrantyInformation : str
    shippingInformation : str
    availabilityStatus : str
    reviews: [Review]
    returnPolicy: str
    minimumOrderQuantity : int
    meta : Meta
    images : [str]
    thumbnail : str


