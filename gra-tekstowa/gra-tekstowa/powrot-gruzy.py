# -*- coding: latin-1 -*-
#powrot - gruzy
kierunek4 = input("Ju¿ nie ma odwrotu. Wybierz opcje 1 lub 2, wpisujac odpowiednia cyfre: ")
if kierunek4 == '1': #znowu do kobiety, ale po zawroceniu:
    print("""Mezczyzna pewnie sobie poradzi', powiedziales cicho i ruszyles za glosem kobiety. 
    Na szczêscie szybko udalo ci sie ja znalezc. Niby szybko, ale jednak za pozno, by jej jakkolwiek pomoc.
    By³a przysypana gruzem, nogi przygniotl jej jakis filar. Sam juz nic nie mogles zdzialac.

    'Spokojnie', usmiechnela sie blado. 'Dziekuje ci, ze nie umieram sama...'.

    'Ja... Ja moge cos zrobic!'
    
    'Nie. Juz nic nie mozesz zrobic, ale...' zakaszlala. 'Za parkiem jest mala chatka, powinno byc tam bezpiecznie. Schowaj sie tam, zgromadz zapasy i wychodz jak najmniej'.

    'Ale...!'

    Kobieta zaczela sie krztusic krwia i machnela reka, zebys juz uciekal. Przez chwile chciales szukac mezczyzny, ale jego glos juz dawno ucichl. Pewnie byl w podobnym stanie co kobieta, a trup w niczym ci nie pomoze.
    Na miêkkich nogach idziesz wiec szukac chatki. Nie bylo to trudne. """)
    subprocess.call("chata-sam.py", shell=True, encoding='latin-1')