from tkinter import *
import random

root = Tk()
root.title("lista")
root.geometry("400x400")

lista_ale = Label(root)
lista_organizada = Label(root)
btn = Button(root)

def randomlist():
    randomlist = random.sample(range(1,30),5)  
    lista_ale["text"] = "lista aleatória: " + str(randomlist)
    randomlist.sort()
    lista_organizada["text"] = "lista organizada: " + str(randomlist)

btn= Button(root, text="gere uma lista aleatória", command=randomlist)
btn.place(relx = 0.5, rely=0.4, anchor=CENTER)

lista_ale.place(relx = 0.5, rely=0.5, anchor=CENTER)
lista_organizada.place(relx = 0.5, rely=0.6, anchor=CENTER)

root.mainloop()