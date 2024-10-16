from dataclasses import dataclass


@dataclass
class Dimensions:
    width: int
    height: int
    depth: int

@dataclass
class Meta:
    createdAt : str
    updatedAt : str
    barcode : str
    qrCode : str

@dataclass
class Review:
    rating : int
    comment : str
    date : str
    reviewerName : str
    reviewerEmail : str



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

