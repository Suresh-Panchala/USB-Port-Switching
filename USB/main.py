from tkinter import *
from tkinter import Tk

import serial.tools.list_ports

temp = 0
portState = 0
comPort = 0
ports = list(serial.tools.list_ports.comports())
for portString in ports:
    com = str(portString)
    comPort = com[0:4]
serialPort = serial.Serial(port=comPort, baudrate=9600, timeout=2)

root: Tk = Tk()
root.title("USB SWITCHING APPLICATION")
root.geometry('400x450')
root.resizable(width=False, height=False)
root.iconbitmap('usb.ico')
logo = PhotoImage(file='usb.png')
frame = LabelFrame(root, height=10, width=500, bg='#1C2833', fg='#ffffff').pack()
w1 = Label(root, text="USB SWITCH", font='Helvetica 20 bold', fg='#0B5345').pack(padx=10, pady=10)
w2 = Label(root, image=logo).pack(padx=10, pady=10)


def usb_b():
    serialPort.write(b'B')
    global temp
    if temp == 0:
        temp = 1
        stB.pack_forget()
        stA.pack(pady=5)


def usb_c():
    serialPort.write(b'C')
    global temp
    if temp == 1:
        temp = 0
        stA.pack_forget()
        stB.pack(pady=5)


top = Label(root, text=" Select any one of the Ports to Connect ", font='Times 14 ', fg='#117A65').pack()
b1 = Button(root, text="USB - B", width=20, font='Helvetica 20 ', borderwidth='0', bg='#2E86C1',
            fg='#ffffff', command=usb_b).pack(pady=10)
b2 = Button(root, text="USB - C", width=20, font='Helvetica 20 ', borderwidth='0', bg='#2E86C1',
            fg='#ffffff', command=usb_c).pack(pady=5)
stA = Label(root, text="USB - B Port is Active Now", width=27, font='Times 16 ', fg='#FA032C', bg='#000000')
stB = Label(root, text="USB - C Port is Active Now", width=27, font='Times 16 ', fg='#FA032C', bg='#000000')

qt = Button(root, text="QUIT", command=root.destroy, width=9,  font='Arial 12 bold', bg='#C0392B',
            fg='#ffffff', borderwidth='0').pack(side='bottom', pady=20)

root.mainloop()
