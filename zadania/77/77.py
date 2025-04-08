def vigenere_encrypt(tekst, klucz):
    tekst = tekst.upper()
    klucz = klucz.upper()
    zakodowany = ""
    klucz_index = 0
    
    for litera in tekst:
        if litera.isalpha():
            przesuniecie = ord(klucz[klucz_index % len(klucz)]) - ord('A')
            litera_zakodowana = chr((ord(litera) - ord('A') + przesuniecie) % 26 + ord('A'))
            zakodowany += litera_zakodowana
            klucz_index += 1
        else:
            continue
    
    return zakodowany

tekst = "TO WAZNE BYSMY WIEDZIELI SKAD PRZYCHODZIMY, PONIEWAZ JESLI NIE WIEMY SKAD PRZYCHODZIMY, TO NIE WIEMY GDZIE JESTESMY. A JESLI NIE WIEMY GDZIE JESTESMY, TO NIE WIEMY DOKAD ZMIERZAMY. A JESLI KTOS NIE WIE DOKAD ZMIERZA, TO PRAWDOPODOBNIE ZMIERZA W ZLYM KIERUNKU. TERRY PRATCHETT."
klucz = "LUBIMYCZYTAC"
print(vigenere_encrypt(tekst, klucz))