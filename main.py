import tkinter as tk
import qrcode
from tkinter import filedialog

def generate_qr_code():
    url = url_entry.get()
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white")
    qr_img.show()
    save_button.pack()

def save_qr_code():
    url = url_entry.get()
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white")
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    qr_img.save(file_path)

window = tk.Tk()
window.title("QR Code Generator")

url_label = tk.Label(window, text="Website URL:")
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()

generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

save_button = tk.Button(window, text="Save QR Code", command=save_qr_code)

window.mainloop()