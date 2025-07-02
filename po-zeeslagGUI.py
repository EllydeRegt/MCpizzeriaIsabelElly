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

SCHIP = " 0 "
WATER = " - "
MIS = " / "

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
    teken_schip(X, Y)
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
        speelBord[Y][X] = SCHIP                    # toont op het speelBord wat er geraakt is
        print("alle_schepen", alle_schepen)
        for schip in alle_schepen:                 # controleert voor ieder schip of de coordinaat op dat schip ligt
            if [Y, X] in schip:
                schip.remove([Y, X])               # .remove() verwijdert de geraakte coordinaat uit de lijst van dat schip
                if schip == []:
                    print("Schip is gezonken")
        print("alle_schepen", alle_schepen)
    else: 
        print("Helaas!, dit was mis, probeer opnieuw!")
        speelBord[Y][X] = MIS
    return speelBord

def controleer_einde_spel(alle_schepen):
    spelAfgelopen = True
    for schip in alle_schepen:
        if schip != []:         # als er een schip is dat nog niet is gezonken (en dus nog coordinaten heeft in de lijst)
            spelAfgelopen = False
    return spelAfgelopen


def teken_bord(hoogte, breedte):   
    start_x = -BORD_GROOTTE / 2 
    start_y = -BORD_GROOTTE / 2
    for rij in range(hoogte + 1):
        turtle.penup()
        turtle.goto(start_x, start_y + rij * HOKJE)
        turtle.pendown()
        turtle.forward(BORD_GROOTTE)
    
    # vanaf hier de verticale lijnen
    turtle.left(90)
    for kolom in range(breedte + 1):
        turtle.penup()
        turtle.goto(start_x + kolom * HOKJE, start_y)
        turtle.pendown()
        turtle.forward(BORD_GROOTTE)
    

def teken_schip(X, Y):
    start_x = -BORD_GROOTTE / 2
    start_y = -BORD_GROOTTE / 2
    turtle.fillcolor("red")
    turtle.begin_fill()
    for x in X:
        for y in Y:
            turtle.penup()
            turtle.goto(start_x + x * HOKJE, start_y + y * HOKJE)
            turtle.pendown()
            turtle.forward(HOKJE)
            turtle.right(90)
            turtle.forward(HOKJE)
            turtle.right(90)
            turtle.forward(HOKJE)
            turtle.right(90)
            turtle.forward(HOKJE)
            turtle.right(90)
    turtle.end_fill()



def draw_ship(x, y, length, horiz=True):
    turtle.penup()
    turtle.goto(x*BORD_GROOTTE, y*BORD_GROOTTE)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        if horiz: turtle.forward(length*BORD_GROOTTE)
        else: turtle.forward(BORD_GROOTTE)
        turtle.right(90)
        if horiz: turtle.forward(BORD_GROOTTE)
        else: turtle.forward(length*BORD_GROOTTE)
        turtle.right(90)
    turtle.end_fill()














### HOOFDPROGRAMMA ###

#maak een leeg bord
bord, breedte, hoogte = maakBord()
speelBord, breedte, hoogte = maakBord()


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