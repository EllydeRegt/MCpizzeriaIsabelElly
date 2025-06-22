# Po Zeeslag
# Elly de Regt

### GLOBALE VARIABELE ###

import random

spelAfgelopen = False
aantalPogingen = 0

### FUNCTIEDEFINITIE ###

def maakBord():
    invoer = input("Hoe breedt wil je het bord hebben?")
    breedte = int(invoer)                       # zet de input om in een integer
    print(breedte)
    invoer = input("Hoe hoog wil je het bord hebben?")
    hoogte = int(invoer)                        # zet de input om in een integer
    print(hoogte)
    rij = []
    for x in range(breedte):
        rij.append(" - ")                     #maakt een rij met juiste aantal kolommen
    for y in range(hoogte):
        bord = [rij] * hoogte                   #zet deze rij zovaal in het bord als je rijen wilt
    return bord, breedte, hoogte

def toonBord(hoogte, breedte):
    for kolom in range(breedte):
        print(" ", chr(65+kolom), end="")       #spatie en dan de letters boven het bord
    print()                                     #vanaf hier een enter en verder met het bord
    for x in range(hoogte):
        print(1 + x, end="")                  #de cijfers langs het bord(index 0 wordt cijfer 1)
        for y in range(breedte):
            print(bord[x][y], end="")
        print()

def plaatsSchepen(bord):
    Y = random.randint(0,3)       
    X = random.randint(0,3)          
    print(Y)
    print(X)
    bord[Y][X] = " 0 "
    return bord

# def vraagSpelerOmCoordinaten():

# def verwerkSchot():


### HOOFDPROGRAMMA ###

#maak een leeg bord
bord, breedte, hoogte = maakBord()
# breedte = int(breedteStr)
# hoogte = int(hoogteStr)

#vul bord met willekeurige schepen
print(bord)
plaatsSchepen(bord)
print(bord)
#toon bord met schepen op het scherm

#zolang spel niet is afgelopen, doe dan:
while spelAfgelopen == False:
    #vraag speler om invoer
    invoer = input("Voer een coordinaat in")
    #tel poging
    #verwerk schot: controleer of raak/mis, vertel gebruiker, pas bord aan
    #toon bord met schepen op het scherm
    toonBord(hoogte, breedte)

#spel afgelopen: geef gebruiker een compliment
if spelAfgelopen == True:
    print("Goed gespeeld!")




#vul bord met willekeurige schepen
#plaatsSchepen()
#toon bord met schepen op het scherm
#zolang spel niet is afgelopen, doe dan:
    #vraag speler om invoer
    #tel poging
    #verwerk schot: controleer of raak/mis, vertel gebruiker, pas bord aan
    #toon bord met schepen op het scherm
#spel afgelopen: geef gebruiker een compliment
