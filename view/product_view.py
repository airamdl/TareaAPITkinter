import urllib
from tkinter import Tk, Frame, Label, PhotoImage, RAISED
from urllib.request import urlopen

from PIL import ImageTk
from PIL._tkinter_finder import tk

from main import product

root = Tk()
root.title("Tkinter API layout")
root.maxsize(900, 600)
root.config(bg="skyblue")


product_frame = Frame(root, width=300, height=400, bg='grey')
product_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(root, width=650, height=400, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)

title = product.title
Label(product_frame, text=title).grid(row=0, column=0, padx=5, pady=5)


if hasattr(product, 'images'):

    image_url = product.images[0]
    print(image_url)
    image_path =
else:
    image_path = "../imageFolder/default_image.png"

print(image_path)

image = PhotoImage(file=image_path)
product_image = image.subsample(1,1)

Label(product_frame, image=product_image).grid(row=1, column=0, padx=5, pady=5)

Label(right_frame, ).grid(row=0,column=0, padx=5, pady=5)

tool_bar = Frame(product_frame, width=220, height=325)
tool_bar.grid(row=2, column=0, padx=5, pady=5)

Label(tool_bar, text="Anterior", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)
Label(tool_bar, text="Siguiente", relief=RAISED).grid(row=0, column=2, padx=5, pady=3, ipadx=10)

Label(tool_bar, text="Descripción").grid(row=1, column=1, padx=5, pady=5)
Label(tool_bar, text="Precio").grid(row=2, column=1, padx=5, pady=5)
Label(tool_bar, text="Stock").grid(row=3, column=1, padx=5, pady=5)
Label(tool_bar, text="Información de envio").grid(row=4, column=1, padx=5, pady=5)
Label(tool_bar, text="Toda la información").grid(row=5, column=1, padx=5, pady=5)
Label(tool_bar, text="Reseñas").grid(row=6, column=1, padx=5, pady=5)

root.mainloop()





