from tkinter import *
from tkinter import messagebox
import pyqrcode
import os

window = Tk()
window.title("QR Code Generator")

#genera codice qr
def generate():
    if len(subject.get()) != 0:
        global myQr
        myQr = pyqrcode.create(subject.get())
        qrImage = myQr.xbm(scale=6)
        global photo
        photo = BitmapImage(data=qrImage)
    else:
        messagebox.showerror(message="Immetere il link.", title="Errore")
    try:
        showCode()
    except:
        pass

#Mostra Codice
def showCode():
    global photo
    notificationLabel.config(image=photo)
    subLabel.config(text="Codice QR di: " + subject.get())

def save():
    #cartella di qr
    dir = path1 = os.getcwd() + "\\Qr Codes"
    #crea cartella se non esiste
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get()) != 0:
            qrImage = myQr.png(os.path.join(dir, name.get() + ".png"), scale=6)
            messagebox.showinfo(message="Immagine salvata", title="Salvataggio completato")
        else:
            messagebox.showerror(message="Il nome del file non può essere vuoto", title="Errore")
    except:
        messagebox.showerror(message="Genera il codice QR prima", title="Errore")

lab1 = Label(window, text="Inserisci il link", font=("Helvetica", 12))
lab1.grid(row=0, column=0, sticky=N + S + E + W)

lab2 = Label(window, text="Inserisci il nome del file", font=("Helvetica", 12))
lab2.grid(row=1, column=0, sticky=N + S + E + W)

subject = StringVar()
subjectEntry = Entry(window, textvariable=subject, font=("Helvetica", 12))
subjectEntry.grid(row=0, column=1, sticky=N + S + E + W)

name = StringVar()
nameEntry = Entry(window, textvariable=name, font=("Helvetica", 12))
nameEntry.grid(row=1, column=1, sticky=N + S + E + W)

createButton = Button(window, text="Crea QR Code", font=("Helvetica", 12), width=15, command=generate)
createButton.grid(row=0, column=3, sticky=N + S + E + W)
notificationLabel = Label(window)
notificationLabel.grid(row=2, column=1, sticky=N + S + E + W)

subLabel1 = Label(window, text="")
subLabel1.grid(row=3, column=1, sticky=N + S + E + W)

showButton = Button(window, text="Salva come PNG", font=("Helvetica", 12), width=15, command=save)
showButton.grid(row=1, column=3, sticky=N + S + E + W)

totalRows=3
totalCols=3
for row in range(totalRows+1):
    window.grid_rowconfigure(row, weight=1)
for col in range(totalCols+1):
    window.grid_columnconfigure(col, weight=1)

window.mainloop()