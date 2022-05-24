#powrot do parku/ - pojdz na gruzy lub do chaty
kierunek3 = input("""Aby wybrac opcje, wpisz 1 lub 2:  """)

if kierunek3=='1': #gruzy
    print("test1")
    # -*- coding: latin-1 -*-
    subprocess.call("powrot-gruzy.py", shell=True, encoding='latin-1')


    

if kierunek3=='2': #chata
    print("test2")
    # -*- coding: latin-1 -*-
    subprocess.call("chata-sam.py", shell=True, encoding='latin-1')
