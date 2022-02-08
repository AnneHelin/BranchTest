# X-funktio tarkistaa onko kulma suora
# Lisää funktioon virheen laskenta millimetreinä 

def suorakulma(sivuA, sivuB, lavistaja):
    """Tarkista surorakulmaisuuden käyttäen Phytagoran lausetta
    Args:
        sivuA (float): Ensimmäisen sivun pituus
        sivuB (float): Toisen sivun pituus
        lavistaja (float): Lävistäjän pituus
     Returns:
        float: Lävistäjän pituusvirhe 0 -> ei virhettä  
    """

    try:
        A_nelio = sivuA * sivuA
        B_nelio = sivuB * sivuB
        l_nelio = lavistaja * lavistaja
    # TODO jos antaa vahingossa kirjaimen arvoksi -> kaatuu
        pitaisi_olla = A_nelio + B_nelio
        ero = l_nelio**0,5 - pitaisi_olla**0.5
        
    except:
        ero = 999
        print('Syötetty arvo on virheellinen')
    finally:    
        return ero

# Testataan, että toimii 
if __name__ == "__main__":
    # Testi kulma on suora
    vastaus = suorakulma(3, 4, 5)
    print(vastaus)    

    # Testi kulma ei ole suora
    vastaus = suorakulma(3, 4, 6)
    print(vastaus)

