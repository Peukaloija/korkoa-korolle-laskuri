def korkoa_korolle_laskuri():

    """ Skripti, mikä laskee rahaston korkoa korolle tuoton sekä sen lisäksi oleellisia tunnuslukuja kuten kulut ja säästöt ilman korkoa korolle efektiä  """
        
    #Luodaan tarvittavat boolean arvot poikkeuksien ja väärien käyttäjän antamien arvojen hallintaan
    alkupaaoma = None
    kuukausisaasto = None
    tuotto_kuluton = None
    kulut = None
    vuodet = None 
    
    #Kysytään käyttäjältä arvoja ja varmistetaan, että skripti vastaa asianmukaisesti poikkeuksiin ja vääriin arvoihin
    
    #Alkupääoma
    while alkupaaoma == None:
        try:
            alkupaaoma = float(input('Mikä on aloituspääoma?: '))
            #Mikäli käyttäjä syöttää virheellisen arvon esim. alle 0 tai kirjaimia
            if alkupaaoma < 0 or not isinstance(alkupaaoma, float):
                print('Kelvoton alkupääoma, yritä uudelleen')
                #Annetaan esimerkki kelvollisesta arvosta
                print('Esimerkki kelvollisesta alkupääomasta: 2000')
                alkupaaoma = None
            else:
                break
        except ValueError as e:
            print(f'{e} on kelvoton alkupääoma, yritä uudestaan')
            print('Esimerkki kelvollisesta alkupääomasta: 2000')
            alkupaaoma = None
        
                
    #Toistetaan poikkeukset jokaisten arvojen kohdalla
    #Kuukausisäästö
    while kuukausisaasto == None:
        try:
            kuukausisaasto = float(input('Mikä on kuukausittainen säästö?: '))
            if kuukausisaasto < 0 or not isinstance(kuukausisaasto, float):
                print('Kelvoton kuukausisäästösumma, yritä uudelleen')
                print('Esimerkki kelvollisesta kuukausisäästösummasta: 200')
                kuukausisaasto = None
            else:
                break
        except ValueError as d:
            print(f'{d} on kelvoton kuukausisäästösumma, yritä uudestaan')
            print('Esimerkki kelvollisesta kuukausisäästösummasta: 200')
            kuukausisaasto = None
            
    #Tuotto-odotus
    while tuotto_kuluton == None:
        try:
            tuotto_kuluton = float(input('Mikä on vuotuinen tuotto-odotus? (%): '))
            if tuotto_kuluton <= 0 or not isinstance(tuotto_kuluton, float):
                print('Kelvoton tuotto-odotus, yritä uudelleen')
                print('Esimerkki kelvollisesta tuotto-odotuksesta: 8')
                tuotto_kuluton = None
            else:
                break
        except ValueError as w:
            print(f"{w} on kelvoton tuotto-odotus")
            print('Esimerkki kelvollisesta tuotto-odotuksesta: 8')
            tuotto_kuluton = None
    
                
    #Hallinnointikulut
    while kulut == None:
        try:
            kulut = float(input('Mitkä ovat rahaston vuotuiset hallinnointikulut?: '))
            if kulut < 0 or not isinstance(kulut, float):
                print('Kelvoton hallinnointikulu, yritä uudelleen')
                print('Esimerkki kelvollisesta hallinnointikulusta: 0.20')
                kulut = None
            else:
                break
        except ValueError as k:
            print(f"{k} on kelvoton vuotuinen hallinnointikulu, yritä uudelleen")
            print('Esimerkki kelvollisesta hallinnointikulusta: 0.20')
            kulut = None
    
    
    #Vuodet
    while vuodet == None:
        try:
            vuodet = int(input('Kuinka monta vuotta sijoitat?: '))
            if vuodet <= 0 or not isinstance(vuodet, int):
                print('Kelvoton vuosimäärä, yritä uudelleen')
                print('Esimerkki kelvollisesta vuosimäärästä: 20')
                vuodet = None
            else:
                break
        except ValueError as u:
            print(f"{u} on kelvoton vuosimäärä, yritä uudelleen")
            print('Esimerkki kelvollisesta vuosimäärästä: 20')
            vuodet = None
    
    
    
    #Alustetaan muuttujia silmukkaa varten
    tuotto_kuluilla = tuotto_kuluton - kulut
    potti_kuluton = 0 + alkupaaoma
    potti_kuluilla = 0 + alkupaaoma
    kuukausisaastot = 0

    #Luodaan arvoista kuukausittaisia, jotta voidaan ottaa huomioon myös kuukausittainen säästäminen
    kk_tuotto_kuluton = (1 + tuotto_kuluton / 100) ** (1/12)
    kk_tuotto_kuluilla = (1 + tuotto_kuluilla / 100) ** (1/12)
    kuukaudet = vuodet * 12

    #Luodaan silmukka, jonka avulla lasketaan tuotto ilman kuluja ja niiden kanssa
    for kuukausi in range(0, kuukaudet):
            
        #Potti kuluilla
        potti_kuluilla += kuukausisaasto
        potti_kuluilla *= kk_tuotto_kuluilla

        #Potti kuluton
        potti_kuluton += kuukausisaasto
        potti_kuluton *= kk_tuotto_kuluton

        #Ilman korkoa korolle säästöt
        kuukausisaastot += kuukausisaasto

    print(f"\nLopullinen summa {vuodet} vuoden jälkeen: {round(potti_kuluilla)} euroa")
    print(f"\nLisätietoja:")
    print(f"Lopullinen summa jos ei olisi kuluja: {round(potti_kuluton)} euroa")
    print(f"Kulut söivät tuotosta: {round(potti_kuluton)-round(potti_kuluilla)} euroa")
    print(f"Säästöt ilman korkoa korolle efektiä: {round(kuukausisaastot)} euroa")


korkoa_korolle_laskuri()

