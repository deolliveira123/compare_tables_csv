import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=400, bg='lightsteelblue2', relief='raised')
canvas1.pack()
label1 = tk.Label(root, text='convertendo txt para csv', bg='lightsteelblue2')
label1.config(font=('Arial', 20))
canvas1.create_window(200, 40, window=label1)

def getTxt ():
    global read_file

    import_file_path = filedialog.askopenfilename()
    read_file = open(import_file_path, 'r')
browserButtonTxt = tk.Button(text="   Importandoo arquivo   ", command=getTxt, bg='brown', fg='white', font=('Arial', 12, 'bold'))
canvas1.create_window(200, 120, window=browserButtonTxt)

def getTxt2 ():
    global read_file1

    import_file_path1 = filedialog.askopenfilename()
    read_file1 = open(import_file_path1, 'r')
browserButtonTxt2 = tk.Button(text="   Importandoo arquivo 2  ", command=getTxt2, bg='brown', fg='white', font=('Arial', 12, 'bold'))
canvas1.create_window(200, 160, window=browserButtonTxt2)


def convertToCsv ():
    global read_file
    global read_file1

    t1 = read_file.readlines()
    t2 = read_file1.readlines()

    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')

    outFile = open(export_file_path, 'w')
    x = 0

    for i in t1:
        if i != t2[x]:
            outFile.write(t2[x])
        x += 1
    outFile.close()


saveAsButtoncsv = tk.Button(text='Convertendo para CSV', command=convertToCsv, bg='brown', fg='white', font=('Arial', 12, 'bold'))
canvas1.create_window(200, 220, window=saveAsButtoncsv)

def exitApplication():
    MsgBox = tk.messagebox.askquestion('fechar?')
    if MsgBox == 'yes':
        root.destroy()
exitButton = tk.Button(label1 = tk.Label(root, text='convertendo txt para csv', bg='lightsteelblue2')
canvas1.create_window(200, 240, window=exitButton)

root.mainloop()
