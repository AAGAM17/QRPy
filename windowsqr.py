import tkinter as tk
import pyqrcode
from tkinter import filedialog
from PIL import Image

def generate_qr_code():
    url = url_entry.get()
    qr = pyqrcode.create(url)
    qr.png('temp.png', scale=10)
    qr_img = Image.open('temp.png')
    qr_img = qr_img.resize((410, 410))
    qr_img.save('temp.png')
    qr_img = tk.PhotoImage(file='temp.png')
    qr_label.config(image=qr_img)
    qr_label.image = qr_img
    save_button.pack()

def save_qr_code():
    url = url_entry.get()
    qr = pyqrcode.create(url)
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    qr.png(file_path, scale=10)

window = tk.Tk()
window.title("QR Code Generator")

url_label = tk.Label(window, text="Website URL:")
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()

generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

qr_label = tk.Label(window)
qr_label.pack()

save_button = tk.Button(window, text="Save QR Code", command=save_qr_code)

window.mainloop()