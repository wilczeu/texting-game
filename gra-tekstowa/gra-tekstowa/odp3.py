# -*- coding: latin-1 -*-
    
#poczatek historii-przygody
#park, gruzy i stara chata


print(" ")
name = input("""
Przed wybraniem opcji, podaj imie dla swojej postaci:  """)
odp3 = input("""
Wybierz opcjê 1 lub 2:  """)

import subprocess

if odp3 == '1':
    print("""
    """ + name + """, budzisz sie zdezorientowany na jakies drewnianej, brudnej lawce. Rozgladasz sie.
    Wyglada na to, ze jestes w zostawionym samemu sobie parku. Stare drzewa otulone mgla, wygladaja jak potwory z najstraszniejszych horrorow.
    Nigdzie ani jednej zywej duszy.
    Grzmot, trzy sekundy pozniej blysk.
    Chyba zapowiada sie burza.
    Od lawki, na ktorej sie obudziles, mozesz isc w dwie strony. 
    W lewo - l, lub prawo - p.""")
    # -*- coding: latin-1 -*-
    subprocess.call("kierunek1.py", shell=True, encoding='latin-1')

    

if odp3 =='2':
    print("""
    Wlasnie wyszedles ze swojej chatki na uboczu wioski. Jest piekny dzien. Swieci slonce, z zachodu wieje przyjemny, cieply wiatr. Od rana we wszystkich gospodarstwach trwa rowniez przygotowanie do uroczystosci pierwszego dnia wiosny, ktora ma sie odbyc dzisiaj w poludnie.
    
    Gdzie zamierzasz najpierw pojsc?:
    1. Nad rzeke, nazbierac jakis ladnych kamyczkow do pomalowania.
    2. Do wioski, aby zobaczyc jak ida przygotowania.
    3. Do lasu, aby nazbierac ladnych kwiatow na uroczystosc.

    """)
    # -*- coding: latin-1 -*-
    subprocess.call("wybor1-domek.py", shell=True, encoding='latin-1')
    exit(0)