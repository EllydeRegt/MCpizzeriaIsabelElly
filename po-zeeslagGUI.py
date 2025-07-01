# Po Zeeslag
# Elly de Regt

### GLOBALE VARIABELE ###

import random

spelAfgelopen = False
aantalPogingen = 0

### FUNCTIEDEFINITIE ###

def maakBord():
    # invoer = input("Hoe breedt wil je het bord hebben?")
    # breedte = int(invoer)                       # int() zet de input om in een integer
    # print("breedte:", breedte)
    # invoer = input("Hoe hoog wil je het bord hebben?")
    # hoogte = int(invoer)                        # zet de input om in een integer
    # print("hoogte", hoogte)
    breedte = 10
    hoogte = 10
    bord = []
    for y in range(hoogte):
        rij = []
        for x in range(breedte):
            rij.append(" - ")  
        bord.append(rij)                        #maakt een rij met juiste aantal kolommen
    return bord, breedte, hoogte

def toonBord(bord, hoogte, breedte):
    for kolom in range(breedte):
        print(" ", chr(65+kolom), end="")       #spatie en dan de letters boven het bord
    print()                                     #vanaf hier een enter en verder met het bord
    for x in range(hoogte):
        print(1 + x, end="")                    #de cijfers langs het bord(index 0 wordt cijfer 1)
        for y in range(breedte):
            print(bord[x][y], end="")
        print()

#############TEST#####TEST#############TEST#############TEST

def plaatsSchip(bord, breedte, hoogte, lengte_schip):
    richtingen = ["verticaal", "horizontaal"]
    schip_geplaatst = False
    while schip_geplaatst == False:
        richting = random.choice(richtingen)    # kiest een random richting
        if richting == "horizontaal":
            Y = [random.randint(0,(hoogte - 1))]                      # kiest een random Y-coordinaat
            X = [random.randint(0,(breedte - lengte_schip))]          # kiest een random X-coordinaat
            for i in range(lengte_schip - 1):   # -1 omdat er al 1 waarde in de lijst staat
                volgende_X = X[-1] + 1          # X[-1] refereert naar het laatste item in de lijst
                X.append(volgende_X)
            Y = Y * len(X)
        elif richting == "verticaal":
            Y = [random.randint(0,(hoogte - lengte_schip))]
            X = [random.randint(0,(breedte - 1))]
            for i in range(lengte_schip - 1):   # -1 omdat er al 1 waarde in de lijst staat
                volgende_Y = Y[-1] + 1          # Y[-1] refereert naar het laatste item in de lijst
                Y.append(volgende_Y)
            X = X * len(Y)
        # lijsten met coordinaten gemaakt, nu controleren of vrij en schip plaatsen
        schepen_omheen = geenSchepenRond(bord, Y, X, hoogte, breedte)
        if schepen_omheen == False:
            for y in Y:
                for x in X:
                    bord[y][x] = " 0 "
            schip_geplaatst = True
    return bord, Y, X


# coordinatenSchip = []
# for i in X:
#     coordinaat = []
#     coordinaat.append(X[i], Y[i])



def geenSchepenRond(bord, Y, X, hoogte, breedte):
    schepen_omheen = False

    for y in Y:
        for x in X:
            for dy in range(y-1, y + 2):
                for dx in range(x-1, x + 2):
                    if (0 <= dy and dy < hoogte) and (0 <= dx and dx < breedte):
                        if bord[dy][dx] == " 0 ":
                            schepen_omheen = True

    # for y in Y:
    #     for i in range(-1, 2):
    #         dy = y + i
    #         for x in X:
    #             for i in range(-1, 2):
    #                 dx = x + i
    #                 if (0 <= dy and dy < hoogte) and (0 <= dx and dx < breedte):
    #                     if bord[dy][dx] == " 0 ":
    #                         schepen_omheen = True
    return schepen_omheen


def plaats_schepen(bord, breedte, hoogte):
    bord, Y, X = plaatsSchip(bord, breedte, hoogte, 2)
    schip1 = []
    for i in range(len(Y)):
        coordinaat = [Y[i], X[i]]
        schip1.append(coordinaat)
    print("schip1", schip1)
    bord, Y, X = plaatsSchip(bord, breedte, hoogte, 3)
    schip2 = []
    for i in range(len(Y)):
        coordinaat = [Y[i], X[i]]
        schip2.append(coordinaat)
    print("schip2", schip2)
    bord, Y, X = plaatsSchip(bord, breedte, hoogte, 3)
    schip3 = []
    for i in range(len(Y)):
        coordinaat = [Y[i], X[i]]
        schip3.append(coordinaat)
    print("schip3", schip3)
    bord, Y, X = plaatsSchip(bord, breedte, hoogte, 4)
    schip4 = []
    for i in range(len(Y)):
        coordinaat = [Y[i], X[i]]
        schip4.append(coordinaat)
    print("schip4", schip4)
    bord, Y, X = plaatsSchip(bord, breedte, hoogte, 5)
    schip5 = []
    for i in range(len(Y)):
        coordinaat = [Y[i], X[i]]
        schip5.append(coordinaat)
    print("schip5", schip5)
    return bord, schip1, schip2, schip3, schip4, schip5


def vraagSpelerOmCoordinaten(aantalPogingen, hoogte, breedte):
    goeieGok = False
    geldige_Xcoordinaat = False
    geldige_Ycoordinaat = False
    while goeieGok == False:                    # terwijl er nog geen geldige gok is gedaan blijft hij ernaar vragen
        while geldige_Xcoordinaat == False:     # terwijl er nog geen geldige X-coordinaat is ingevuld blijft hij ernaar vragen
            invoerX = input("Voer een letter in (de X-coordinaat)").strip()             # .strip() haalt onoidge spaties voor en achter de invoer weg
            invoerX, geldige_Xcoordinaat = controleer_Xcoordinaat(invoerX)              #roept functie aan die controleert of letter is en hoofdletter maakt
        X_coordinaat = ord(invoerX) - 65
        while geldige_Ycoordinaat == False:     # terwijl er nog geen geldige Y-coordinaat is ingevuld blijft hij ernaar vragen
            invoerY = input("Voer een cijfer in (de Y-coordinaat)").strip()             # .strip() haalt onodige spaties voor en achter de invoer weg
            invoerY, geldige_Ycoordinaat = controleer_Ycoordinaat(invoerY)              #roept functie aan die controleert of cijfer is    
        Y_coordinaat = int(invoerY) - 1
        if ((Y_coordinaat + 1) > hoogte) or ((X_coordinaat +1 ) > breedte):     # controleert of de coordinaten op het bord liggen
            print("Sorry, deze coordinaten liggen niet op het bord, probeer opnieuw")
            geldige_Xcoordinaat = False
            geldige_Ycoordinaat = False
        else:
            print("Je hebt ingevoerd: (", invoerX, invoerY, ")")
            goeieGok = True
            aantalPogingen += 1
    ingevulde_coordinaat = []                    # zet de coordinaat in een lijst als [X_coordinaat, Y_coordinaat]
    ingevulde_coordinaat.append(X_coordinaat)
    ingevulde_coordinaat.append(Y_coordinaat)
    return ingevulde_coordinaat, aantalPogingen

def controleer_Xcoordinaat(invoer):
    geldige_Xcoordinaat = invoer.isalpha()       # .isalpha() is een boolean die controleert of het letters uit het alphabet zijn
    if geldige_Xcoordinaat == False:             # als de gok geen letter is
        print('Dit is geen letter, voer een letter in')
    else:
        if len(invoer) > 1:                      # controleert of de invoer 1 teken is     
            print("Dit is meer dan 1 letter, voer 1 letter in")
            geldige_Xcoordinaat = False
        else:
            print('gok is een letter')
            invoer = invoer.upper()              # maakt van de invoer hoofdletters
            geldige_Xcoordinaat = True
    return invoer, geldige_Xcoordinaat

def controleer_Ycoordinaat(invoer):
    geldige_Ycoordinaat = invoer.isdigit()       # .isdigit() is een boolean die controleert of het hele, positieve getallen zijn
    if geldige_Ycoordinaat == False:
        print("Dit is geen geldig getal, voer een getal in")
    else:
        # if len(invoer) > 1 and invoer != 10:                      # controleert of de invoer 1 teken is 
        #     print("Dit is meer dan 1 getal, voer 1 getal in")
        #     geldige_Ycoordinaat = False
        # else:
            print('gok is een getal')
            geldige_Ycoordinaat = True
    return invoer, geldige_Ycoordinaat

def verwerkSchot(bord, ingevulde_coordinaat, speelBord, alle_schepen):
    Y = ingevulde_coordinaat[1]
    X = ingevulde_coordinaat[0]
    if bord[Y][X] == " 0 ":                        # als er op de ingevulde coordinaat een "0" ligt (een schip)
        print("Raak! Op deze coordinaat lag een schip!")
        speelBord[Y][X] = " 0 "
        print("alle_schepen", alle_schepen)
        for schip in alle_schepen:
            if [Y, X] in schip:
                schip.remove([Y, X])
                if schip == []:
                    print("Schip is gezonken")
        print("alle_schepen", alle_schepen)
    else: 
        print("Helaas!, dit was mis, probeer opnieuw!")
        speelBord[Y][X] = " / "
    # for y in range(9):
    #     for x in range(9):
    #         if speelBord[y][x] == bord[y][x]:
    #             print("Hoera! Alle schepen zijn gezonken")
    return speelBord

def eindeSpel_controle(alle_schepen, spelAfgelopen):
    for schip in alle_schepen:
        if schip != []:         # als er een schip is dat nog niet is gezonken (en dus nog coordinaten heeft in de lijst)
            spelAfgelopen = False
        else:
            spelAfgelopen = True
    return spelAfgelopen
    



# def eindeSpel_controle(bord, speelBord):
#     speelBord = speelBord.replace(" / ", " - ")
#     if speelBord == bord:
#         print("Je hebt gewonnen! Einde spel!")
#         spelAfgelopen = True
#     return spelAfgelopen


### HOOFDPROGRAMMA ###

#maak een leeg bord
bord, breedte, hoogte = maakBord()
speelBord, breedte, hoogte = maakBord()
# breedte = int(breedteStr)
# hoogte = int(hoogteStr)

#vul bord met willekeurige schepen

# lengte_schip = 2
# schepen_geplaatst = 0
# # Xcoordinaten_schepen = []
# # Ycoordinaten_schepen = []
# while schepen_geplaatst < 4:
#     bord, Y, X = plaatsSchip(bord, breedte, hoogte, lengte_schip)
#     print("Y:", Y, "X:", X)
#     # for i in range(len(X)):
#     #     Xcoordinaten_schepen.append(X)
#     #     Ycoordinaten_schepen.append(Y)
#     lengte_schip += 1
#     schepen_geplaatst += 1
# # print("Xcoordinaten_schepen:", Xcoordinaten_schepen)
# # print("Ycoordinaten_schepen:", Ycoordinaten_schepen)
# bord, Y, X = plaatsSchip(bord, breedte, hoogte, 3)

bord, schip1, schip2, schip3, schip4, schip5 = plaats_schepen(bord, breedte, hoogte)
alle_schepen = [schip1, schip2, schip3, schip4, schip5]
toonBord(bord, hoogte, breedte)
toonBord(speelBord, hoogte, breedte)    #toon bord met schepen op het scherm

#zolang spel niet is afgelopen, doe dan:
while spelAfgelopen == False:
    ingevulde_coordinaat, aantalPogingen = vraagSpelerOmCoordinaten(aantalPogingen, hoogte, breedte)
    print("Aantal pogingen gedaan:", aantalPogingen)
    speelBord = verwerkSchot(bord, ingevulde_coordinaat, speelBord, alle_schepen)
    spelAfgelopen = eindeSpel_controle(alle_schepen, spelAfgelopen)
    toonBord(speelBord, hoogte, breedte)

#spel afgelopen: geef gebruiker een compliment
if spelAfgelopen == True:
    print("Goed gespeeld!")
    print("Je hebt in ", aantalPogingen, "pogingen geraden waar alle schepen lagen")
    print("Dit was hoe de schepen waren geplaatst")
    toonBord(bord, hoogte, breedte)




#vul bord met willekeurige schepen
#plaatsSchepen()
#toon bord met schepen op het scherm
#zolang spel niet is afgelopen, doe dan:
    #vraag speler om invoer
    #tel poging
    #verwerk schot: controleer of raak/mis, vertel gebruiker, pas bord aan
    #toon bord met schepen op het scherm
#spel afgelopen: geef gebruiker een compliment
