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
    rij = ["-"*breedte]                       #maakt een rij met juiste aantal kolommen
    for y in range(hoogte):
        bord = rij * hoogte                   #zet deze rij zovaal in het bord als je rijen wilt
    return bord, breedte, hoogte

def toonBord(hoogte, breedte):
    for kolom in range(breedte):
        print(" ", chr(65+kolom), end="")       #spatie en dan de letters boven het bord
    print()                                     #vanaf hier een enter en verder met het bord
    for rij in range(hoogte):
        print(1 + rij, end="")                  #de cijfers langs het bord
        for kolom in range(breedte):
            print(bord[rij][kolom], end="")
        print()

# def plaatsSchepen(rij1, rij2, rij3):
#     for i in rij1:
#         for i in rij2:
#             for i in rij3:
#                 p = random.choice(i)
#                 print(rij1[0:p])
#                 print(rij2[0:p])
#                 print(rij3[0:p])
#     for i in rij1:
#         for i in rij2:
#             for i in rij3:
#                 p = random.choice(i)
#                 print(rij1[1:p])
#                 print(rij2[0:p])
#                 print(rij3[0:p])
#     for i in rij1:
#         for i in rij2:
#             for i in rij3:
#                 p = random.choice(i)
#                 print(rij1[1:p])
#                 print(rij2[0:p])
#                 print(rij3[0:p])
#     return p


def plaatsSchepen(bord, breedte, hoogte):
    bord[random.choice(hoogte)][random.choice(breedte)] = "0"
    return bord

# def vraagSpelerOmCoordinaten():

# def verwerkSchot():


### HOOFDPROGRAMMA ###

#maak een leeg bord
# invoer = input("Hoe breedt wil je het bord hebben?")
# breedte = int(invoer)       # zet de input om in een integer
# print(breedte)
# invoer = input("Hoe hoog wil je het bord hebben?")
# hoogte = int(invoer)        # zet de input om in een integer
# print(hoogte)
bord, breedte, hoogte = maakBord()

#vul bord met willekeurige schepen
print(bord)
# plaatsSchepen(bord, breedte, hoogte)
#toon bord met schepen op het scherm

#zolang spel niet is afgelopen, doe dan:
while spelAfgelopen == False:
    #vraag speler om invoer
    invoer = input("Voer een coordinaat in")
    print(invoer)
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
