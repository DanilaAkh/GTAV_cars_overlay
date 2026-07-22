import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO

conn = sqlite3.connect('gtav_cars.db')


root = Tk()
root.title("SQLite Image Viewer")

def show(data):
    img_byte = BytesIO(data)
    img = ImageTk.PhotoImage(Image.open(img_byte))
    Label(root,image=img).pack()
    root.image = img # Keep a reference

def fetch(car):
    with conn:
        c = conn.cursor()
        name = car # Any id
        c.execute('SELECT photo FROM cars where name=?',(name,))
        data = c.fetchall()[0][0] # Get the blob data
    show(data) # Call the function with the passes data
    

def show_img(car):
    fetch(car)
    root.mainloop()
