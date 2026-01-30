from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)   
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} voor {prijs_na_korting} euro."
    return uitvoer

def inkomsten_totaal(inkomsten):
    totaal = sum(inkomsten)
    btw = float(0.09)
    bedrag = totaal * btw
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden." 
    return uitvoer

def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return [laagste, hoogste]

def gemiddelde(mijn_lijst):
    bedrag = sum(mijn_lijst)/len(mijn_lijst)
    uitvoer = f"De gemiddelde inkomsten deze week zijn {bedrag} euro."
    return uitvoer

def meervoudig(mijn_lijst):
    invoer_lijst = laag_en_hoog(mijn_lijst) 
    uitvoer = invoer_lijst
    return uitvoer 

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

inkomsten = [220, 430, 125, 160, 205, 90, 345]
mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
invoer_lijst_2 = [10, 5, 3, 2, 1, 2, 9]

print(aanbieding_1("aardbei", 4, 0.1))
print(inkomsten_totaal(inkomsten))
print(laag_en_hoog(mijn_lijst))
print(gemiddelde(mijn_lijst))
print(meervoudig(invoer_lijst))
print(combinatie(invoer_lijst_2))