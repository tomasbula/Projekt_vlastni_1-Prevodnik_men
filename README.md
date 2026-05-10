# PŘEVODNÍK MĚN

- autor: Ing. Tomáš Bula
- email: tomas.bula@post.cz
- GitHub: https://github.com/tomasbula
- vytvořeno: 05/2026

## Popis projektu
Tento projekt slouží jako převodník měn dle aktuálních kurzů ČNB.

Odkaz ZDE:
https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/

## Instalace knihoven
Knihovny, které jsou použity v kódu jsou ulozžené v souboru requirements.txt. Pro instalaci je doporučeno použít nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:

<pre>
$ pip3 --version                        # ověření verze manažeru
$ pip3 install -r requirements.txt      # instalace knihoven
</pre>

## Spuštění projektu
Spuštění souboru main.py se provádí přes terminál:
- Nejdříve program vypíše seznam dostupných měn, které čerpá z odkazu viz výše.
- Následně uživatel zadá výchozí měnu pomocí její zkratky (např.: CZK).
- Poté uživatel zadá zkratky měn, do kterých chce převádět (např.: EUR, USD).
- Nakonec uživatel zadá částku, kterou chce převést (např.: 1000).
- Program pak provede požadovaný převod a vypíše výsledek.

Prgram také disponuje možnosti opakování.

## Ukázka projektu
Výpočet převodu (výchozí měna: CZK; měny pro převod: EUR, USD; částka pro převod: 1000):

<pre>
----------------------------------------------------------------------
Vítejte v programu pro převod měn.
----------------------------------------------------------------------
Dostupné měny pro převod:
CZK: Česká republika
AUD: Austrálie
BRL: Brazílie
CNY: Čína
DKK: Dánsko
EUR: EMU
PHP: Filipíny
HKD: Hongkong
INR: Indie
IDR: Indonesie
ISK: Island
ILS: Izrael
JPY: Japonsko
ZAR: Jižní Afrika
CAD: Kanada
KRW: Korejská republika
HUF: Maďarsko
MYR: Malajsie
MXN: Mexiko
XDR: MMF
NOK: Norsko
NZD: Nový Zéland
PLN: Polsko
RON: Rumunsko
SGD: Singapur
SEK: Švédsko
CHF: Švýcarsko
THB: Thajsko
TRY: Turecko1)
USD: USA
GBP: Velká Británie
----------------------------------------------------------------------
Zadejte zkratku výchozí měny: 
CZK
----------------------------------------------------------------------
Zadejte zkratky měn (oddělené čárkou): 
EUR, USD
----------------------------------------------------------------------
Zadejte částku, kterou chcete převést: 
1000
----------------------------------------------------------------------
Výsledky převodu:
41.05 EUR
48.05 USD
----------------------------------------------------------------------
Chcete úrovést další převod? (ano/ne):
</pre>
