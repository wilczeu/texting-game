# -*- coding: latin-1 -*-
import subprocess


kierunek1 = input("W ktora strone sie wybierasz?: ")

#kierunek - lewo w parku do gruz�W:

if kierunek1 == 'l':
    print("""
    Lewa strona wydawa� ci si� bardziej kuszaca. Ruszasz wiec wlasnie tam.
    Z kazdym kolejnym krokiem, mgla wydaje sie byc coraz to gestsza, bardziej duszaca oraz coraz bardziej szara, momentami wrecz czarna.
    Wiekowe drzewa przypominaja dziwaczne, przerazajace postacie z horrorow.
    Rozgladasz sie. W oddali widzisz pomara�czowe, delikatnie blyskajace swiatlo. Postanawiasz isc w tamtym kierunku.
    Ogie�? Bardzo mozliwe.
    Przy�pieszasz kroku o tyle, o ile jest w stanie twoj odwodniony organizm.
    
    W ko�cu mijasz ostatnie sprochniale drzewo i wchodzisz na jakies gruzy. Niedaleko, naprzeciwko ciebie, jest ogromny plomien. Bardzo wyraznie czujesz na skorze jego cieplo.
    
    'Pomocy!!!', slyszysz nagle delikatny glos. Ciezko stwierdzic czy nalezal do mlodego chlopca, czy dziewczyny.
    'Pomocy..!', dociera do ciebie drugi glos, z przeciwnej strony niz poprzedni. Ten z kolei jest typowo meski.
 
    Co robisz?
    1. Ratujesz wlasciciela pierwszego glosu
    2. Ratujesz wlasciciela drugiego glosu
    3. Uciekasz tam, skad przyszedles.""")
    # -*- coding: latin-1 -*-
    subprocess.call("kierunek2-gruzy.py", shell=True, encoding='latin-1')
    


if kierunek1 == 'p':
     print("""
        Prawa strona wydawala ci sie jednak bardziej pociagajaca opcja. Ruszasz wiec wlasnie tam.
        Twoj organizm staje sie coraz s�abszy. Kiedy ostatnio jadles? Kiedy ostatnio piles?
        Mgla przyjemnie cie otula, jak pierzyna. Oczy ci sie powoli zamykaja. 
        Jednak gdy juz myslales, ze zasniesz na stojaco, widzisz jakis niewielki drewniany dom.
        Szybko sie rozbudzasz i delikatnie przyspieszasz kroku.
        Gdy podchodzisz, widzisz ze ciemne drzwi ledwo trzymaja sie na zawiasach, a w jednym z dwoch przednich okien brakuje szyby.
        Znow zagrzmialo, deszcz sie nasilil.
    
        Co robisz?
        1. Najpierw ogladasz dom dookola, by zobaczyc czy jest ktos w poblizu.
        2. Wchodzisz.""")
        # -*- coding: latin-1 -*-
     subprocess.call("chata-sam.py", shell=True, encoding='latin-1')
        
        