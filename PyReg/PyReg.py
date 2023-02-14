import os
# Toon het hoofdmenu
print ("========== PyReg ===========")
print ("Welkom bij PyReg, het Python KassaSysteem voor en door DeveloperLand!")
print ("Tel de kassa, en geef op hoeveel er nu in zit.")
# Start programma, stel de nodige variabelen in
bedragInKassaBegin = float(input("Bedrag in kassa? "))
keuze = 0
dagTotaal = 0
aantalBonnen = 0
dagTotaalTerug = 0
# Laat de gebruiker een keuze maken
while(not keuze == "9" ):# Herhaal tot de gebruiker aangeeft dat het programma afgesloten moet worden
    os.system('cls')
    print ("======== HOOFDMENU =========")
    print ("1. Nieuwe bon")
    print ("2. Retour")
    print ("3. Toon kassatotaal")
    print ("9. Afsluiten")
    print ("============================")

    keuze = input("Maak uw keuze en druk op <ENTER>.")# Laat de gebruiker een keuze maken

    if (keuze == "1"):
        bestelKeuze = 0
        bonTotaal = 0
        bonString = ""
        while(not bestelKeuze == "9"):
            print ("========= BON MENU =========")
            print ("Bon "+ str(aantalBonnen))
            print( "1. Volwassene                     € 19,-")
            print( "2. Kinderen tot 12jr              € 9,-")
            print( "3. Familiepas (2x volw. 3x kind)  € 49")
            print( "4. DeveloperLand-kaart            € 4,50")# Voeg eenDeveloperland-kaarttoe aan de bon
            print( "5. Kinderwagen/bolderkar (1 dag)  € 6")
            print( "6. Parkeerdagkaart                € 9")
            print( "9. Afronden bon")
            print( "Z. Bon annuleren")
            print ("============================")
            bestelKeuze = input("Maak uw keuze en druk op <ENTER>.")
# Voeg één volwasseneticket toe aan de bon
            if ( bestelKeuze == "1"):
                bonTotaal = bonTotaal + 19
                bonString = bonString + "1x Volwassene                  € 19\r\n"
            elif ( bestelKeuze == "2"):
                bonTotaal = bonTotaal + 9
                bonString = bonString + "1x kind (tot 12jr)             € 9\r\n"# Voeg één kinderkaartje toe aan de bon
            elif ( bestelKeuze == "3"):
                bonTotaal = bonTotaal + 49
                bonString = bonString + "1x Familiepas                  € 49\r\n"# Voeg een familiepas toe aan de bon
            elif ( bestelKeuze == "4"):
                bonTotaal = bonTotaal + 4.50
                bonString = bonString + "1x Parkkaart                   € 4,50\r\n"
                # Voek een kinderwagen/bolderkar toe aan de bon
            elif ( bestelKeuze == "5"):
                bonTotaal = bonTotaal + 6
                bonString = bonString + "1x kinderwagen/bolderkarhuur   € 6\r\n"
            elif ( bestelKeuze == "6"):
                bonTotaal = bonTotaal + 9
                bonString = bonString + "1x Parkeerdagkaart             € 9\r\n"
                # Voeg een parkeerkaart toe aan de bon
            elif(bestelKeuze == "9"):
                aantalBonnen = aantalBonnen +1
                dagTotaal = dagTotaal + bonTotaal
                print( bonString )
                print ("======== BON TOTAAL ========")
                print( "Te betalen: " + str(bonTotaal) )
                betaald = float(input("Betaald:    "))# Gebruiker wil de bon annuleren; reset bon variabelenen keer terug naar het hoofdmenu
                terug = bonTotaal - betaald
                print ( "Terug:     " + str(terug))# Gebruiker wil een nieuwe bon maken, stel variabelen voor bon in en toon menu
                input("Druk op <ENTER> om door te gaan.")
            elif (bestelKeuze == "Z" or bestelKeuze == "z"):
                bestelKeuze = 9
                bonTotaal = 0
                bonString = ""
    elif(keuze == "2"):# Gebruiker wil bedrag retourneren
        print ("Uitvoeren terugbetaling")
        terugTeGeven = float(input( "Bedrag originele bon: "))
        reden = input("Reden retour: ")
        dagTotaalTerug = terugTeGeven
        # Verwerk retourbedrag in dagtotaal
    elif(keuze == "3"):
        # Kassa is correct afgesloten, toon dagtotalen
        print ("======= DAG TOTALEN ========")
        print ("In kassa begin:   " + str(bedragInKassaBegin))
        print ("Verkocht:         " + str(dagTotaal))# Gebruiker wil de dagtotalen zien
        print ("Retour:           " + str(dagTotaalTerug))# Toon retourbedrag
        print ("In kassa:         " + str( bedragInKassaBegin + dagTotaal - dagTotaalTerug ))
        input("Druk op <ENTER> om door te gaan.")
inKassa = float(input("Hoeveel zit er nu in de kassa?")) 
while(not inKassa == (bedragInKassaBegin + dagTotaal - dagTotaalTerug )):
    print("Je hebt een kassaverschil! Tel de kassa opnieuw")# Herhaal zolang het opgegeven bedrag in kassa niet overeenkomt met het berekende bedrag in kassa
    inKassa = float(input("Hoeveel zit er nu in de kassa?")) # Vraag om bedrag en reden
# Gebruiker wil het programma afsluiten, vraag om bedrag in kassa
os.system('cls')
# Toon bon-menu
print("Kassa klopt, programma wordt afgesloten.")
print ("======== DAGTOTALEN ========")
print ("Aantal bonnen: " + str(aantalBonnen))
print ("Verkocht:      " + str(dagTotaal))
print ("Totaal retour: " + str(dagTotaalTerug))
print ("In kassa:      " + str(inKassa))
print ("============================")
# Bon is klaar, toon totaal en reken af