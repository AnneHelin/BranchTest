# X-funktio tarkistaa onko kulma suora
 


def suorakulma(sivuA, sivuB, lavistaja):
    """Tarkista surorakulmaisuuden käyttäen Phytagoran lausetta

    Args:
        sivuA (float): Ensimmäisen sivun pituus
        sivuB (float): Toisen sivun pituus
        lavistaja (float): Lävistäjän pituus

    Returns:
        boolean: TRUE -> suorakulma     
    
    """
    A_nelio = sivuA * sivuA
    B_nelio = sivuB * sivuB
    l_nelio = lavistaja * lavistaja
    # TODO 
    if A_nelio + B_nelio == l_nelio:
        suora = True
    else:     
        suora = False
    return suora

# Testataan, että toimii 
if __name__ == "__main__":
    # Testi kulma on suora
    vastaus = suorakulma(3, 4, 5)
    print(vastaus)    

    # Testi kulma ei ole suora
    vastaus = suorakulma(3, 4, 6)
    print(vastaus)

