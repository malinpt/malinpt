# impordi tk vidinad ja konstandid
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv, sys, re

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
    info=elements[0]
    messagebox.showinfo(message=info)


# loome akna
raam = Tk()
raam.title("Tabel")
raam.geometry("500x500")


# loome nupu
nupp = ttk.Button(raam, text="Na", command=infokast)
nupp.place(x=70, y=40, width=150)

# ilmutame akna ekraanile
raam.mainloop()