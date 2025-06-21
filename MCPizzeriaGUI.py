# Dit bestand zorgt voor de gebruikersinterface (GUI)van onze programma.
# Vul hier de naam van je programma in:
#
#
# Vul hier jullie namen in:
# Isabel en Elly
#
#


### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import MCpizzeriaSQL


### ---------  Functie definities  -----------------

def zoekKlant():
    gevonden_klantnaam = MCpizzeriaSQL.zoekKlantInTabel(ingevoerde_klantnaam.get())
    print("gevonden klanten", gevonden_klantnaam)
    invoerVeldKlantnaam.delete(0, END) #invoerveld voor naam leeg maken
    invoerveldKlantNr.delete(0, END) #invoerveld voor klantNr leeg maken
    for rij in gevonden_klantnaam: #voor elke rij dat de query oplevert
         #toon klantnummer, de eerste kolom uit het resultaat in de invoerveld
         invoerveldKlantNr.insert(END, rij[0]) 
         #toon klantAchternaam, de tweede kolom uit het resultaat in de invoerveld
         invoerVeldKlantnaam.insert(END, rij[1]) 

def zoekPizzanaam():
    gevonden_pizzanaam = MCpizzeriaSQL.zoekPizzaInTabel(ingevoerde_pizzanaam.get())
    print("gevonden pizzanaam", gevonden_pizzanaam)
    invoerVeldPizzanaam.delete(0, END) #invoerveld voor pizzanaam leegmaken
    for rij in gevonden_pizzanaam: #voor elke rij dat de query oplevert
        #toon pizzanaam, de eerste kolom uit het resultaat in het invoerveld
        invoerVeldPizzanaam.insert(END, rij[1])

def toonMenuInListbox():
    listboxMenu.delete(0, END) #maak de listbox leeg
    pizza_tabel = MCpizzeriaSQL.vraagOpGegevensPizzaTabel()
    for regel in pizza_tabel:
        listboxMenu.insert(END, regel) #voeg elke regel uit resultaat in listboxMenu
    listboxMenu.insert(0, "ID Gerecht Prijs")

### functie voor het selecteren van een rij uit de listbox en deze in een andere veld te plaatsen
def haalGeselecteerdeRijOp(event):
    #bepaal op welke regel er geklikt is
    geselecteerdeRegelInLijst = listboxMenu.curselection()[0] 
    #haal tekst uit die regel
    geselecteerdeTekst = listboxMenu.get(geselecteerdeRegelInLijst) 
    #verwijder tekst uit veld waar je in wilt schrijven, voor het geval er al iets staat
    invoerveldGeselecteerdePizza.delete(0, END) 
    #zet tekst in veld
    invoerveldGeselecteerdePizza.insert(0, geselecteerdeTekst)

def toonWinkelwagenInListbox():
    listboxWinkelwagen.delete(0, END),  #maak de listbox leeg
    winkelWagen_tabel = MCpizzeriaSQL.vraagOpGegevensWinkelWagenTabel
    for regel in winkelWagen_tabel:
        listboxWinkelwagen.insert(END, regel)   #voeg elke regel uit resultaat in listboxWinkelwagen

#voeg de bestelling van klant met gekozen pizza en aantal toe 
#in de winkelwagentabel
#en toon de bestelling in de listbox op het scherm
def voegToeAanWinkelWagen():
    klantNr = invoerveldKlantNr.get()
    gerechtID = ingevoerde_pizzanaam.get()
    aantal = aantalGekozen.get()
    MCpizzeriaSQL.voegToeAanWinkelWagen(klantNr, gerechtID, aantal )
    winkelwagen_tabel = MCpizzeriaSQL.vraagOpGegevensWinkelWagenTabel()
    listboxWinkelwagen.delete(0, END) #listbox eerst even leeg maken
    for regel in winkelwagen_tabel:
        listboxWinkelwagen.insert(END, regel)

## !! def verwijderUitWinkelWagen():  !! ##


### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico")
venster.wm_title("Po Zeeslag")

labelIntro = Label(venster, text="Welkom!")
labelIntro.grid(row=0, column=0, sticky="W")

klantNaam = Label(venster, text="klantnaam:")
klantNaam.grid(row=1, column=0)

ingevoerde_klantnaam = StringVar ()
invoerVeldKlantnaam = Entry(venster, textvariable= ingevoerde_klantnaam)
invoerVeldKlantnaam.grid(row=1, column=1, sticky="W")

KnopZoekOpKlantnaam = Button(venster, text="Zoek klant", width= 12, command= zoekKlant)
KnopZoekOpKlantnaam.grid(row=1, column=3)


klantNr = Label(venster, text="klantnummer:")
klantNr.grid(row=2, column=0)

invoerveldKlantNr = Entry(venster)
invoerveldKlantNr.grid(row=2, column=1, sticky="W")

Pizzanaam = Label(venster, text="Pizzanaam")
Pizzanaam.grid(row= 3, column= 0)

ingevoerde_pizzanaam = StringVar ()
invoerVeldPizzanaam = Entry(venster, textvariable= ingevoerde_pizzanaam)
invoerVeldPizzanaam.grid(row= 3, column= 1, sticky= "W")

KnopZoekPizzanaam = Button(venster, text= "Zoek Pizza", width= 12, command= zoekPizzanaam)
KnopZoekPizzanaam.grid(row= 3, column= 3)

Mogelijkheden = Label(venster, text="Mogelijkheden:")
Mogelijkheden.grid(row= 4, column= 0)

listboxMenu = Listbox(venster, height= 6, width= 50)
listboxMenu.grid(row=4, column=1, rowspan= 6, columnspan= 2, sticky= "W")
listboxMenu.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)

scrollbarlistbox = Scrollbar(venster)
scrollbarlistbox.grid(row=4, column=2, rowspan=6, sticky="E")
listboxMenu.config(yscrollcommand=scrollbarlistbox.set)
scrollbarlistbox.config(command=listboxMenu.yview)

knopToonPizzas = Button(venster, text="Toon alle pizza's", width=12, command=toonMenuInListbox)
knopToonPizzas.grid(row=4, column=3)

GekozenPizza = Label(venster, text="Gekozen Pizza:")
GekozenPizza.grid(row= 10, column= 0)

ingevoerde_geselecteerdePizza = StringVar()
invoerveldGeselecteerdePizza = Entry(venster, textvariable= ingevoerde_pizzanaam)
invoerveldGeselecteerdePizza.grid(row= 10, column= 1, sticky= "W")

Aantal = Label(venster, text= "Aantal:")
Aantal.grid(row= 11, column= 0)

aantalGekozen = IntVar()    #het is een getal
aantalGekozen.set(1)    #standaard geselecteerde waarde
OptionMenuPizzaAantal = OptionMenu(venster, aantalGekozen, 1, 2, 3)
OptionMenuPizzaAantal.grid(row= 11, column=1)

Winkelwagen = Label(venster, text="Winkelwagen:")
Winkelwagen.grid(row=12, column= 0)

listboxWinkelwagen = Listbox(venster, height= 6, width= 50)
listboxWinkelwagen.grid(row=12, column=1, rowspan= 6, columnspan= 2, sticky= "W")
listboxWinkelwagen.bind('<<ListboxSelect>>', toonWinkelwagenInListbox)

knopVoegToeAanWinkelWagen = Button(venster, text="Voeg toe", width=12, command=voegToeAanWinkelWagen)
knopVoegToeAanWinkelWagen.grid(row=12, column=4)






knopSluit = Button(venster, text= "Sluiten", width= 12, command= venster.destroy)
knopSluit.grid(row= 17, column= 4)


#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
