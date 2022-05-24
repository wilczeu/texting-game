#PRZYGODA - LAS
#wioska, rzeka czy las?
import subprocess 

wybor1=input("""Aby wybrac opcje, wpisz odpowiednio 1, 2 lub 3:  """)

#1. Nad rzeke, nazbierac jakis ladnych kamyczkow do pomalowania.
if wybor1=='1':
    print("""Jest tak cieplo... rzeka wydaje sie byc najbardziej kuszaca opcja. """)
    # -*- coding: latin-1 -*-
    subprocess.call("rzeka.py", shell=True, encoding='latin-1')

#2. Do wioski, aby zobaczyc jak ida przygotowania.
if wybor1=='2':
    print("""Od zawsze lubiles wiosne i przygotowania. Idziesz wiec sprawdzic ich postepy. Moze tez potrzebuje ktos, by mu pomoc? """)

#3. Do lasu, aby nazbierac ladnych kwiatow na uroczystosc.
if wybor1=='3':
    print("""Moze i nie jestes zbyt dobry w przygotowaniu uroczystosci, no ale kwiaty w taki dzien sa obowiazkowe. Nazbierac nie zaszkodzi. """)
