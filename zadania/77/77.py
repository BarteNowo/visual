def szyfr_vigenerea(tekst, klucz):
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
            zakodowany += litera
            continue
    
    return zakodowany

def deszyfr_vigenerea(zakodowany_tekst, klucz):
    zakodowany_tekst = zakodowany_tekst.upper()
    klucz = klucz.upper()
    odszyfrowany = ""
    klucz_index = 0
    
    for litera in zakodowany_tekst:
        if litera.isalpha():
            przesuniecie = ord(klucz[klucz_index % len(klucz)]) - ord('A')
            litera_odszyfrowana = chr((ord(litera) - ord('A') - przesuniecie) % 26 + ord('A'))
            odszyfrowany += litera_odszyfrowana
            klucz_index += 1
        else:
            odszyfrowany += litera
            continue
    
    return odszyfrowany

tekst = "TO WAZNE BYSMY WIEDZIELI SKAD PRZYCHODZIMY, PONIEWAZ JESLI NIE WIEMY SKAD PRZYCHODZIMY, TO NIE WIEMY GDZIE JESTESMY. A JESLI NIE WIEMY GDZIE JESTESMY, TO NIE WIEMY DOKAD ZMIERZAMY. A JESLI KTOS NIE WIE DOKAD ZMIERZA, TO PRAWDOPODOBNIE ZMIERZA W ZLYM KIERUNKU. TERRY PRATCHETT."
klucz = "LUBIMYCZYTAC"
print(szyfr_vigenerea(tekst, klucz))
print(deszyfr_vigenerea("V CNHBHCFKRTGMBT DUYMWINNSU HHP WVSVMNLD, JWXXYWH VATXOMIWHHP DUYMWINNSUC. LCIJMQNLKD OUTZXW, D REMJV JTGLX KCEZKDHEHE FCD TGWMQEU MHEVS YLABJIPRUBIW JNHWHJQ. NNFXNQG VWOVBQAHO RTSHDX IPXAPD LDSL TZDYRBHIWKD. JWXXYMP VTEBEHWQG REOQDU WNTBA BYRE FDCWWL. PHETI JECUD EMMBHCAY MTS EXTS SGRZUTD YWJCG TABDZ OUR ZUOZLEWG. LOEYME OERWPDVMEB JDCTHJKNR LDSL NDCOC. BQIBBBIW MHP BLL. BIATX PJUSNVHSB.", "ZLODZIEJCZASU"))