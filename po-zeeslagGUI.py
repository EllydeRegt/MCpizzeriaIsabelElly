# Po Zeeslag
# Elly de Regt

### GLOBALE VARIABELE ###

import random
import turtle

turtle.hideturtle()
turtle.pencolor("blue")     
turtle.speed(0)             # Zet de snelheid op maximaal om snel te tekenen

HOKJE = 30
BORD_GROOTTE = 300
START_X = -BORD_GROOTTE / 2
START_Y = BORD_GROOTTE / 2

SCHIP = " 0 "
WATER = " - "
MIS = " / "
RAAK_KLEUR = "red"
MIS_KLEUR = "blue"
GERADEN_SCHIP = "green"

spelAfgelopen = False
aantalPogingen = 0

### FUNCTIEDEFINITIE ###

def spelUitleg():
    print("Je gaat het spel zeeslag spelen. Ik leg uit hoe het werkt")
    print("Je vijand heeft een vloot, je weet niet precies waar, maar wel welke schepen")
    print("Een schip van 2 hokjes lang, twee van 3 hokjes, een van 4 en een van 5 hokjes")
    print("Je wilt de vloot tot zinken brengen, door steeds een 'schot' te schieten")
    print("Voer steeds een coordinaat in, bestaande uit een letter en een cijfer")
    print("Totdat je alle delen van het schip hebt geraakt zinkt het niet")
    print("Probeer alle schepen in het veld tot zinken te brengen")
    print("Ik zal het laten weten als een schip is geraakt, en als een schip is gezonken")
    print("Probeer in zo min mogelijk pogingen de vloot tot zinken te brengen.")
    print("Veel succes!")

def maakBord():
    breedte = 10
    hoogte = 10
    bord = []
    for y in range(hoogte):
        rij = []
        for x in range(breedte):
            rij.append(WATER)                   #maakt een rij met juiste aantal kolommen
        bord.append(rij)
    teken_bord(hoogte, breedte)
    return bord, breedte, hoogte

# print het bord, nu niet meer nodig vanwege de turtle die later is toegevoegd
def toonBord(bord, hoogte, breedte):
    for kolom in range(breedte):
        print(" ", chr(65+kolom), end="")       #spatie en dan de letters boven het bord
    print()                                     #vanaf hier een enter en verder met het bord
    for x in range(hoogte):
        print(1 + x, end="")                    #de cijfers langs het bord(index 0 wordt cijfer 1)
        for y in range(breedte):
            print(bord[x][y], end="")
        print()

# plaatst een schip met een gegeven lengte op een random plek op het bord
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
                    bord[y][x] = SCHIP
            schip_geplaatst = True
    return bord, Y, X

# controleert of het schip geen ander schip zal raken, voordat het geplaatst wordt
def geenSchepenRond(bord, Y, X, hoogte, breedte):
    schepen_omheen = False
    for y in Y:
        for i in range(-1, 2):
            dy = y + i
            for x in X:
                for i in range(-1, 2):
                    dx = x + i
                    if (0 <= dy and dy < hoogte) and (0 <= dx and dx < breedte):
                        if bord[dy][dx] == SCHIP:
                            schepen_omheen = True
    return schepen_omheen


def plaats_schepen(bord, breedte, hoogte):
    bord, Y, X = plaatsSchip(bord, breedte, hoogte, 2)
    schip1 = []
    for i in range(len(Y)):
        coordinaat = [X[i], Y[i]]
        schip1.append(coordinaat)
    print("schip1", schip1)
    bord, Y, X = plaatsSchip(bord, breedte, hoogte, 3)
    schip2 = []
    for i in range(len(Y)):
        coordinaat = [X[i], Y[i]]
        schip2.append(coordinaat)
    print("schip2", schip2)
    bord, Y, X = plaatsSchip(bord, breedte, hoogte, 3)
    schip3 = []
    for i in range(len(Y)):
        coordinaat = [X[i], Y[i]]
        schip3.append(coordinaat)
    print("schip3", schip3)
    bord, Y, X = plaatsSchip(bord, breedte, hoogte, 4)
    schip4 = []
    for i in range(len(Y)):
        coordinaat = [X[i], Y[i]]
        schip4.append(coordinaat)
    print("schip4", schip4)
    bord, Y, X = plaatsSchip(bord, breedte, hoogte, 5)
    schip5 = []
    for i in range(len(Y)):
        coordinaat = [X[i], Y[i]]
        schip5.append(coordinaat)
    print("schip5", schip5)
    return bord, schip1, schip2, schip3, schip4, schip5


def vraag_speler_om_coordinaten(aantalPogingen, hoogte, breedte):
    goeieGok = False
    geldige_X = False
    geldige_Y = False
    while goeieGok == False:          # terwijl er nog geen geldige gok is gedaan blijft hij ernaar vragen
        while geldige_X == False:     # terwijl er nog geen geldige X-coordinaat is ingevuld blijft hij ernaar vragen
            invoerX = input("Voer een letter in (de X-coordinaat)").strip()             # .strip() haalt onoidge spaties voor en achter de invoer weg
            invoerX, geldige_X = controleer_X(invoerX)              #roept functie aan die controleert of letter is en hoofdletter maakt
        X_coordinaat = ord(invoerX) - 65
        while geldige_Y == False:     # terwijl er nog geen geldige Y-coordinaat is ingevuld blijft hij ernaar vragen
            invoerY = input("Voer een cijfer in (de Y-coordinaat)").strip()             # .strip() haalt onodige spaties voor en achter de invoer weg
            invoerY, geldige_Y = controleer_Y(invoerY)              #roept functie aan die controleert of cijfer is    
        Y_coordinaat = int(invoerY) - 1
        if ((Y_coordinaat + 1) > hoogte) or ((X_coordinaat +1 ) > breedte):     # controleert of de coordinaten op het bord liggen
            print("Sorry, deze coordinaten liggen niet op het bord, probeer opnieuw")
            geldige_X = False
            geldige_Y = False
        else:
            print("Je hebt ingevoerd: (", invoerX, invoerY, ")")
            if speelBord[Y_coordinaat][X_coordinaat] == WATER:    # controleert of de coordinaat al is ingevoerd
                aantalPogingen += 1
                goeieGok = True
            else:
                print("Deze coordinaat heb je al eens ingevoerd")
                geldige_X = False
                geldige_Y = False
    ingevulde_coordinaat = []                    # zet de coordinaat in een lijst als [X_coordinaat, Y_coordinaat]
    ingevulde_coordinaat.append(X_coordinaat)
    ingevulde_coordinaat.append(Y_coordinaat)
    return ingevulde_coordinaat, aantalPogingen

def controleer_X(invoer):
    geldige_X = invoer.isalpha()       # .isalpha() is een boolean die controleert of het letters uit het alphabet zijn
    if geldige_X == False:             # als de gok geen letter is
        print('Dit is geen letter, voer een letter in')
    else:
        if len(invoer) > 1:                      # controleert of de invoer 1 teken is     
            print("Dit is meer dan 1 letter, voer 1 letter in")
            geldige_X = False
        else:
            print('gok is een letter')
            invoer = invoer.upper()              # maakt van de invoer hoofdletters
            geldige_X = True
    return invoer, geldige_X

def controleer_Y(invoer):
    geldige_Y = invoer.isdigit()       # .isdigit() is een boolean die controleert of het hele, positieve getallen zijn
    if geldige_Y == False:
        print("Dit is geen geldig getal, voer een getal in")
    else:
            ###!! DEZE CODE WERKT NIET MEER MET GETAL 10, DAAROM IN COMMENTAAR !!!###
        # if len(invoer) > 1 and invoer != 10:                      # controleert of de invoer 1 teken is 
        #     print("Dit is meer dan 1 getal, voer 1 getal in")
        #     geldige_Ycoordinaat = False
        # else:
            print('gok is een getal')
            geldige_Y = True
    return invoer, geldige_Y

def verwerkSchot(bord, ingevulde_coordinaat, speelBord, alle_schepen):
    Y = ingevulde_coordinaat[1]
    X = ingevulde_coordinaat[0]
    if bord[Y][X] == SCHIP:                        # als er op de ingevulde coordinaat een "0" ligt (een schip)
        print("Raak! Op deze coordinaat lag een schip!")
        teken_hokje(X, Y, RAAK_KLEUR)
        speelBord[Y][X] = SCHIP                    # toont op het speelBord wat er geraakt is
        print("alle_schepen", alle_schepen)
        for schip in alle_schepen:                 # controleert voor ieder schip of de coordinaat op dat schip ligt
            if [X, Y] in schip:
                schip.remove([X, Y])               # .remove() verwijdert de geraakte coordinaat uit de lijst van dat schip
                if schip == []:
                    print("Schip is gezonken")
        print("alle_schepen", alle_schepen)
    else: 
        print("Helaas!, dit was mis, probeer opnieuw!")
        teken_hokje(X, Y, MIS_KLEUR)
        speelBord[Y][X] = MIS
    return speelBord

def controleer_einde_spel(alle_schepen):
    spelAfgelopen = True
    for schip in alle_schepen:
        if schip != []:         # als er een schip is dat nog niet is gezonken (en dus nog coordinaten heeft in de lijst)
            spelAfgelopen = False
    return spelAfgelopen


def teken_bord(hoogte, breedte):  
    # tekent de horizontale lijnen 
    for rij in range(hoogte + 1):
        turtle.penup()
        turtle.goto(START_X, START_Y - rij * HOKJE)
        turtle.pendown()
        turtle.forward(BORD_GROOTTE)
    # Hij 'tekent' de letters naast het bord
    for rij in range(hoogte):
        turtle.penup()
        turtle.goto(START_X - 15, START_Y - rij * HOKJE - 15)    # - 15 zorgt ervoor dat de letters netjes naast het bijbehorende hokje en niet op het bord komen
        turtle.pendown()                         
        turtle.write(chr(65 + rij), align="right", font=("Arial", 12, "normal"))    #.write laat turtle typen
    
    # vanaf hier de verticale lijnen
    turtle.right(90)
    for kolom in range(breedte + 1):
        turtle.penup()
        turtle.goto(START_X + kolom * HOKJE, START_Y)
        turtle.pendown()
        turtle.forward(BORD_GROOTTE)
    # hij 'tekent' de cijfers boven het bord
    for kolom in range(breedte):
        turtle.penup()
        turtle.goto(START_X + kolom * HOKJE  + 15, START_Y + 15)  # + 15 zorgt ervoor dat de cijfers netjes boven het bijbehorende hokje en niet op het bord komen
        turtle.pendown()                                       
        turtle.write(str((kolom + 1)), align="center", font=("Arial", 12, "normal"))    # str() is nodig omdat je met "" de variabele kolom niet kan gebruiken
    turtle.penup()
    turtle.home()
    

###### functie werkt, maar is niet nodig omdat speler zelf schepen 'onthult' ###########
# def teken_schip(X, Y):
#     print("X:", X, "Y:", Y)
#     turtle.fillcolor(GERADEN_SCHIP)
#     for x in X:
#         for y in Y:
#             turtle.begin_fill()
#             turtle.penup()
#             turtle.goto(START_X + x * HOKJE, START_Y - y * HOKJE)
#             turtle.pendown()
#             turtle.forward(HOKJE)
#             turtle.right(90)
#             turtle.forward(HOKJE)
#             turtle.right(90)
#             turtle.forward(HOKJE)
#             turtle.right(90)
#             turtle.forward(HOKJE)
#             turtle.right(90)
#             turtle.end_fill()
#             turtle.penup()
#             turtle.home()

#######################################################

# tekent een hokje, blauw of rood aan de hand van de functie verwerk_schot (mis of raak)
def teken_hokje(x, y, vulkleur):
    turtle.fillcolor(vulkleur)
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(START_X + x * HOKJE, START_Y - y* HOKJE)
    turtle.pendown()
    for i in range(4):
        turtle.forward(HOKJE)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.home()








### HOOFDPROGRAMMA ###

#maak een leeg bord
bord, breedte, hoogte = maakBord()
speelBord, breedte, hoogte = maakBord()

#vul bord met willekeurige schepen
bord, schip1, schip2, schip3, schip4, schip5 = plaats_schepen(bord, breedte, hoogte)
alle_schepen = [schip1, schip2, schip3, schip4, schip5]
toonBord(bord, hoogte, breedte)
toonBord(speelBord, hoogte, breedte)    #toon bord zonder schepen op het scherm

#zolang spel niet is afgelopen, doe dan:
while spelAfgelopen == False:
    ingevulde_coordinaat, aantalPogingen = vraag_speler_om_coordinaten(aantalPogingen, hoogte, breedte)
    print("Aantal pogingen gedaan:", aantalPogingen)
    speelBord = verwerkSchot(bord, ingevulde_coordinaat, speelBord, alle_schepen)
    spelAfgelopen = controleer_einde_spel(alle_schepen)
    toonBord(speelBord, hoogte, breedte)


#spel afgelopen: geef gebruiker een compliment
if spelAfgelopen == True:
    print("Goed gespeeld!")
    print("Je hebt in ", aantalPogingen, "pogingen geraden waar alle schepen lagen")
    print("Dit was hoe de schepen waren geplaatst")
    toonBord(bord, hoogte, breedte)


turtle.done()