# PÄÄOHJELMA

# KIRJASTOJEN JA MODULIEN LATAUS

# Otetaan käyttöön Windows-äänikirjasto (pythonin sisälle rakennettu)
import winsound

# Otetaan käyttöön oma funktiomoduuli
import funktiot_moduli

def select_case(sanakirja, avain, oletus):
    """Muiden ohjelmointikielten Select-Case-rakennetta vastaava funktio

    Args:
        sanakirja(dict): Avain-arvo-parit
        avain (any): hakuavain
        oletus (any): arvo, jos hakuavainta ei löydy

    Returns:
        any: Hakuavainta vastaava arvo tai oletus, mikäli hakuavainta ei löytynyt
    """
    arvo = sanakirja.get(avain, oletus)    
    return arvo

    # Varsinainen pääohjelma alkaa tästä
    huoneraja_arvot = {'MH': 30, 'K' : 20, 'KPH' : 5, 'WC': 5, 'OH': 20}

    

    """
    return arvo    
# Varsinainen pääohjelma alkaa tästä
mittaustulokset = []

# Ikuinen silmukka
while True:
    # Tätä toistetaan, kunnes käyttäjä sulkee ohjelman
    
    seina1 = float(input('Anna ensimmäisen seinän pituus:' ))
    seina2 = float(input('Anna toisen seinän pituus:' ))
    lavistaja = float(input('Anna ristimitta:' ))

    mittaustulokset.append(seina1)
    mittaustulokset.append(seina2)
    mittaustulokset.append(lavistaja)

    # Kerrotaan onko tila suorakulmainen
    print('Nurkka suorakulmainen', funktiot_moduli.suorakulma(
        seina1, seina2, lavistaja))

    # Kysytään käyttäjältä haluaako jatkaa
    lopetetaan = input('Paina L, jos haluat lopettaa: ').upper()
    
    if lopetetaan == 'L':
        break

# Ohjelman suoritus päättyy
 
# Kysytään mittaajan ja työmaan tiedot
Tyomaa = input('Minkä tyyppinen työmaa oli (kerrostalo, rivitalo tai OK-talo): ')

# Ilmoitetaan montako senttiä mittauksessa saa olla virhettä IF-rakenteen avulla

if Tyomaa == 'kerrostalo':
    print('Maksimivirhe saa olla 10 mm')
elif Tyomaa == 'rivitalo':
    print('Maksimivirhe saa olla 20 mm')
else:
    print('Maksimivirhe saa olla 50 mm')        

mittauksia = len(mittaustulokset)
print('Kiitos tästä päivästä, teit', mittauksia, 'mittaus')    


# Tulostetaan ruudulle kaikki mittaustulokset
print('Päivän mittaukset alla:')
for mitaus in mittaustulokset:
    print(mitaus)

