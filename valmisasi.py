#importimine
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
import csv, sys, re
import os
from tkinter.ttk import * 
#avame tekstifaili kus vajalik info
with open('elem.txt', encoding='utf-8') as fail:
    read = fail.readlines() #loeme sisse read mitte elemendid
elements = {}  
for rida in read:
      vesinik = read[0]
      liitium = read[1]
      naatrium = read[2]
      kaalium = read[3]
      rubiidium = read[4]
      tseesium = read[5]
      frantsium = read[6]
      berüllium = read[7]
      magneesium = read[8]
      kaltsium = read[9]
      strontsium = read[10]
      baarium = read[11]
      raadium = read[12]
      boor = read[13]
      alumiinium = read[14]
      gallium = read[15]
      indium = read[16]
      tallium = read[17]
      süsinik = read[18]
      räni = read[19]
      germaanium = read[20]
      tina = read[21]
      plii = read[22]
      lämmastik = read[23]
      fosfor = read[24]
      arseen = read[25]
      antimon = read[26]
      vismut = read[27]
      hapnik = read[28]
      väävel = read[29]
      seleen = read[30]
      telluur = read[31]
      poloonium = read[32]
      fluor = read[33]
      kloor = read[34]
      broom = read[35]
      jood = read[36]
      astaat = read[37]
      heelium = read[38]
      neoon = read[39]
      aargoon = read[40]
      krüptoon = read[41]
      ksenoon = read[42]
      radoon = read[43]
      



fail.close()

def infokast():
    messagebox.showinfo(message=vesinik)
    
def infokast1():
    messagebox.showinfo(message=liitium)
    
def infokast2():
    messagebox.showinfo(message=naatrium)
    
def infokast3():
    messagebox.showinfo(message=kaalium)
    
def infokast4():
    messagebox.showinfo(message=rubiidium)
    
def infokast5():
    messagebox.showinfo(message=tseesium)
    
def infokast6():
    messagebox.showinfo(message=frantsium)
    
def infokast7():
    messagebox.showinfo(message=berüllium)
    
def infokast8():
    messagebox.showinfo(message=magneesium)
    
def infokast9():
    messagebox.showinfo(message=kaltsium)
    
def infokast10():
    messagebox.showinfo(message=strontsium)
    
def infokast11():
    messagebox.showinfo(message=baarium)
    
def infokast12():
    messagebox.showinfo(message=raadium)

def infokast13():
    messagebox.showinfo(message=boor)
    
def infokast14():
    messagebox.showinfo(message=alumiinium)
    
def infokast15():
    messagebox.showinfo(message=gallium)
    
def infokast16():
    messagebox.showinfo(message=indium)
    
def infokast17():
    messagebox.showinfo(message=tallium)
    
def infokast18():
    messagebox.showinfo(message=süsinik)
    
def infokast19():
    messagebox.showinfo(message=räni)
    
def infokast20():
    messagebox.showinfo(message=germaanium)
    
def infokast21():
    messagebox.showinfo(message=tina)
    
def infokast22():
    messagebox.showinfo(message=plii)
    
def infokast23():
    messagebox.showinfo(message=lämmastik)
    
def infokast24():
    messagebox.showinfo(message=fosfor)
    
def infokast25():
    messagebox.showinfo(message=arseen)
    
def infokast26():
    messagebox.showinfo(message=antimon)
    
def infokast27():
    messagebox.showinfo(message=vismut)
    
def infokast28():
    messagebox.showinfo(message=hapnik)
    
def infokast29():
    messagebox.showinfo(message=väävel)
    
def infokast30():
    messagebox.showinfo(message=seleen)
    
def infokast31():
    messagebox.showinfo(message=telluur)
    
def infokast32():
    messagebox.showinfo(message=poloonium)
    
def infokast33():
    messagebox.showinfo(message=fluor)
    
def infokast34():
    messagebox.showinfo(message=kloor)
    
def infokast35():
    messagebox.showinfo(message=broom)
    
def infokast36():
    messagebox.showinfo(message=jood)
    
def infokast37():
    messagebox.showinfo(message=astaat)
    
def infokast38():
    messagebox.showinfo(message=heelium)
    
def infokast39():
    messagebox.showinfo(message=neoon)
    
def infokast40():
    messagebox.showinfo(message=argoon)
    
def infokast41():
    messagebox.showinfo(message=krüptoon)
    
def infokast42():
    messagebox.showinfo(message=ksenoon)
    
def infokast43():
    messagebox.showinfo(message=radoon)
    


# loome akna
raam = Tk()
raam.title("Perioodilisustabel")
raam.geometry("1750x600")

st = Style()
st.theme_use('classic')
st.configure('A.TButton', background = '#89cff0', foreground = 'white')
st.map('A.TButton', background=[('active','black')])

st.configure('B.TButton', background = '#43b3e7', foreground = 'white')
st.map('B.TButton', background=[('active','black')])

st.configure('V.TButton', background = '#d4bee9', foreground = 'white')
st.map('V.TButton', background=[('active','black')])

st.configure('C.TButton', background = 'pink', foreground = 'white')
st.map('C.TButton', background=[('active','black')])


# nupud 1A
nupp = Button(raam, text="H",style='B.TButton',command = infokast)
nupp.place(x=70, y=20, width=75 , height = 75)
nupp = Button(raam, text="Li",style='A.TButton', command = infokast1)
nupp.place(x=70, y= 100, width=75, height = 75)
nupp = Button(raam, text="Na", style='A.TButton',command=infokast2)
nupp.place(x=70, y= 180, width=75, height = 75)
nupp = Button(raam, text="K",style='A.TButton', command=infokast3)
nupp.place(x=70, y= 260, width=75, height = 75)
nupp = Button(raam, text="Rb",style='A.TButton', command=infokast4)
nupp.place(x=70, y=340, width=75, height= 75)
nupp = Button(raam, text="Cs",style='A.TButton', command=infokast5)
nupp.place(x=70, y=420, width=75, height = 75)
nupp = Button(raam, text="Fr",style='A.TButton', command=infokast6)
nupp.place(x=70, y=500, width=75, height = 75)
#IIA
nupp = Button(raam, text="Be",style='A.TButton', command=infokast7)
nupp.place(x=160, y= 100, width=75 , height = 75)
nupp = Button(raam, text="Mg",style='A.TButton', command=infokast8)
nupp.place(x=160, y=180, width=75 , height = 75)
nupp = Button(raam, text="Ca",style='A.TButton', command=infokast9)
nupp.place(x=160, y= 260, width=75 , height = 75)
nupp = Button(raam, text="Sr",style='A.TButton', command=infokast10)
nupp.place(x=160, y= 340, width=75 , height = 75)
nupp = Button(raam, text="Ba",style='A.TButton', command=infokast11)
nupp.place(x=160, y= 420, width=75 , height = 75)
nupp = Button(raam, text="Ra",style='A.TButton', command=infokast12)
nupp.place(x=160, y= 500, width=75 , height = 75)
# #IIIA
nupp = Button(raam, text="B",style='B.TButton', command=infokast13)
nupp.place(x=1150, y=100, width=75 , height = 75)
nupp = Button(raam, text="Al",style='A.TButton', command=infokast14)
nupp.place(x=1150, y=180, width=75 , height = 75)
nupp = Button(raam, text="Ga",style='A.TButton', command=infokast15)
nupp.place(x=1150, y=260, width=75 , height = 75)
nupp = Button(raam, text="In",style='A.TButton', command=infokast16)
nupp.place(x=1150, y=340, width=75 , height = 75)
nupp = Button(raam, text="Tl",style='A.TButton', command=infokast17)
nupp.place(x=1150, y=420, width=75 , height = 75)
# #IVA
nupp = Button(raam, text="C",style='B.TButton', command=infokast18)
nupp.place(x=1240, y=100, width=75 , height = 75)
nupp = Button(raam, text="Si",style='B.TButton', command=infokast19)
nupp.place(x=1240, y=180, width=75 , height = 75)
nupp = Button(raam, text="Ge",style='A.TButton', command=infokast20)
nupp.place(x=1240, y=260, width=75 , height = 75)
nupp = Button(raam, text="Sn",style='A.TButton', command=infokast21)
nupp.place(x=1240, y=340, width=75 , height = 75)
nupp = Button(raam, text="Pb",style='A.TButton', command=infokast22)
nupp.place(x=1240, y=420, width=75 , height = 75)
# #VA
nupp = Button(raam, text="N",style='B.TButton', command=infokast23)
nupp.place(x=1330, y=100, width=75 , height = 75)
nupp = Button(raam, text="P",style='B.TButton', command=infokast24)
nupp.place(x=1330, y=180, width=75 , height = 75)
nupp = Button(raam, text="As",style='B.TButton', command=infokast25)
nupp.place(x=1330, y=260, width=75 , height = 75)
nupp = Button(raam, text="Sb",style='A.TButton', command=infokast26)
nupp.place(x=1330, y=340, width=75 , height = 75)
nupp = Button(raam, text="Bi",style='A.TButton', command=infokast27)
nupp.place(x=1330, y=420, width=75 , height = 75)
# #VIA
nupp = Button(raam, text="O",style='B.TButton', command=infokast28)
nupp.place(x=1420, y=100, width=75 , height = 75)
nupp = Button(raam, text="S", style='B.TButton',command=infokast29)
nupp.place(x=1420, y=180, width=75 , height = 75)
nupp = Button(raam, text="Se",style='B.TButton', command=infokast30)
nupp.place(x=1420, y=260, width=75 , height = 75)
nupp = Button(raam, text="Te",style='B.TButton', command=infokast31)
nupp.place(x=1420, y=340, width=75 , height = 75)
nupp = Button(raam, text="Po",style='A.TButton', command=infokast32)
nupp.place(x=1420, y=420, width=75 , height = 75)
# #VIIA
nupp = Button(raam, text="F",style='B.TButton', command=infokast33)
nupp.place(x=1510, y=100, width=75 , height = 75)
nupp = Button(raam, text="Cl",style='B.TButton', command=infokast34)
nupp.place(x=1510, y=180, width=75 , height = 75)
nupp = Button(raam, text="Br",style='B.TButton', command=infokast35)
nupp.place(x=1510, y=260, width=75 , height = 75)
nupp = Button(raam, text="I",style='B.TButton', command=infokast36)
nupp.place(x=1510, y=340, width=75 , height = 75)
nupp = Button(raam, text="At",style='B.TButton', command=infokast37)
nupp.place(x=1510, y=420, width=75 , height = 75)
# #VIIIA
nupp = Button(raam, text="He",style='V.TButton', command=infokast38)
nupp.place(x=1600, y=20, width=75 , height = 75)
nupp = Button(raam, text="Ne",style='V.TButton', command=infokast39)
nupp.place(x=1600, y=100, width=75 , height = 75)
nupp = Button(raam, text="Ar",style='V.TButton', command=infokast40)
nupp.place(x=1600, y=180, width=75 , height = 75)
nupp = Button(raam, text="Kr",style='V.TButton', command=infokast41)
nupp.place(x=1600, y=260, width=75 , height = 75)
nupp = Button(raam, text="Xe",style='V.TButton', command=infokast42)
nupp.place(x=1600, y=340, width=75 , height = 75)
nupp = Button(raam, text="Rn",style='V.TButton', command=infokast43)
nupp.place(x=1600, y=420, width=75 , height = 75)
#vahepealne imelik
nupp = Button(raam, text="?",style='C.TButton')
nupp.place(x=250, y=260, width=75 , height = 75)
nupp = Button(raam, text="?",style='C.TButton')
nupp.place(x=250, y=340, width=75, height= 75)
nupp = Button(raam, text="?",style='C.TButton')
nupp.place(x=250, y=420, width=75, height = 75)
nupp = Button(raam, text="?",style='C.TButton')
nupp.place(x=250, y=500, width=75, height = 75)
# vahepealne imelik 2
nupp = Button(raam, text="?",style='C.TButton')
nupp.place(x=340, y=260, width=75 , height = 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=340, y=340, width=75, height= 75)
nupp = Button(raam, text="?",style='C.TButton')
nupp.place(x=340, y=420, width=75, height = 75)
nupp = Button(raam, text="?",style='C.TButton')
nupp.place(x=340, y=500, width=75, height = 75)
# 3
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=430, y=260, width=75 , height = 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=430, y=340, width=75, height= 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=430, y=420, width=75, height = 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=430, y=500, width=75, height = 75)
#4
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=520, y=260, width=75 , height = 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=520, y=340, width=75, height= 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=520, y=420, width=75, height = 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=520, y=500, width=75, height = 75)
#5
nupp = Button(raam, text="?", style='C.TButton',)
nupp.place(x=610, y=260, width=75 , height = 75)
nupp = Button(raam, text="?", style='C.TButton',)
nupp.place(x=610, y=340, width=75, height= 75)
nupp = Button(raam, text="?", style='C.TButton',)
nupp.place(x=610, y=420, width=75, height = 75)
nupp = Button(raam, text="?", style='C.TButton',)
nupp.place(x=610, y=500, width=75, height = 75)
#6
nupp = Button(raam, text="?",style='C.TButton')
nupp.place(x=700, y=260, width=75 , height = 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=700, y=340, width=75, height= 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=700, y=420, width=75, height = 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=700, y=500, width=75, height = 75)
#7
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=790, y=260, width=75 , height = 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=790, y=340, width=75, height= 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=790, y=420, width=75, height = 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=790, y=500, width=75, height = 75)
#8
nupp = Button(raam, text="?",style='C.TButton')
nupp.place(x=880, y=260, width=75 , height = 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=880, y=340, width=75, height= 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=880, y=420, width=75, height = 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=880, y=500, width=75, height = 75)
#9
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=970, y=260, width=75 , height = 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=970, y=340, width=75, height= 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=970, y=420, width=75, height = 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=970, y=500, width=75, height = 75)
#10
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=1060, y=260, width=75 , height = 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=1060, y=340, width=75, height= 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=1060, y=420, width=75, height = 75)
nupp = Button(raam, text="?", style='C.TButton')
nupp.place(x=1060, y=500, width=75, height = 75)
# ilmutame akna ekraanile
raam.mainloop()