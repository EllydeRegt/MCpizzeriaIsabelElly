# Po Zeeslag
# Elly de Regt

### GLOBALE VARIABELE ###

import random

### FUNCTIEDEFINITIE ###

def maakBord(aantalKolommen, aantalRijen):
    bord = []
    rij = ["-"*aantalKolommen]
    for y in range(aantalRijen):
       bord.append(rij)
    print("leeg bord gemaakt")
    # bord = [ ["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"] ]
    return bord

def toonBord(lengte, breedte):
    for rij in range(lengte):
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

def plaatsSchepen(bord):
    bord[random.choice(bord)][random.choice(bord)] = "0"
    return bord

# def vraagSpelerOmCoordinaten():

# def verwerkSchot():


### HOOFDPROGRAMMA ###
        #maak een leeg bord
breedte = 3
lengte = 3
bord = maakBord(breedte, lengte)
toonBord(lengte, breedte)

        #vul bord met willekeurige schepen
#plaatsSchepen()

        #toon bord met schepen op het scherm
        #zolang spel niet is afgelopen, doe dan:
        #vraag speler om invoer
        #tel poging
        #verwerk schot: controleer of raak/mis, vertel gebruiker, pas bord aan
        #toon bord met schepen op het scherm
        #spel afgelopen: geef gebruiker een compliment
