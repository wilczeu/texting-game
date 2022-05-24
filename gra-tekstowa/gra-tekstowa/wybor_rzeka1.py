#idziesz odprowadzic dziewczynke
import subprocess 

print("""'Ja odprowadze' mowisz szybko.

Dziewczynka podaza dzielnie tuz obok ciebie.

'Zaprowadzisz mnie do swojego domu?'

'yhym' - mruknela i pokiwala glowa.

Zapowiada sie podroz w ciszy.

Po dluzszym czasie, mijajac pole kukurydzy, docieracie do gospodarstwa.

'Twoi rodzice na pewno sa tutaj a nie w wiosce?' - zapytalem niepewnie.

'yhym' - mruknela i pokiwala glowa.

Weszlismy na podworko i od razu podbiegl do nas dosc sporawy kundel, szczekajac.

'Fafik! Wracaj no tu!' - krzyknal za nim jakis mezczyzna. Wyszedl zza budynku z wiadrem wody w rece. Podszedl do nas mruzac oczy. 'Ooo... to ty! Czesc sloneczko!' - przytulil dziewczynke.

'Dzien dobry' - przywitalem sie milo.

'Dobry dobry. Co sie jej stalo? Jakas taka przestraszona i przemoczona jest', byl wyraznie zmartwiony o swoja corke.

'Wpadla do rzeki niedaleko, gdy sie z dzieciakami bawila. Odprowadzilem ja wiec do domu, zeby upewnic sie ze bezpiecznie dotrze'.

Mezczyzna mruknal cos pod nosem i pokiwal glowa. Slomiany kapelusz delikatnie opadl mu przy tym na nos.

'Chodz kochanienka. Przygotuje ci suche ubrania, dobrzu?'

'Dobrze, tato'.

Odeszli kawalek, pies za nimi.

'Dziekuje ci bardzo, tak w ogole! Do zobaczenia na festynie!' - krzyknal przez ramie i mi pomachal na pozegnanie.

Odmachalem mu i wyszedlem z terenu gospodarstwa.

Popatrzylem w gore, zeby zobaczyc pozycje slonca. Bylo tuz po dziesiatej.
""")
wybor_gosp1=input("""Co robisz?:
1. Wracasz nad rzeke.
2. Idziesz do lasu.
3. Udajesz sie do wioski.
""")

if wybor_gosp1=='1': #nad rzeke wracasz
    print("""
    Jeszcze sporo czasu do festynu. Mozesz wiec spokojnie wrocic nad rzeke i sie nalezycie zrelaksowac.
    """)
    # -*- coding: latin-1 -*-
    subprocess.call("rzeka2.py", shell=True, encoding='latin-1')

if wybor_gosp1=='2': #las.py
    print("""
    W sumie znasz w lesie miejsca, w ktorych rosna ladne kwiaty o tej porze roku. Uznalez ze warto troche ich nazbierac z okazji pierwszego dnia wiosny.
   """)
    # -*- coding: latin-1 -*-
    subprocess.call("las.py", shell=True, encoding='latin-1')

if wybor_gosp1=='3': #wioska.py
    print("""
    Od zawsze lubiles wiosne i przygotowania. Idziesz wiec sprawdzic ich postepy. Moze tez potrzebuje ktos, by mu pomoc?
    """)
    # -*- coding: latin-1 -*-
    subprocess.call("wioska.py", shell=True, encoding='latin-1')