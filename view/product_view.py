import tkinter as tk
from tkinter import ttk, Label
import requests
from PIL import ImageTk, Image
from main import product
from main import Product_list


root = tk.Tk()
root.title("Tkinter API layout")
root.maxsize(1100, 800)
root.config(bg="skyblue")

current_index = 0


print(product)
def show_description():
    description = "Descripción: "
    description += product.description
    ttk.Label(right_frame, text=description).grid(row=0, column=0, padx=5, pady=5)


def show_price():
    price = "Precio: " + str(product.price)
    ttk.Label(right_frame, text=price).grid(row=1, column=0, padx=5, pady=5)

def show_stock():
    stock = "Stock: " + str(product.stock)
    ttk.Label(right_frame, text=stock).grid(row=2, column=0, padx=5, pady=5)

# def show_shipping():
#     shipping = "La informacion de envio" + str(product.shippingInformation)
#     ttk.Label(right_frame, text=shipping).grid(row=3, column=0, padx=5, pady=5)


def show_ship_info():
    show_ship_information = "La informacion de envio es : " + str(product.shippingInformation)
    ttk.Label(right_frame, text=show_ship_information).grid(row=3, column=0, padx=5, pady=5)

def show_all():
    text = f"ID: {product.id}\n" \
               f"Title: {product.title}\n" \
               f"Description: {product.description}\n" \
               f"Category: {product.category}\n" \
               f"Price: {product.price}\n" \
               f"Discount Percentage: {product.discountPercentage}\n" \
               f"Rating: {product.rating}\n" \
               f"Stock: {product.stock}\n" \
               f"Tags: {', '.join(product.tags)}\n" \
               f"SKU: {product.sku}\n" \
               f"Weight: {product.weight}\n" \
               f"Dimensions (WxHxD): {product.dimensions.width}x{product.dimensions.height}x{product.dimensions.depth}\n" \
               f"Warranty Information: {product.warrantyInformation}\n" \
               f"Shipping Information: {product.shippingInformation}\n" \
               f"Availability Status: {product.availabilityStatus}\n" \
               f"Return Policy: {product.returnPolicy}\n" \
               f"Minimum Order Quantity: {product.minimumOrderQuantity}\n"

    ttk.Label(right_frame, text=text).grid(row=4, column=0, padx=5, pady=5)


def show_reviews():
    for review in product.reviews:
        review = product.reviews
    ttk.Label(right_frame, text=review).grid(row=5, column=0, padx=5, pady=5)

def destroy_all():
    global right_frame
    for element in right_frame.winfo_children():
        element.destroy()
    right_frame.config(width=5,height=5)
    ttk.Label(right_frame, ).grid(row=0, column=0, padx=5, pady=5)




def show_product(index):
    global current_index
    current_index = index
    product.show_product(index)

def show_previous():
    global current_index
    print(product.current_index)
    if product.current_index > 0:
        product.current_index -= 1
        product.show_product(product.current_index)



def show_next():
    global current_index
    print(product.current_index)
    if product.current_index < len(product.products) - 1:
        product.current_index += 1
        product.show_product(product.current_index)





product_frame = tk.Frame(root, width=300, height=400, bg='grey')
product_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = tk.Frame(root, width=650, height=400, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)

title = product.title
ttk.Label(product_frame, text=title).grid(row=0, column=0, padx=5, pady=5)

r = requests.get(product.thumbnail, stream=True) # Descarga la foto, bloquea el proceso hasta que termina
image = Image.open(r.raw) # Cargo los bits en formato imagen
image_ttk = ImageTk.PhotoImage(image) # Lo convierto a imagen tkinter (para poderse usar en un label por ejemplo)

ttk.Label(product_frame, image=image_ttk).grid(row=1, column=0, padx=5, pady=5)



tool_bar = tk.Frame(product_frame, width=220, height=325)
tool_bar.grid(row=2, column=0, padx=5, pady=5)

ttk.Button(tool_bar, text="Anterior", command=show_previous).grid(row=0, column=0, padx=5, pady=3, ipadx=10)
ttk.Button(tool_bar, text="Siguiente", command=show_next).grid(row=0, column=2, padx=5, pady=3, ipadx=10)


ttk.Button(tool_bar, text="Descripción", command=show_description).grid(row=1, column=1, padx=5, pady=5)


ttk.Button(tool_bar, text="Precio",command=show_price).grid(row=2, column=1, padx=5, pady=5)



ttk.Button(tool_bar, text="Stock",command=show_stock).grid(row=3, column=1, padx=5, pady=5)



ttk.Button(tool_bar, text="Información de envio", command=show_ship_info).grid(row=4, column=1, padx=5, pady=5)



ttk.Button(tool_bar, text="Toda la información", command=show_all).grid(row=5, column=1, padx=5, pady=5)



ttk.Button(tool_bar, text="Reseñas",command=show_reviews).grid(row=6, column=1, padx=5, pady=5)

ttk.Button(tool_bar, text="Limpiar todo",command=destroy_all).grid(row=7, column=1, padx=5, pady=5)

ttk.Label(right_frame,).grid(row=0,column=0, padx=5, pady=5)




root.mainloop()





