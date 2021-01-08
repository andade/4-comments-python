import tkinter
from tkinter import *
import os
import unicodedata

def strip_accents(text):
    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)

window = Tk()


#variables pour A
messagea=StringVar()
messagea.set("Message A")
noma=StringVar()
noma.set("Nom A")
textnoma=""
textmessagea=""

#variables pour B
messageb=StringVar()
messageb.set("Message B")
nomb=StringVar()
nomb.set("Nom B")
textnomb=""
textmessageb=""

#variables pour C
messagec=StringVar()
messagec.set("Message C")
nomc=StringVar()
nomc.set("Nom C")
textnomc=""
textmessagec=""

#variables pour D
messaged=StringVar()
messaged.set("Message D")
nomd=StringVar()
nomd.set("Nom D")
textnomd=""
textmessaged=""

window.rowconfigure(0,minsize=40)
#####################################################
#login mainwindow
######################################################
def bouttonaclick():
    fichiernoma = open(r"\\DESKTOP-BB1U1D1\_zone de transit\nom A.txt","w")
    fichiermessagea = open(r"\\DESKTOP-BB1U1D1\_zone de transit\message A.txt","w")
    global messagea
    global noma
    global textnoma
    global textmessagea
    messagea.set(casemessagea.get())
    textmessagea=strip_accents(casemessagea.get())
    casemessagea.delete(0, END)
    noma.set(casenoma.get())
    textnoma=strip_accents(casenoma.get())
    casenoma.delete(0,END)
    fichiernoma.write(textnoma)
    print(textnoma)
    fichiernoma.close()
    fichiermessagea.write(textmessagea)
    fichiermessagea.close()


def bouttonbclick():
    
    
    global messageb
    global nomb
    global textnomb
    global textmessageb
    messageb.set(casemessageb.get())
    textmessageb=strip_accents(casemessageb.get())
    casemessageb.delete(0, END)
    nomb.set(casenomb.get())
    textnomb=strip_accents(casenomb.get())
    casenomb.delete(0,END)
    fichiernomb = open(r"\\DESKTOP-BB1U1D1\_zone de transit\nom B.txt","w")
    fichiernomb.write(textnomb)
    fichiernomb.close()
    fichiermessageb = open(r"\\DESKTOP-BB1U1D1\_zone de transit\message B.txt","w")
    fichiermessageb.write(textmessageb)
    fichiermessageb.close()
    
def bouttoncclick():
    fichiernomc = open(r"\\DESKTOP-BB1U1D1\_zone de transit\nom C.txt","w")
    fichiermessagec = open(r"\\DESKTOP-BB1U1D1\_zone de transit\message C.txt","w")
    global messagec
    global nomc
    global textnomc
    global textmessagec
    messagec.set(casemessagec.get())
    textmessagec=strip_accents(casemessagec.get())
    casemessagec.delete(0, END)
    nomc.set(casenomc.get())
    textnomc=strip_accents(casenomc.get())
    casenomc.delete(0,END)
    fichiernomc.write(textnomc)
    fichiernomc.close()
    fichiermessagec.write(textmessagec)
    fichiermessagec.close()
    
def bouttondclick():
    fichiernomd = open(r"\\DESKTOP-BB1U1D1\_zone de transit\nom D.txt","w")
    fichiermessaged = open(r"\\DESKTOP-BB1U1D1\_zone de transit\message D.txt","w")
    global messaged
    global nomd
    global textnomd
    global textmessaged
    messaged.set(casemessaged.get())
    textmessaged=strip_accents(casemessaged.get())
    casemessaged.delete(0, END)
    nomd.set(casenomd.get())
    textnomd=strip_accents(casenomd.get())
    casenomd.delete(0,END)
    fichiernomd.write(textnomd)
    fichiernomd.close()
    fichiermessaged.write(textmessaged)
    fichiermessaged.close()

    #Window creation   
colonne1=Label(window, text="Nom")
colonne1.grid(row=1, column=1)

colonne3=Label(window, text="Message")
colonne3.grid(row=1, column=2)

casenoma = Entry(window, bd =10)
casenoma.grid(row=2, column=1)
casemessagea = Entry(window, bd =10)
casemessagea.grid(row=2, column=2)
etiquettemessagea = Label(window, textvariable=messagea, wraplength=500)
etiquettemessagea.grid(row=2, column=6)
deuxpointa = Label(window, text=" :")
deuxpointa.grid(row=2, column=5)
etiquettenoma = Label(window, textvariable=noma, wraplength=500)
etiquettenoma.grid(row=2, column=4)
buttona = tkinter.Button(window, text="Changer le message A", command = bouttonaclick)
buttona.grid(row=2, column=3)

casenomb = Entry(window, bd =10)
casenomb.grid(row=3, column=1)
casemessageb = Entry(window, bd =10)
casemessageb.grid(row=3, column=2)
etiquettemessageb = Label(window, textvariable=messageb, wraplength=500)
etiquettemessageb.grid(row=3, column=6)
deuxpointb = Label(window, text=" :")
deuxpointb.grid(row=3, column=5)
etiquettenomb = Label(window, textvariable=nomb, wraplength=500)
etiquettenomb.grid(row=3, column=4)
buttonb = tkinter.Button(window, text="Changer le message B", command = bouttonbclick)
buttonb.grid(row=3, column=3)

casenomc = Entry(window, bd =10)
casenomc.grid(row=4, column=1)
casemessagec = Entry(window, bd =10)
casemessagec.grid(row=4, column=2)
etiquettemessagec = Label(window, textvariable=messagec, wraplength=500)
etiquettemessagec.grid(row=4, column=6)
deuxpointc = Label(window, text=" :")
deuxpointc.grid(row=4, column=5)
etiquettenomc = Label(window, textvariable=nomc, wraplength=500)
etiquettenomc.grid(row=4, column=4)
buttonc = tkinter.Button(window, text="Changer le message c", command = bouttoncclick)
buttonc.grid(row=4, column=3)

casenomd = Entry(window, bd =10)
casenomd.grid(row=5, column=1)
casemessaged = Entry(window, bd =10)
casemessaged.grid(row=5, column=2)
etiquettemessaged = Label(window, textvariable=messaged, wraplength=500)
etiquettemessaged.grid(row=5, column=6)
deuxpointd = Label(window, text=" :")
deuxpointd.grid(row=5, column=5)
etiquettenomd = Label(window, textvariable=nomd, wraplength=500)
etiquettenomd.grid(row=5, column=4)
buttond = tkinter.Button(window, text="Changer le message D", command = bouttondclick)
buttond.grid(row=5, column=3)


window.mainloop()
   
