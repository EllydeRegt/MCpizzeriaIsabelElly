# Po Zeeslag
# Elly de Regt

### GLOBALE VARIABELE ###

import random
import turtle

BREEDTE = 10
HOOGTE = 10
HOKJE = 30
BORD_GROOTTE = 300
START_X = -BORD_GROOTTE / 2
START_Y = BORD_GROOTTE / 2

SCHIP = " 0 "
WATER = " - "
MIS = " / "
RAAK_KLEUR = "red"
MIS_KLEUR = "blue"

spelAfgelopen = False

### FUNCTIEDEFINITIE ###

# legt uit hoe het spel werkt
def uitleg_spel():
    print("Je gaat het spel zeeslag spelen. Ik leg uit hoe het werkt")
    print("Je vijand heeft een vloot, je weet niet precies waar, maar wel welke schepen")
    print("Een schip van 2 hokjes lang, twee van 3 hokjes, een van 4 en een van 5 hokjes")
    print("Je wilt de vloot tot zinken brengen, door steeds een 'schot' te schieten")
    print("Voer steeds een coordinaat in, bestaande uit een letter en een cijfer")
    print("Totdat je alle delen van het schip hebt geraakt zinkt het niet")
    print("Probeer alle schepen in het veld tot zinken te brengen")
    print("Ik zal het laten weten als een schip is geraakt, en als een schip is gezonken")
    print("Wanneer je een schip hebt geraakt kleurt het hokje rood, en als je mis schiet, blauw")
    print("Probeer in zo min mogelijk pogingen de vloot tot zinken te brengen.")
    print("Veel succes!")

# maakt een leeg bord, wordt 2x aangehaald, 1 met schepen, 1 zonder schepen (het speelbord)
def maakBord():
    bord = []
    for y in range(HOOGTE):
        rij = []
        for x in range(BREEDTE):
            rij.append(WATER)                   #maakt een rij met juiste aantal kolommen
        bord.append(rij)
    return bord

# print het bord, nu niet per se meer nodig vanwege de turtle die later is toegevoegd
def toonBord(bord):
    teken_bord()
    for kolom in range(BREEDTE):
        print(" ", chr(65+kolom), end="")       #spatie en dan de letters boven het bord
    print()                                     #vanaf hier een enter en verder met het bord
    for x in range(HOOGTE):
        print(1 + x, end="")                    #de cijfers langs het bord(index 0 wordt cijfer 1)
        for y in range(BREEDTE):
            print(bord[x][y], end="")
        print()

# plaatst een schip met een gegeven lengte op een random plek op het bord
def plaatsSchip(bord, lengte_schip):
    richtingen = ["verticaal", "horizontaal"]
    schip_geplaatst = False
    while schip_geplaatst == False:
        richting = random.choice(richtingen)    # kiest een random richting
        if richting == "horizontaal":
            y = [random.randint(0,(HOOGTE - 1))]                      # kiest een random Y-coordinaat
            x = [random.randint(0,(BREEDTE - lengte_schip))]          # kiest een random X-coordinaat
            for i in range(lengte_schip - 1):   # -1 omdat er al 1 waarde in de lijst staat
                volgende_X = x[-1] + 1          # X[-1] refereert naar het laatste item in de lijst
                x.append(volgende_X)
            y = y * len(x)
        elif richting == "verticaal":
            y = [random.randint(0,(HOOGTE - lengte_schip))]
            x = [random.randint(0,(BREEDTE - 1))]
            for i in range(lengte_schip - 1):
                volgende_Y = y[-1] + 1
                y.append(volgende_Y)
            x = x * len(y)
        # lijsten met coordinaten gemaakt, nu controleren of vrij en schip plaatsen
        schepen_omheen = geenSchepenRond(bord, y, x)
        if schepen_omheen == False:
            for horizontaal in y:
                for verticaal in x:
                    bord[horizontaal][verticaal] = SCHIP
            schip_geplaatst = True
    return bord, y, x

# controleert of het schip geen ander schip zal raken, voordat het geplaatst wordt
def geenSchepenRond(bord, y, x):
    schepen_omheen = False
    for horizontaal in y:
        for i in range(-1, 2):          # i krijgt nu de waardes, -1, 0 en 1 (boven / midden / onder)
            dy = horizontaal + i
            for verticaal in x:
                for i in range(-1, 2):
                    dx = verticaal + i
                    if (0 <= dy and dy < HOOGTE) and (0 <= dx and dx < BREEDTE):    # zorgt ervoor dat er geen error komt als het schip langs de rand ligt
                        if bord[dy][dx] == SCHIP:
                            schepen_omheen = True
    return schepen_omheen

# plaatst schepen van verschillende lengtes op het bord
# is niet in een for-loop gezet zodat twee schepen van 3 geplaatst konden worden, zoals in het echte spel
# ook konden zo de coordinaten van alle schepen in een apparte lijst worden gezet
def plaats_schepen(bord):
    bord, y, x = plaatsSchip(bord, 2)
    schip1 = []
    for i in range(len(y)):
        coordinaat = [x[i], y[i]]
        schip1.append(coordinaat)
    bord, y, x = plaatsSchip(bord, 3)
    schip2 = []
    for i in range(len(y)):
        coordinaat = [x[i], y[i]]
        schip2.append(coordinaat)
    bord, y, x = plaatsSchip(bord, 3)
    schip3 = []
    for i in range(len(y)):
        coordinaat = [x[i], y[i]]
        schip3.append(coordinaat)
    bord, y, x = plaatsSchip(bord, 4)
    schip4 = []
    for i in range(len(y)):
        coordinaat = [x[i], y[i]]
        schip4.append(coordinaat)
    bord, y, x = plaatsSchip(bord, 5)
    schip5 = []
    for i in range(len(y)):
        coordinaat = [x[i], y[i]]
        schip5.append(coordinaat)
    return bord, schip1, schip2, schip3, schip4, schip5

# vraagt de speler om een coördinaat en returned deze in een lijst
def vraag_speler_om_coordinaten(aantalPogingen):
    goeieGok = False
    geldige_X = False
    geldige_Y = False
    while goeieGok == False:          # terwijl er nog geen geldige gok is gedaan blijft hij ernaar vragen
        while geldige_X == False:     # terwijl er nog geen geldige X-coordinaat is ingevuld blijft hij ernaar vragen
            invoerX = input("Voer een letter in (de X-coordinaat)").strip()     # .strip() haalt onnodige spaties voor en achter de invoer weg
            invoerX, geldige_X = controleer_X(invoerX)                          #roept functie aan die controleert of invoer letter is en hoofdletter maakt
        X_coordinaat = ord(invoerX) - 65
        while geldige_Y == False:     # terwijl er nog geen geldige Y-coordinaat is ingevuld blijft hij ernaar vragen
            invoerY = input("Voer een cijfer in (de Y-coordinaat)").strip()     # .strip() haalt onnodige spaties voor en achter de invoer weg
            invoerY, geldige_Y = controleer_Y(invoerY)                          #roept functie aan die controleert of cijfer is    
        Y_coordinaat = int(invoerY) - 1
        if ((Y_coordinaat + 1) > HOOGTE) or ((X_coordinaat +1 ) > BREEDTE):     # controleert of de coordinaten op het bord liggen
            print("Sorry, deze coordinaten liggen niet op het bord, probeer opnieuw")
            geldige_X = False
            geldige_Y = False
        else:
            print("Je hebt ingevoerd: (", invoerX, invoerY, ")")
            # controleert of de coordinaat al is ingevoerd
            if speelBord[Y_coordinaat][X_coordinaat] == WATER:
                aantalPogingen += 1
                goeieGok = True
            else:
                print("Deze coordinaat heb je al eens ingevoerd")
                geldige_X = False
                geldige_Y = False
    # zet de coordinaat in een lijst als [X_coordinaat, Y_coordinaat]
    ingevulde_coordinaat = []
    ingevulde_coordinaat.append(X_coordinaat)
    ingevulde_coordinaat.append(Y_coordinaat)
    return ingevulde_coordinaat, aantalPogingen

# controleert of de ingevoerde x-coördinaat één letter is en zet deze evt. om in een hoofdletter
def controleer_X(invoer):
    geldige_X = invoer.isalpha()       # .isalpha() is een boolean die controleert of het letters uit het alphabet zijn
    if geldige_X == False:             # als de gok geen letter is
        print('Dit is geen letter, voer een letter in')
    else:
        if len(invoer) > 1:            # controleert of de invoer 1 teken is     
            print("Dit is meer dan 1 letter, voer 1 letter in")
            geldige_X = False
        else:
            print('gok is een letter')
            invoer = invoer.upper()    # .upper() maakt van de invoer hoofdletters
            geldige_X = True
    return invoer, geldige_X

# controleert of de ingevoerde y-coördinaat een getal is
def controleer_Y(invoer):
    geldige_Y = invoer.isdigit()       # .isdigit() is een boolean die controleert of het hele, positieve getallen zijn
    if geldige_Y == False:
        print("Dit is geen geldig getal, voer een getal in")
    else:
        print('gok is een getal')
        geldige_Y = True
    return invoer, geldige_Y

# kijkt of schot raak/mis en of schip is gezonken
def verwerkSchot(bord, ingevulde_coordinaat, speelBord, alle_schepen):
    y = ingevulde_coordinaat[1]
    x = ingevulde_coordinaat[0]
    if bord[y][x] == SCHIP:
        print("Raak! Op deze coordinaat lag een schip!")
        teken_hokje(x, y, RAAK_KLEUR)
        speelBord[y][x] = SCHIP                    # toont op het speelBord wat er geraakt is
        for schip in alle_schepen:                 # controleert voor ieder schip of de coordinaat op dat schip ligt
            if [x, y] in schip:
                schip.remove([x, y])               # .remove() verwijdert de geraakte coordinaat uit de lijst van dat schip
                if schip == []:
                    print("Schip is gezonken")
    else: 
        print("Helaas!, dit was mis, probeer opnieuw!")
        teken_hokje(x, y, MIS_KLEUR)
        speelBord[y][x] = MIS
    return speelBord

#controleert of alle schepen zijn gezonken en het spel eindigt
def controleer_einde_spel(alle_schepen):
    potjeAfgelopen = True
    for schip in alle_schepen:
        if schip != []:         # als er een schip is dat nog niet is gezonken (en dus nog coordinaten heeft in de lijst)
            potjeAfgelopen = False
    return potjeAfgelopen

# tekent het bord met turtle
def teken_bord():  
    # tekent de horizontale lijnen 
    for rij in range(HOOGTE + 1):   # +1 omdat de lijnen de hokjes omlijnen, er is dus 1 lijn extra
        turtle.penup()
        turtle.goto(START_X, START_Y - rij * HOKJE)
        turtle.pendown()
        turtle.forward(BORD_GROOTTE)
    # Hij 'tekent' de letters naast het bord
    for rij in range(HOOGTE):       # hier geen +1 omdat er evenveel letters als rijen zijn
        turtle.penup()
        turtle.goto(START_X - 20, START_Y - rij * HOKJE - 20)    # - 20 zorgt ervoor dat de letters netjes naast het bijbehorende hokje en niet op het bord komen
        turtle.pendown()                         
        turtle.write(str((rij + 1)), align="center", font=("Arial", 12, "normal"))    # str() is nodig omdat je met "" de variabele: rij niet kan gebruiken
    
    # vanaf hier de verticale lijnen
    turtle.right(90)
    for kolom in range(BREEDTE + 1):    # voor de +1 bij breedte geldt hetzelfde als voor de hoogte
        turtle.penup()
        turtle.goto(START_X + kolom * HOKJE, START_Y)
        turtle.pendown()
        turtle.forward(BORD_GROOTTE)
    # hij 'tekent' de cijfers boven het bord
    for kolom in range(BREEDTE):
        turtle.penup()
        turtle.goto(START_X + kolom * HOKJE  + 20, START_Y + 20)  # + 20 zorgt ervoor dat de cijfers netjes boven het bijbehorende hokje en niet op het bord komen
        turtle.pendown() 
        turtle.write(chr(65 + kolom), align="right", font=("Arial", 12, "normal"))    #.write(...) laat turtle typen                                      
    turtle.penup()
    turtle.home()   # .home() zorgt ervoor dat de turtle terug naar zijn beginpositie gaat, waardoor deze geen verkeerde lijnen gaat tekenen

# tekent een hokje, blauw of rood aan de hand van de functie verwerk_schot (mis of raak)
def teken_hokje(x, y, vulkleur):
    turtle.fillcolor(vulkleur)
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(START_X + x * HOKJE, START_Y - y * HOKJE)
    turtle.pendown()
    for i in range(4):
        turtle.forward(HOKJE)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.home()   # .home() zorgt ervoor dat de turtle terug naar zijn beginpositie gaat, waardoor deze geen verkeerde lijnen gaat tekenen

# slaat de score op in een bestand
def opslaan_score(aantalPogingen):
    score = str(aantalPogingen)
    bestand = open("scores.txt", "a") #a omdat je achteraan bestand wil toevoegen
    bestand.write("\n")
    bestand.write(score)
    bestand.close()
    print("klaar")

# toont een overzicht met de behaalde scores en de highscore
def laten_zien_scores():
    scores = []
    bestand = open("scores.txt", "r")
    inhoud_als_lijst = bestand.readlines() # zet elk regel in een lijst

    # print netjes de scores en zet deze in een nette lijst (zonder \n)
    print("scores:")
    for regel in inhoud_als_lijst:
      regel = regel.strip()     # .strip() haalt ook de \n weg, waardoor de scores gelijk onder elkaar worden geprint
      print(regel)
      scores.append(regel)
    highscore = min(scores)
    print("Hoe minder pogingen, hoe beter. De laagst mogelijke score is 17")
    print("Je highscore is:", highscore)
    bestand.close()
    
def geef_feedback_einde_spel(aantalPogingen):
    print("Goed gespeeld!")
    print("Je hebt in ", aantalPogingen, "pogingen geraden waar alle schepen lagen")
    if aantalPogingen == "17":
        print("Hoera! Je hebt de topscore behaalt")
    else:
        print("Met", (aantalPogingen - 17), "pogingen minder zou de topscore zijn bereikt")
    opslaan_score(aantalPogingen)
    laten_zien_scores()


### HOOFDPROGRAMMA ###

uitleg_spel()

while spelAfgelopen == False:
    # deze staan in de while, zodat ze ook bij een nieuw potje gelden
    turtle.hideturtle()
    turtle.pencolor("blue")     
    turtle.speed(0)             # Zet de snelheid op maximaal om snel te tekenen

    potjeAfgelopen = False
    aantalPogingen = 0

    #maak een leeg bord
    bord = maakBord()
    speelBord = maakBord()     # dit wordt het bord dat de speler ziet

    #vul bord met willekeurige schepen
    bord, schip1, schip2, schip3, schip4, schip5 = plaats_schepen(bord)
    alle_schepen = [schip1, schip2, schip3, schip4, schip5]
    laten_zien_scores()
    toonBord(bord)
    toonBord(speelBord)    #toont bord zonder schepen op het scherm

    #zolang het potje niet is afgelopen, doe dan:
    while potjeAfgelopen == False:
        ingevulde_coordinaat, aantalPogingen = vraag_speler_om_coordinaten(aantalPogingen)
        print("Aantal pogingen gedaan:", aantalPogingen)
        speelBord = verwerkSchot(bord, ingevulde_coordinaat, speelBord, alle_schepen)
        potjeAfgelopen = controleer_einde_spel(alle_schepen)
        toonBord(speelBord)

    #spel afgelopen: geef gebruiker een compliment
    if potjeAfgelopen == True:
        geef_feedback_einde_spel(aantalPogingen)
        # als de gebruiker nog een potje wilt doen
        invoer = input("Type 1 als je een revanche wilt, en 2 als je wilt stoppen met spelen.")
        if invoer == "1":
            potjeAfgelopen = False
            turtle.reset()      # .reset() verwijdert alle tekeningen en brengt de turtle terug naar de beginpositie, zodat een leeg raster getekent kan worden
        else:
            print("Bedankt voor het spelen!")
            spelAfgelopen = True
turtle.done()
