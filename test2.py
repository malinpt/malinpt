from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv, sys, re
import os

elementsFile = open('periodictable.csv', encoding='utf-8')
elementsCsvReader = csv.reader(elementsFile)
elements = list(elementsCsvReader)
elementsFile.close()

ELEMENTS = {}  # The data structure that stores all the element data.
for line in elements:
     element = {'Atomic Number':  line[0],
                'Symbol':         line[1],
                'Element':        line[2],
                'Origin of name': line[3]}
#                 'Group':          line[4],
#                 'Period':         line[5],
#                 'Atomic weight':  line[6] + ' u', # atomic mass unit
#                 'Density':        line[7] + ' g/cm^3', # grams/cubic cm
#                 'Melting point':  line[8] + ' K', # kelvin
#                 'Boiling point':  line[9] + ' K', # kelvin
#                 'Specific heat capacity':      line[10] + ' J/(g*K)',
#                 'Electronegativity':           line[11],
#                 'Abundance in earth\'s crust': line[12] + ' mg/kg'}

# see funktsioon käivitatakse nupule klõpsamisel


def infokast():
    info=elements[0][2]
    messagebox.showinfo(message=info)


# loome akna
raam = Tk()
raam.title("Tabel")
raam.geometry("1000x1000")


# loome nupu
nupp = ttk.Button(raam, text="H", command=infokast)
nupp.place(x=70, y=0, width=75 , height = 75)
nupp = ttk.Button(raam, text="Li", command = infokast)
nupp.place(x=70, y= 80, width=75, height = 75)
nupp = ttk.Button(raam, text="Na", command=infokast)
nupp.place(x=70, y= 160, width=75, height = 75)
nupp = ttk.Button(raam, text="K", command=infokast)
nupp.place(x=70, y= 240, width=75, height = 75)
nupp = ttk.Button(raam, text="Rb", command=infokast)
nupp.place(x=70, y=320, width=75, height= 75)
nupp = ttk.Button(raam, text="Cs", command=infokast)
nupp.place(x=70, y=400, width=75, height = 75)
nupp = ttk.Button(raam, text="Fr", command=infokast)
nupp.place(x=70, y=480, width=75, height = 75)

# ilmutame akna ekraanile
raam.mainloop()