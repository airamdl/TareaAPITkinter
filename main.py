import json
from tkinter import Tk, Frame

import requests
from dataclass_wizard import fromdict

from model.api_response import APIResponse

response = requests.get("https://dummyjson.com/products")
print(response.status_code)

data_product = response.json()


Product_list = fromdict(APIResponse, data_product)

for product in Product_list.products:
    print(product.title)





