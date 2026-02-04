def presenteer(data_bron, totaal):
    for item, bedrag in data_bron.items():
        print(f"{item} : {bedrag} euro")
    print("==========================")
    print(f"Totaal : {totaal} euro")