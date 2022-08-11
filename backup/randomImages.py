#get a random image from internet
import requests
import os

url = 'https://source.unsplash.com/random/400x400'
response = requests.get(url)

#display response in a window

from io import BytesIO
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Random Image')
root.geometry('400x400')

image = Image.open(BytesIO(response.content))
image = image.resize((400, 400), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.pack()

root.mainloop()

print('done')