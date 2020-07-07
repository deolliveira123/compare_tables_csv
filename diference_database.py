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
    read_file = pd.read_csv(import_file_path)
browserButtonTxt = tk.Button(text="   Importandoo arquivo   ", command=getTxt, bg='brown', fg='white', font=('Arial', 12, 'bold'))
canvas1.create_window(200, 120, window=browserButtonTxt)

def convertToCsv ():
    global read_file
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    read_file.to_csv(export_file_path, index=None)

saveAsButtoncsv = tk.Button(text='Convertendo para CSV', command=convertToCsv, bg='brown', fg='white', font=('Arial', 12, 'bold'))
canvas1.create_window(200, 180, window=saveAsButtoncsv)

#def exitApplication():
    #MsgBox = tk.messagebox.askquestion('fechar?')
    #if MsgBox == 'yes':
        #root.destroy()
#exitButton = tk.Button(label1 = tk.Label(root, text='convertendo txt para csv', bg='lightsteelblue2')
#label1.config(font=('Arial', 20))root, text='fechando', command=exitApplication, bg='brown', fg='white', font=('Arial', 12, 'bold'))
#canvas1.create_window(200, 240, window=exitButton)

root.mainloop()
