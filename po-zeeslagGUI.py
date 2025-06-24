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
    bord = []
    for y in range(hoogte):
        rij = []
        for x in range(breedte):
            rij.append(" - ")  
        bord.append(rij)                     #maakt een rij met juiste aantal kolommen
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

def plaatsSchepen(bord, breedte, hoogte):
    schepen_geplaatst = 0
    while schepen_geplaatst < 3:
        Y = random.randint(0,(hoogte - 1))       # kiest een random Y-coordinaat
        X = random.randint(0,(breedte - 1))      # kiest een random X-coordinaat
        schepen_omheen = geenSchepenRond(bord, Y, X)
        if (bord[Y][X] == " - ") and (schepen_omheen == False):     # zorgt ervoor dat alleen een schip wordt geplaatst waar nog geen schip ligt
            bord[Y][X] = " 0 "
            schepen_geplaatst += 1
    return bord

def geenSchepenRond(bord, Y, X):
    schepen_omheen = False
    verschuivingen = [-1, 0, 1]
    for dy in verschuivingen:
        naastY = Y + dy
        for dx in verschuivingen:
            naastX = X + dx
            if (0 <= naastY and naastY < hoogte) and (0 <= naastX and naastX < breedte):    #zorgt dat er geen foutmelding komt aan de rand van het bord
                if bord[naastY][naastX] == " 0 ":
                    schepen_omheen = True
    return schepen_omheen


def vraagSpelerOmCoordinaten():
    goeieGok = False
    geldige_Xcoordinaat = False
    geldige_Ycoordinaat = False
    while goeieGok == False:
        while geldige_Xcoordinaat == False:             # terwijl er nog geen geldige X-coordinaat is ingevuld blijft hij ernaar vragen
            invoerX = input("Voer een letter in (de X-coordinaat)")
            invoerX, geldige_Xcoordinaat = controleer_Xcoordinaat(invoerX)       #roept functie aan die controleert of letter is en hoofdletter maakt
        X_coordinaat = ord(invoerX) - 65
        while geldige_Ycoordinaat == False:             # terwijl er nog geen geldige Y-coordinaat is ingevuld blijft hij ernaar vragen
            invoerY = input("Voer een cijfer in (de Y-coordinaat)")
            invoerY, geldige_Ycoordinaat = controleer_Ycoordinaat(invoerY)      #roept functie aan die controleert of cijfer is
        Y_coordinaat = int(invoerY) - 1
        if ((Y_coordinaat + 1) > len(bord)) or ((X_coordinaat +1 ) > len(bord[0])): # controleert of de coordinaten op het bord liggen
            print("Sorry, deze coordinaten liggen niet op het bord, probeer opnieuw")
            geldige_Xcoordinaat = False
            geldige_Ycoordinaat = False
        else:
            print("Je hebt ingevoerd: (", invoerX, invoerY, ")")
            goeieGok = True
    ingevulde_coordinaat = []                       # zet de coordinaat in een lijst als [X_coordinaat, Y_coordinaat]
    ingevulde_coordinaat.append(X_coordinaat)
    ingevulde_coordinaat.append(Y_coordinaat)
    return ingevulde_coordinaat

def controleer_Xcoordinaat(invoer):
    geldige_Xcoordinaat = invoer.isalpha()          # .isalpha() is een boolean die controleert of het letters uit het alphabet zijn
    if geldige_Xcoordinaat == False:                # als de gok geen letter is
        print('Dit is geen letter, voer een letter in')
    else:
        if len(invoer) > 1:                         # controleert of de invoer 1 teken is     
            print("Dit is meer dan 1 letter, voer 1 letter in")
        else:
            print('gok is een letter')
            invoer = invoer.upper()                 # maakt van de invoer hoofdletters
            geldige_Xcoordinaat == True
    return invoer, geldige_Xcoordinaat

def controleer_Ycoordinaat(invoer):
    geldige_Ycoordinaat = invoer.isdigit()          # .isdigit() is een boolean die controleert of het hele, positieve getallen zijn
    if geldige_Ycoordinaat == False:
        print("Dit is geen geldig getal, voer een getal in")
    else:
        if len(invoer) > 1:                         # controleert of de invoer 1 teken is 
            print("Dit is meer dan 1 getal, voer 1 getal in")
        else:
            print('gok is een getal')
            geldige_Ycoordinaat == True
    return invoer, geldige_Ycoordinaat

def verwerkSchot(bord, ingevulde_coordinaat):
    Y = ingevulde_coordinaat[1]
    X = ingevulde_coordinaat[0]
    if bord[Y][X] == " 0 ": # als er op de ingevulde coordinaat een "0" ligt (een schip)
        print("Raak! Op deze coordinaat lag een schip!")
    else: print("Helaas!, dit was mis, probeer opnieuw!")




### HOOFDPROGRAMMA ###

#maak een leeg bord
bord, breedte, hoogte = maakBord()
# breedte = int(breedteStr)
# hoogte = int(hoogteStr)

#vul bord met willekeurige schepen
print(bord)
bord = plaatsSchepen(bord, breedte, hoogte)
print(bord)
toonBord(hoogte, breedte)
#toon bord met schepen op het scherm

#zolang spel niet is afgelopen, doe dan:
while spelAfgelopen == False:
    #vraag speler om invoer
    ingevulde_coordinaat = vraagSpelerOmCoordinaten()
    print("ingevulde_coordinaat:", ingevulde_coordinaat)
    #tel poging
    print("Aantal pogingen gedaan:", aantalPogingen)
    #verwerk schot: controleer of raak/mis, vertel gebruiker, pas bord aan
    verwerkSchot(bord, ingevulde_coordinaat)
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
