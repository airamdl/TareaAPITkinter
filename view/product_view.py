import tkinter as tk
from tkinter import ttk, Label
import requests
from PIL import ImageTk, Image
from main import product
from main import Product_list




product.id = 0

print(product.reviews[2].rating)


print(product)
def show_description():
    index = product.id
    description = "Descripción: "
    description += Product_list.products[index].description
    ttk.Label(right_frame, text=description, wraplength=600).grid(row=0, column=0, padx=5, pady=5)


def show_price():
    index = product.id
    price = "Precio: " + str(Product_list.products[index].price)
    ttk.Label(right_frame, text=price).grid(row=1, column=0, padx=5, pady=5)

def show_stock():
    index = product.id
    stock = "Stock: " + str(Product_list.products[index].stock)
    ttk.Label(right_frame, text=stock).grid(row=2, column=0, padx=5, pady=5)

# def show_shipping():
#     shipping = "La informacion de envio" + str(product.shippingInformation)
#     ttk.Label(right_frame, text=shipping).grid(row=3, column=0, padx=5, pady=5)


def show_ship_info():
    index = product.id
    show_ship_information = "La informacion de envio es : " + str(Product_list.products[index].shippingInformation)
    ttk.Label(right_frame, text=show_ship_information).grid(row=3, column=0, padx=5, pady=5)

def show_all():
    index = product.id
    text = f"ID: {Product_list.products[index].id}\n" \
               f"Title: {Product_list.products[index].title}\n" \
               f"Description: {Product_list.products[index].description}\n" \
               f"Category: {Product_list.products[index].category}\n" \
               f"Price: {Product_list.products[index].price}\n" \
               f"Discount Percentage: {Product_list.products[index].discountPercentage}\n" \
               f"Rating: {Product_list.products[index].rating}\n" \
               f"Stock: {Product_list.products[index].stock}\n" \
               f"Tags: {', '.join(Product_list.products[index].tags)}\n" \
               f"SKU: {Product_list.products[index].sku}\n" \
               f"Weight: {Product_list.products[index].weight}\n" \
               f"Dimensions (WxHxD): {Product_list.products[index].dimensions.width}x{Product_list.products[index].dimensions.height}x{Product_list.products[index].dimensions.depth}\n" \
               f"Warranty Information: {Product_list.products[index].warrantyInformation}\n" \
               f"Shipping Information: {Product_list.products[index].shippingInformation}\n" \
               f"Availability Status: {Product_list.products[index].availabilityStatus}\n" \
               f"Return Policy: {Product_list.products[index].returnPolicy}\n" \
               f"Minimum Order Quantity: {Product_list.products[index].minimumOrderQuantity}\n"

    ttk.Label(right_frame, text=text, wraplength=600).grid(row=4, column=0, padx=5, pady=5)


# def show_reviews(index):
#     i=5
#
#     for review in product.reviews:
#
#         review = str( f"  - Rating: {Product_list.products[index].reviews.rating}\n"
#                       f" Comment: {Product_list.products[index].reviews.comment}\n"
#                       f" Date: {Product_list.products[index].reviews.date}\n"
#                       f"Reviewer: {Product_list.products[index].reviews.reviewerName}, Email: {Product_list.products[index].reviewerEmail}")
#         ttk.Label(right_frame, text=review).grid(row=i, column=0, padx=5, pady=5)
#         i+=1

def destroy_all():
    global right_frame
    for element in right_frame.winfo_children():
        element.destroy()
    right_frame.config(width=5,height=5)
    ttk.Label(right_frame, ).grid(row=0, column=0, padx=5, pady=5)




def show_product(index):
    global right_frame

    product_frame = tk.Frame(root, width=300, height=400, bg='grey')
    product_frame.grid(row=0, column=0, padx=10, pady=5)

    right_frame = tk.Frame(root, width=650, height=400, bg='grey')
    right_frame.grid(row=0, column=1, padx=10, pady=5)
    print()
    title = Product_list.products[index].title
    ttk.Label(product_frame, text=title).grid(row=0, column=0, padx=5, pady=5)


    r = requests.get(Product_list.products[index].thumbnail, stream=True) # Descarga la foto, bloquea el proceso hasta que termina

    image = Image.open(r.raw)  # Cargo los bits en formato imagen

    image_ttk = ImageTk.PhotoImage(image)  # Lo convierto a imagen tkinter (para poderse usar en un label por ejemplo)
    print(image_ttk)
    ttk.Label(product_frame, image=image_ttk).grid(row=1, column=0, padx=5, pady=5)

    tool_bar = tk.Frame(product_frame, width=220, height=325)
    tool_bar.grid(row=2, column=0, padx=5, pady=5)

    ttk.Button(tool_bar, text="Anterior", command=show_previous).grid(row=0, column=0, padx=5, pady=3, ipadx=10)
    ttk.Button(tool_bar, text="Siguiente", command=show_next).grid(row=0, column=2, padx=5, pady=3, ipadx=10)

    ttk.Button(tool_bar, text="Descripción", command=show_description).grid(row=1, column=1, padx=5, pady=5)

    ttk.Button(tool_bar, text="Precio", command=show_price).grid(row=2, column=1, padx=5, pady=5)

    ttk.Button(tool_bar, text="Stock", command=show_stock).grid(row=3, column=1, padx=5, pady=5)

    ttk.Button(tool_bar, text="Información de envio", command=show_ship_info).grid(row=4, column=1, padx=5, pady=5)

    ttk.Button(tool_bar, text="Toda la información", command=show_all).grid(row=5, column=1, padx=5, pady=5)

    #ttk.Button(tool_bar, text="Reseñas", command=show_reviews(index)).grid(row=6, column=1, padx=5, pady=5)

    ttk.Button(tool_bar, text="Limpiar todo", command=destroy_all).grid(row=7, column=1, padx=5, pady=5)

    ttk.Label(right_frame, ).grid(row=0, column=0, padx=5, pady=5)


def show_previous():
    if product.id > 0:
        product.id -= 1
        destroy_all()
        show_product(product.id)

    else:
        product.id = len(Product_list.products) - 1
        destroy_all()
        show_product(product.id)



def show_next():
    if product.id < len(Product_list.products) - 1:
        product.id += 1
        destroy_all()
        show_product(product.id)

    else:
        product.id = 0
        destroy_all()
        show_product(product.id)


root = tk.Tk()
root.title("Tkinter API layout")
root.maxsize(1400, 1000)
root.config(bg="skyblue")


show_product(product.id)

# product_frame = tk.Frame(root, width=300, height=400, bg='grey')
# product_frame.grid(row=0, column=0, padx=10, pady=5)
#
# right_frame = tk.Frame(root, width=650, height=400, bg='grey')
# right_frame.grid(row=0, column=1, padx=10, pady=5)
#
# title = product.title
# ttk.Label(product_frame, text=title).grid(row=0, column=0, padx=5, pady=5)
#
# r = requests.get(product.thumbnail, stream=True) # Descarga la foto, bloquea el proceso hasta que termina
# image = Image.open(r.raw) # Cargo los bits en formato imagen
# image_ttk = ImageTk.PhotoImage(image) # Lo convierto a imagen tkinter (para poderse usar en un label por ejemplo)
#
# ttk.Label(product_frame, image=image_ttk).grid(row=1, column=0, padx=5, pady=5)
#
#
#
# tool_bar = tk.Frame(product_frame, width=220, height=325)
# tool_bar.grid(row=2, column=0, padx=5, pady=5)
#
# ttk.Button(tool_bar, text="Anterior", command=show_previous).grid(row=0, column=0, padx=5, pady=3, ipadx=10)
# ttk.Button(tool_bar, text="Siguiente", command=show_next).grid(row=0, column=2, padx=5, pady=3, ipadx=10)
#
#
# ttk.Button(tool_bar, text="Descripción", command=show_description).grid(row=1, column=1, padx=5, pady=5)
#
#
# ttk.Button(tool_bar, text="Precio",command=show_price).grid(row=2, column=1, padx=5, pady=5)
#
#
#
# ttk.Button(tool_bar, text="Stock",command=show_stock).grid(row=3, column=1, padx=5, pady=5)
#
#
#
# ttk.Button(tool_bar, text="Información de envio", command=show_ship_info).grid(row=4, column=1, padx=5, pady=5)
#
#
#
# ttk.Button(tool_bar, text="Toda la información", command=show_all).grid(row=5, column=1, padx=5, pady=5)
#
#
#
# ttk.Button(tool_bar, text="Reseñas",command=show_reviews).grid(row=6, column=1, padx=5, pady=5)
#
# ttk.Button(tool_bar, text="Limpiar todo",command=destroy_all).grid(row=7, column=1, padx=5, pady=5)
#
# ttk.Label(right_frame,).grid(row=0,column=0, padx=5, pady=5)




root.mainloop()





