#Python  Code to read QR code using tkinter, Pillow and opencv

from tkinter import Button, Label, PhotoImage, filedialog, StringVar
import tkinter as tk
from PIL import Image
import cv2

qr_file_ptr = None
mainwindow= tk.Tk()
mainwindow.title("QR Code Parser")

def select_qr_image():
    global qr_file_ptr
    qr_file_ptr = filedialog.askopenfilename(initialdir=".", filetypes=(("PNG Files","*.png"),))

    if qr_file_ptr:
        image = Image.open(qr_file_ptr)
        image.thumbnail((200,200))
        image.save(qr_file_ptr)

    qr_image = PhotoImage(file=qr_file_ptr)
    qr_code_lbl.config(image=qr_image)

def read_qr_image():
    global qr_file_ptr
    img = cv2.imread(qr_file_ptr)
    dec = cv2.QRCodeDetector()
    value = dec.detectAndDecode(img)
    qr_info_str.set(value[0])

select_button = Button(mainwindow,text="Select QR code Image", command=select_qr_image)
select_button.config(padx=10,pady=10)
select_button.pack()

qr_code_lbl = Label(mainwindow)
qr_code_lbl.pack(pady=10)

read_button = Button(mainwindow,text="Read QR code", command=read_qr_image)
read_button.config(padx=10,pady=10)
read_button.pack()

qr_info_str = StringVar()
qr_code = Label(mainwindow, textvariable=qr_info_str)
qr_code.config(relief="raised", bd=2, height=3)
qr_code.pack(fill="x", padx=10, pady=10)



mainwindow.geometry("800x600")
mainwindow.resizable(False,False)
mainwindow.mainloop()