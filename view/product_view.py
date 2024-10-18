import tkinter as tk
from tkinter import ttk
import requests
from PIL import ImageTk, Image
from main import product

root = tk.Tk()
root.title("Tkinter API layout")
root.maxsize(900, 600)
root.config(bg="skyblue")

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

ttk.Label(right_frame, ).grid(row=0,column=0, padx=5, pady=5)

tool_bar = tk.Frame(product_frame, width=220, height=325)
tool_bar.grid(row=2, column=0, padx=5, pady=5)

ttk.Button(tool_bar, text="Anterior").grid(row=0, column=0, padx=5, pady=3, ipadx=10)
ttk.Button(tool_bar, text="Siguiente").grid(row=0, column=2, padx=5, pady=3, ipadx=10)

ttk.Label(tool_bar, text="Descripción").grid(row=1, column=1, padx=5, pady=5)
ttk.Label(tool_bar, text="Precio").grid(row=2, column=1, padx=5, pady=5)
ttk.Label(tool_bar, text="Stock").grid(row=3, column=1, padx=5, pady=5)
ttk.Label(tool_bar, text="Información de envio").grid(row=4, column=1, padx=5, pady=5)
ttk.Label(tool_bar, text="Toda la información").grid(row=5, column=1, padx=5, pady=5)
ttk.Label(tool_bar, text="Reseñas").grid(row=6, column=1, padx=5, pady=5)

root.mainloop()





