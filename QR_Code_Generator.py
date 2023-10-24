#Python  Code to generate QR code using tkinter, Pillow and qrcode 


from tkinter import Button, Label, PhotoImage, Entry
from PIL import Image
import tkinter as tk
import qrcode

qr_lbl = None
mainwindow=tk.Tk()
mainwindow.title("QR Code Generator")


def generate_qr_code():
    global qr_lbl
    data = text_entr.get()
    img = qrcode.make(data)
    img.save('QR_Code_Image.png')

    image = Image.open('QR_Code_Image.png')
    image.thumbnail((200,200))
    image.save('D:\\PythonLearning\\TkInter_GUI\\QR_Code_Image.png')

    qr_code = PhotoImage(file="QR_Code_Image.png")
    qr_lbl.config(image=qr_code)
    print(qr_code)

instruction_info = Button(mainwindow, text="Enter the String")
instruction_info.pack()

text_entr = Entry(mainwindow)
text_entr.pack(fill="x")


genrate_code = Button(mainwindow, text="Generate QR Code", command=generate_qr_code)
genrate_code.pack()

qr_lbl = Label(mainwindow)
qr_lbl.place(x=300, y=100, width=200, height=200)



mainwindow.geometry("800x600")
mainwindow.resizable(False, False)
mainwindow.mainloop()