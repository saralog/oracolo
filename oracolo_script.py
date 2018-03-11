from tkinter import *
import os
import frasi_oracolari as fo
import random

def consulta():
    x=random.randint(0, len(fo.list_resp)-1)
    global resp
    resp=fo.list_resp[x]
    w.itemconfigure(testo1,text=resp,fill='yellow')
    return resp
master = Tk()
master.title("Oracoli spaziali")
ind=os.path.abspath('cerchio2.gif')
background = ind
img = PhotoImage(file=background)
w = Canvas(master, width=500, height=333)
w.pack()
photo=w.create_image(250,165, image=img)
testo1=w.create_text(300,100, text="Consigli pseudocasuali\ndell'oracolo \ndello spazio interplanetario\ndel 'boh!' cosmico\n",font="courier", fill="white", state="normal")

w.create_line(300, 500, 500, 0, fill="red", dash=(4, 4))
b = Button(master, text="Ho già la risposta, aspetto solo una tua domanda. Consulta l'Oracolo", command=consulta)
resp=""


b.pack()



mainloop()

