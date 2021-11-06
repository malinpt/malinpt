from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
import csv, sys, re
import os

with open('elements.txt', encoding='utf-8') as fail:
    read = fail.readlines() 
elements = {}  # The data structure that stores all the element data.
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
      
#       element = {'Aatomi number':  rida[0],
#                  'Sümbol':         rida[1],
#                  'Element':        rida[2],
#                  'Metalliliik':    rida[3],
#                  'Sulamispunkt':   rida[4],
#                  'Omadused':       rida[5]}
#                 'Period':         line[5],
#                 'Atomic weight':  line[6] + ' u', # atomic mass unit
#                 'Density':        line[7] + ' g/cm^3', # grams/cubic cm
#                 'Melting point':  line[8] + ' K', # kelvin
#                 'Boiling point':  line[9] + ' K', # kelvin
#                 'Specific heat capacity':      line[10] + ' J/(g*K)',
#                 'Electronegativity':           line[11],
#                 'Abundance in earth\'s crust': line[12] + ' mg/kg'}

# see funktsioon käivitatakse nupule klõpsamisel
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
    
# def infokast1():
#     messagebox.showinfo(message=liitium)
# def infokast1():
#     messagebox.showinfo(message=liitium)
# def infokast1():
#     messagebox.showinfo(message=liitium)
# # def infokast():
#     info=elements[0][2]
#     messagebox.showinfo(message=info)


# loome akna
raam = Tk()
raam.title("Tabel")
raam.geometry("1750x600")

style = ttk.Style()
style.theme_use('classic')
style.configure('TButton', background = 'white', foreground = 'black')
style.map('TButton', background=[('active','red')])



# esimene veerg
nupp = ttk.Button(raam, text="H",command = infokast)
nupp.place(x=70, y=20, width=75 , height = 75)
nupp = ttk.Button(raam, text="Li", command = infokast1)
nupp.place(x=70, y= 100, width=75, height = 75)
nupp = ttk.Button(raam, text="Na", command=infokast2)
nupp.place(x=70, y= 180, width=75, height = 75)
nupp = ttk.Button(raam, text="K", command=infokast3)
nupp.place(x=70, y= 260, width=75, height = 75)
nupp = ttk.Button(raam, text="Rb", command=infokast4)
nupp.place(x=70, y=340, width=75, height= 75)
nupp = ttk.Button(raam, text="Cs", command=infokast5)
nupp.place(x=70, y=420, width=75, height = 75)
nupp = ttk.Button(raam, text="Fr", command=infokast6)
nupp.place(x=70, y=500, width=75, height = 75)
#teine veerg
nupp = ttk.Button(raam, text="Be", command=infokast7)
nupp.place(x=160, y= 100, width=75 , height = 75)
nupp = ttk.Button(raam, text="Mg", command=infokast8)
nupp.place(x=160, y=180, width=75 , height = 75)
nupp = ttk.Button(raam, text="Ca", command=infokast9)
nupp.place(x=160, y= 260, width=75 , height = 75)
nupp = ttk.Button(raam, text="Sr", command=infokast10)
nupp.place(x=160, y= 340, width=75 , height = 75)
nupp = ttk.Button(raam, text="Ba", command=infokast11)
nupp.place(x=160, y= 420, width=75 , height = 75)
nupp = ttk.Button(raam, text="Ra", command=infokast12)
nupp.place(x=160, y= 500, width=75 , height = 75)
#IIIA
nupp = ttk.Button(raam, text="B", command=infokast)
nupp.place(x=1150, y=100, width=75 , height = 75)
nupp = ttk.Button(raam, text="Al", command=infokast)
nupp.place(x=1150, y=180, width=75 , height = 75)
nupp = ttk.Button(raam, text="Ga", command=infokast)
nupp.place(x=1150, y=260, width=75 , height = 75)
nupp = ttk.Button(raam, text="In", command=infokast)
nupp.place(x=1150, y=340, width=75 , height = 75)
nupp = ttk.Button(raam, text="Tl", command=infokast)
nupp.place(x=1150, y=420, width=75 , height = 75)
#IVA
nupp = ttk.Button(raam, text="C", command=infokast)
nupp.place(x=1240, y=100, width=75 , height = 75)
nupp = ttk.Button(raam, text="Si", command=infokast)
nupp.place(x=1240, y=180, width=75 , height = 75)
nupp = ttk.Button(raam, text="Ge", command=infokast)
nupp.place(x=1240, y=260, width=75 , height = 75)
nupp = ttk.Button(raam, text="Sn", command=infokast)
nupp.place(x=1240, y=340, width=75 , height = 75)
nupp = ttk.Button(raam, text="Pb", command=infokast)
nupp.place(x=1240, y=420, width=75 , height = 75)
#VA
nupp = ttk.Button(raam, text="N", command=infokast)
nupp.place(x=1330, y=100, width=75 , height = 75)
nupp = ttk.Button(raam, text="P", command=infokast)
nupp.place(x=1330, y=180, width=75 , height = 75)
nupp = ttk.Button(raam, text="As", command=infokast)
nupp.place(x=1330, y=260, width=75 , height = 75)
nupp = ttk.Button(raam, text="Sb", command=infokast)
nupp.place(x=1330, y=340, width=75 , height = 75)
nupp = ttk.Button(raam, text="Bi", command=infokast)
nupp.place(x=1330, y=420, width=75 , height = 75)
#VIA
nupp = ttk.Button(raam, text="O", command=infokast)
nupp.place(x=1420, y=100, width=75 , height = 75)
nupp = ttk.Button(raam, text="S", command=infokast)
nupp.place(x=1420, y=180, width=75 , height = 75)
nupp = ttk.Button(raam, text="Se", command=infokast)
nupp.place(x=1420, y=260, width=75 , height = 75)
nupp = ttk.Button(raam, text="Te", command=infokast)
nupp.place(x=1420, y=340, width=75 , height = 75)
nupp = ttk.Button(raam, text="Po", command=infokast)
nupp.place(x=1420, y=420, width=75 , height = 75)
#VIIA
nupp = ttk.Button(raam, text="F", command=infokast)
nupp.place(x=1510, y=100, width=75 , height = 75)
nupp = ttk.Button(raam, text="Cl", command=infokast)
nupp.place(x=1510, y=180, width=75 , height = 75)
nupp = ttk.Button(raam, text="Br", command=infokast)
nupp.place(x=1510, y=260, width=75 , height = 75)
nupp = ttk.Button(raam, text="I", command=infokast)
nupp.place(x=1510, y=340, width=75 , height = 75)
nupp = ttk.Button(raam, text="At", command=infokast)
nupp.place(x=1510, y=420, width=75 , height = 75)
#VIIIA
nupp = ttk.Button(raam, text="He", command=infokast)
nupp.place(x=1600, y=20, width=75 , height = 75)
nupp = ttk.Button(raam, text="Ne", command=infokast)
nupp.place(x=1600, y=100, width=75 , height = 75)
nupp = ttk.Button(raam, text="Ar", command=infokast)
nupp.place(x=1600, y=180, width=75 , height = 75)
nupp = ttk.Button(raam, text="Kr", command=infokast)
nupp.place(x=1600, y=260, width=75 , height = 75)
nupp = ttk.Button(raam, text="Xe", command=infokast)
nupp.place(x=1600, y=340, width=75 , height = 75)
nupp = ttk.Button(raam, text="Rn", command=infokast)
nupp.place(x=1600, y=420, width=75 , height = 75)
#vahepealne imelik
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=250, y=260, width=75 , height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=250, y=340, width=75, height= 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=250, y=420, width=75, height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=250, y=500, width=75, height = 75)
# vahepealne imelik 2
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=340, y=260, width=75 , height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=340, y=340, width=75, height= 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=340, y=420, width=75, height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=340, y=500, width=75, height = 75)
# 3
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=430, y=260, width=75 , height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=430, y=340, width=75, height= 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=430, y=420, width=75, height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=430, y=500, width=75, height = 75)
#4
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=520, y=260, width=75 , height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=520, y=340, width=75, height= 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=520, y=420, width=75, height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=520, y=500, width=75, height = 75)
#5
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=610, y=260, width=75 , height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=610, y=340, width=75, height= 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=610, y=420, width=75, height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=610, y=500, width=75, height = 75)
#6
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=700, y=260, width=75 , height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=700, y=340, width=75, height= 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=700, y=420, width=75, height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=700, y=500, width=75, height = 75)
#7
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=790, y=260, width=75 , height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=790, y=340, width=75, height= 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=790, y=420, width=75, height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=790, y=500, width=75, height = 75)
#8
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=880, y=260, width=75 , height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=880, y=340, width=75, height= 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=880, y=420, width=75, height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=880, y=500, width=75, height = 75)
#9
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=970, y=260, width=75 , height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=970, y=340, width=75, height= 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=970, y=420, width=75, height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=970, y=500, width=75, height = 75)
#10
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=1060, y=260, width=75 , height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=1060, y=340, width=75, height= 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=1060, y=420, width=75, height = 75)
nupp = ttk.Button(raam, text="?", command=infokast)
nupp.place(x=1060, y=500, width=75, height = 75)
# ilmutame akna ekraanile
raam.mainloop()