print("""Hejka! Jak sie nazywasz?
""")
#input to jest miejsce na wpisanie
name = input("Podaj swoje imie: ")
print("""
Milo mi cie poznac """ + name + """. Ja nie mam imienia. Chcesz mi je nadac?
""")
name2 = input("Tu podaj moje nowe imie: ")
print(""" 
""" + name2 + "? Piekne imie! Dziekuje!")
print("""Chcesz zostac moim przyjacielem?
""")
odp = input("Jaka jest twoja odpowiedz? - 'tak'/'t' lub 'nie'/'n': ")



if odp=='tak' or odp=='t':
    print("""
    Hurra! Od dzis """ + "  " + name + " oraz " + name2 + " sa przyjaciolmi!!!" )
else:
    print("""
    No dobrze...""")

#TU IMPORTOWAC ODP 2!!!!!!!!!!!!!!!!!!!!
import subprocess
# -*- coding: latin-1 -*-
subprocess.call("odp2.py", shell=True, encoding='latin-1')
# -*- coding: latin-1 -*-
subprocess.call("odp3.py", shell=True, encoding='latin-1')
