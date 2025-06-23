# Po Zeeslag
# Elly de Regt

### GLOBALE VARIABELE ###

import random

spelAfgelopen = False
aantalPogingen = 0

### FUNCTIEDEFINITIE ###

def maakBord():
    invoer = input("Hoe breedt wil je het bord hebben?")
    breedte = int(invoer)                       # int() zet de input om in een integer
    print("breedte:", breedte)
    invoer = input("Hoe hoog wil je het bord hebben?")
    hoogte = int(invoer)                        # zet de input om in een integer
    print("hoogte", hoogte)
    rij = []
    for x in range(breedte):
        rij.append(" - ")                       #maakt een rij met juiste aantal kolommen
    for y in range(hoogte):
        bord = [rij] * hoogte                   #zet deze rij zovaak in het bord als je rijen wilt
    return bord, breedte, hoogte

def toonBord(hoogte, breedte):
    for kolom in range(breedte):
        print(" ", chr(65+kolom), end="")       #spatie en dan de letters boven het bord
    print()                                     #vanaf hier een enter en verder met het bord
    for x in range(hoogte):
        print(1 + x, end="")                    #de cijfers langs het bord(index 0 wordt cijfer 1)
        for y in range(breedte):
            print(bord[x][y], end="")
        print()

def plaatsSchepen(bord):
    Y = random.randint(0,3)       
    X = random.randint(0,3)          
    print("Y", Y)
    print("X", X)
    bord[Y][X] = " 0 "                          ##WERKT NOG NIET, GEEFT HELE RIJ " 0 "
    return bord

def vraagSpelerOmCoordinaten(aantalPogingen):
    invoerX = input("Voer een letter in (de X-coordinaat)")
    invoerX = controleer_Xcoordinaat(invoerX)       #roept functie aan die controleert of letter is en hoofdletter maakt
    X_coordinaat = ord(invoerX) - 65
    invoerY = input("Voer een cijfer in (de Y-coordinaat)")
    Y_coordinaat = int(invoerY)
    print("Je hebt ingevoerd: (", invoerX, invoerY, ")")
    ingevulde_coordinaat = []
    ingevulde_coordinaat.append(X_coordinaat)
    ingevulde_coordinaat.append(Y_coordinaat)
    aantalPogingen += 1
    return aantalPogingen, ingevulde_coordinaat

def controleer_Xcoordinaat(invoer):
    geldige_coordinaat = invoer.isalpha()           # .isalpha() is een boolean die controleert of het letters uit het alphabet zijn
    if geldige_coordinaat == False:					# als de gok geen letter is
        print('Dit is geen letter, voer een letter in')
    else:
        print('gok is een letter')
    hoofdlettercheck = invoer.isupper()		        # .isupper() checkt of de letter een hoofdletter is
    if hoofdlettercheck == False:			        # als de gok een kleine letteris, wisselt hij deze om voor een hoofdletter
        invoer = invoer.swapcase()	                # .swapcase() wisselt kleine letters om voor hoofdletters en andersom
    return invoer

# def verwerkSchot():


### HOOFDPROGRAMMA ###

#maak een leeg bord
bord, breedte, hoogte = maakBord()
# breedte = int(breedteStr)
# hoogte = int(hoogteStr)

#vul bord met willekeurige schepen
print(bord)
bord = plaatsSchepen(bord)
print(bord)
toonBord(hoogte, breedte)
#toon bord met schepen op het scherm

#zolang spel niet is afgelopen, doe dan:
while spelAfgelopen == False:
    #vraag speler om invoer
    aantalPogingen, ingevulde_coordinaat = vraagSpelerOmCoordinaten(aantalPogingen)
    print("ingevulde_coordinaat:", ingevulde_coordinaat)
    #tel poging
    print("Aantal pogingen gedaan:", aantalPogingen)
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
