import io
import requests

from PIL import ImageTk, Image

def url_img(url):
    r = requests.get(url, stream=True)
    return ImageTk.PhotoImage(Image.open(r.raw).resize(100,100))


def show_product(self, index):
    if 0 <= index < len(self.products):
        product = self.products[index]

