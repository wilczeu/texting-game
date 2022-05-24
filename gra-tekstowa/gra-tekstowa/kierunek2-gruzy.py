# -*- coding: latin-1 -*-

from os import name
import subprocess


kierunek2 = input("""
Wybierz jedna z opcji wpisujac 1, 2 lub 3:  """)

#kierunek2 - do kobiety:
if kierunek2=='1':
    print("""'Mezczyzna pewnie sobie poradzi', powiedziales cicho i ruszyles za glosem kobiety. 
    Na szczêscie szybko udalo ci sie ja znalezc. Niby szybko, ale jednak za pozno, by jej jakkolwiek pomoc.
    By³a przysypana gruzem, nogi przygniotl jej jakis filar. Sam juz nic nie mogles zdzialac.

    'Spokojnie', usmiechnela sie blado. 'Dziekuje ci, ze nie umieram sama...'.

    'Ja... Ja moge cos zrobic!'

    'Nie. Juz nic nie mozesz zrobic, ale...' zakaszlala. 'Za parkiem jest mala chatka, powinno byc tam bezpiecznie. Schowaj sie tam, zgromadz zapasy i wychodz jak najmniej'.

    'Ale...!'

    Kobieta zaczela sie krztusic krwia i machnela reka, zebys juz uciekal. Przez chwile chciales szukac mezczyzny, ale jego glos juz dawno ucichl. Pewnie byl w podobnym stanie co kobieta, a trup w niczym ci nie pomoze.
    Na miêkkich nogach idziesz wiec szukac chatki. Nie bylo to trudne.""")
    subprocess.call("chata-sam.py", shell=True, encoding='latin-1')

#kierunek2 - do mezczyzny:
if kierunek2=='2':
    print("""Gdy juz chciales isc do kobiety, uslyszales z tamtej strony huk, a jej glos gwaltownie sie urwal.
    Postanowiles ratowac mezczyzne, bylo go ciagle slychac. Wiecej moze ci pomoc niz trup.
    Mezczyzna wlasnie sie podnosil. Wygladal jakby byl swiezo po trzydziestce. Ubrania mial zakrwawione, porwane. Jego lewa noga byla nienaturalnie zgieta. Jego bark tez jakos dziwnie ustawiony.

    'Zlamane pewnie' steknal widzac, ze mu sie przygladasz. 'Cho no tutaj, pomozesz mi dojsc do chaty'.

    'Na pewno jest pan w stanie chodzic?'

    'Jesli mi pomozesz wstac, to owszem'.
    Kiwnales glowa. Podszedles do niego i wziales go pod zdrowe ramie. Caly sie trzesles z wysilku podczas drogi. 

    'Wiesz co tu sie stalo?', zapytal gdy juz byliscie w parku.

    'Nie. Opowie mi pan o tym?'.

    'Chetnie bym opowiedzial. Problem w tym... ze sam niewiele pamietam. Wiem tylko, ze bombardowania tego miasta trwaja bardzo dlugo i juz nie jednego trupa musialem grzebac'.
    Czyli nici ze szczegolow - pomyslales rozczarowany.

    'I prosze, zadne 'prosze pana'. Mow mi Eugeniusz' - usmiechnal sie przyjaznie.
    W jego usmiechu bylo jednak cos bardzo niepokojacego. W jego oczach tak samo. Postanowiles trzymac sie na dystans i nie ufac temu mezczyznie zbyt szybko.""")
    print("""'A jak ty masz na imie?', zapytal gdy juz staneliscie pod chata. Zanim jednak zdazyles odpowiedziec, stwierdzil:
    'Wygladasz jak taki jeden """ + name + "'. ")
    print("""
    'Tak. Chyba tak mam na imie. Niestety nie mam pewnosci'

    Nastala chwilowa cisza w momencie wejscia do chaty. Wszystko bylo tu stare, drewniale. Bylo czuc pruchnica, co oznaczalo, ze ten budynek nie wytrzyma zbyt dlugo.

    'Nie szkodzi. Duzo osob stracilo pamiec lub tez rozum w ostatnim czasie. Nie znam niestety przyczyny'. 

    Pozniej cos szeptal pod nosem na tyle szybko, ze ciezko bylo cokolwiek zrozumiec. Usiedliscie w pomieszczeniu, ktore chyba bylo kiedys kuchnia.
    
    """
    subprocess.call("chata-z_m1.py", shell=True, encoding='latin-1'))


#powrot do parku
if kierunek2 == '3':
    print("""
    Udajac, ze nic tu nie widziales ani nie slyszales - wracasz do parku.
    Co teraz zamierzasz zrobic?
    1. Wracasz na gruzy
    2. Idziesz w przeciwna strone niz wczesniej.
    """)
    # -*- coding: ISO Latin-10 -*-
    subprocess.call("powrot-park.py", shell=True, encoding='latin-1')

