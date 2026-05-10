#####   PREVODNÍK MĚN   #####

# autor: Ing. Tomáš Bula
# vytvořeno: 05/2026

# Popis:
# Program stáhne dostupné měny a kurzy ze stránek:
# https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/
# Mezi těmito měnami lze provadět libovolně převody.
# Do programu je zakomponována i možnost jeho opakování dle potřeby uživatele.

# Potřebné knihovny
import requests
from bs4 import BeautifulSoup

# Délka separatoru pro oddělení jednotlivých částí programu
delka_separatoru = 70

# Zdrojové webové stránky
ZDROJOVY_URL = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/"


# Funkce pro získání HTML kódu webové stránky
def ziskani_HTML(url):

    """Funkce pro získání obsahu webové stránky."""

    try:
        HTML_kod = requests.get(url, timeout=10)
    except requests.RequestException as e:
        print(f"Chyba při načítání stránky: {e}")
        return None
    if HTML_kod.status_code == 200:
        HTML_kod.encoding = "utf-8"
        web = BeautifulSoup(HTML_kod.text, "html.parser")
        return web
    else:
        print(f"Chyba při načítání stránky (HTTP {HTML_kod.status_code})")
        return None


def ziskani_nazvu_statu(web):
    
    """Vrátí seznam názvů všech států"""
    
    nazvy_statu = []

    tabulka = web.find("table")

    radky = tabulka.find_all("tr")

    for radek in radky[1:]:  # přeskočí hlavičku
        bunky = radek.find_all("td")
        nazev_statu = bunky[0].text.strip()
        nazvy_statu.append(nazev_statu)

    return nazvy_statu


def ziskani_zkratek_men(web):
   
    """Vrátí seznam zkratek měn (např. EUR, USD, GBP...)."""
    
    zkratky = []

    tabulka = web.find("table")
   
    radky = tabulka.find_all("tr")

    for radek in radky[1:]:  # přeskočí hlavičku
        bunky = radek.find_all("td")
        zkratka = bunky[3].text.strip()
        zkratky.append(zkratka)

    return zkratky


def ziskani_kurzu_men(web):
   
    """Vrátí seznam kurzů měn vůči CZK"""
    
    kurzy = []

    tabulka = web.find("table")
   
    radky = tabulka.find_all("tr")

    for radek in radky[1:]:  # přeskočí hlavičku
        bunky = radek.find_all("td")
        kurz = bunky[4].text.strip()
        kurzy.append(kurz)

    return kurzy


def ziskani_mnozstvi_men(web):
   
    """Vrátí seznam množství měn"""
    
    mnozstvi = []

    tabulka = web.find("table")
   
    radky = tabulka.find_all("tr")

    for radek in radky[1:]:  # přeskočí hlavičku
        bunky = radek.find_all("td")
        mnozstvi_meny = bunky[2].text.strip()
        mnozstvi.append(mnozstvi_meny)

    return mnozstvi


def ziskani_dostupnych_men():

    """Funkce pro získání dstupných měn z webové stránky a přidání CZK do seznamu"""

    web = ziskani_HTML(ZDROJOVY_URL)

    zkratky_men = ziskani_zkratek_men(web)

    staty = ziskani_nazvu_statu(web)

    kurzy_men = ziskani_kurzu_men(web)

    mnozstvi_men = ziskani_mnozstvi_men(web)

    # Přvedení kurzů na desetinné číslo (float) a nahrazení čárky tečkou pro správný formát
    kurzy_men_float = []
    for k in kurzy_men:
        kurzy_men_float.append(float(k.replace(",", ".")))
    
    # Převedení množství na celé číslo (int)
    mnozstvi_int = []
    for m in mnozstvi_men:
        mnozstvi_int.append(int(m))
    
    # Finální kurzy pro převod budou vypočítány jako kurz děleno množství
    finalni_kurzy = []
    for k, m in zip(kurzy_men_float, mnozstvi_int):
        finalni_kurzy.append(k / m)

    dostupne_meny = {
        zkratky_men: [staty, finalni_kurzy]
        for zkratky_men, staty, finalni_kurzy in zip(zkratky_men, staty, finalni_kurzy)
    }

    # Přidání CZK do dostupných měn (důležité pro výpočet převodu)
    ceska_republika = {"CZK": ["Česká republika", 1.00]}
    dostupne_meny = {**ceska_republika, **dostupne_meny}

    return dostupne_meny


def separator():
    
    """Funkce pro oddělení jednotlivých částí programu"""
    
    print("-" * delka_separatoru)


def zkratky_a_nazvy_men(dostupne_meny) -> list:
    
    """Funkce pro získání zkratky všech dostupných měn"""
    
    zkratky_men = []
    nazvy_men = []

    for mena in dostupne_meny:
        zkratky_men.append(mena)
        nazvy_men.append(dostupne_meny[mena][0])

    seznam_men = dict(zip(zkratky_men, nazvy_men))

    return seznam_men


def vypis_dostupnych_men(seznam_dostupnych_men):
    
    """Funkce pro výpis dostupných měn pro převod"""
    
    vystup = ""

    for klic, hodnota in seznam_dostupnych_men.items():
        vystup += f"{klic}: {hodnota}\n"
    
    return vystup.strip()


def vyber_men_pro_prevody() -> list:
    
    """Funkce pro výber měn pro převod, které uživatel chce použít"""

    vstup = input("Zadejte zkratky měn (oddělené čárkou): \n")
    
    rozdeleny_seznam = vstup.split(",")
    
    vyber_uzivatele = []
    separator()
    
    for polozka in rozdeleny_seznam:
        cista_mena = polozka.strip().upper()
        
        if cista_mena: 
            vyber_uzivatele.append(cista_mena)
    
    return vyber_uzivatele


def castka_k_prevodu() -> float:
    
    """Funkce pro zadání částky k převodu"""

    while True:
        vstup = input("Zadejte částku, kterou chcete převést: \n")

        separator()
        
        try:
            castka = float(vstup)
            if castka < 0:
                print("Částka nemůže být záporná. Zkuste to znovu.")
                separator()
                continue
            
            return castka
        
        except ValueError:
            print("Neplatný vstup. Zadejte prosím číslo.")
            separator()


def kurzy_vybranych_men(vyber_uzivatele, dostupne_meny) -> dict:
    
    """Funkce pro získání kurzů vybraných měn uživatelem pro převod"""
    
    kurzy = {}

    for mena in vyber_uzivatele:
        if mena in dostupne_meny:
            kurzy[mena] = dostupne_meny[mena][1]
        else:
            print(f"Měna '{mena}' není dostupná pro převod. Ignoruji ji.")
            separator()
    
    return kurzy


def vychozi_mena() -> str:
    
    """Funkce pro výběr výchozí měny"""
   
    while True:

        vstup = input("Zadejte zkratku výchozí měny: \n").strip().upper()
        separator()

        if not vstup:
            print("Nezadali jste žádnou měnu. Zkuste to znovu.")
            separator()
        
        elif vstup not in dostupne_meny:
            print(f"Měna '{vstup}' není dostupná pro převod. Zkuste to znovu.")
            separator()
        
        else:
            return vstup


def prevod_na_czk(castka, vych_mena, dostupne_meny) -> float:
    
    """Funkce pro převod z výchozí měny na CZK"""

    if vych_mena in dostupne_meny:
        kurz = dostupne_meny[vych_mena][1]
        castka_v_czk = castka * kurz
        return castka_v_czk
    
    if vych_mena == "CZK":
        return castka

    else:
        print(f"Měna '{vych_mena}' není dostupná pro převod. Zkuste to znovu.")
        separator()
        return None


def vypocet_prevodu(castka, kurzy):
    
    """Funkce pro výpočet převodu z CZK do vybraných měn"""
    
    prevody = {}

    for mena, kurz in kurzy.items():
        prevody[mena] = round(castka / kurz, 2)
    
    print("Výsledky převodu:")

    for p in prevody:
        print(f"{prevody[p]} {p}")

    separator()


# Získání dostupných měn a kurzů z webu
dostupne_meny = ziskani_dostupnych_men()


def prevodnik_men():
    
    """Hlavní funkce pro spuštění převodníku"""

    # Pozdrav uživatele
    separator()
    print("Vítejte v programu pro převod měn.")
    separator()

    # Výpis seznamu dostupných měn pro převod vůči CZK
    print("Dostupné měny pro převod:")
    seznam_dostupnych_men = zkratky_a_nazvy_men(dostupne_meny)
    dostupne_meny_vypis = vypis_dostupnych_men(seznam_dostupnych_men)
    print(dostupne_meny_vypis)
    separator()

    # Výběr výchozí měny pro převod
    vych_mena = vychozi_mena()

    # Výběr uživatele pro měny, které chce použít pro převod
    vyber = vyber_men_pro_prevody()

    # Zadání částky k převodu v CZK
    castka = castka_k_prevodu()

    # Převod částky z výchozí měny na CZK (pokud není výchozí měna již CZK)
    castka_v_czk = prevod_na_czk(castka, vych_mena, dostupne_meny)

    # Kurzy vybranych měn pro převod
    kurzy = kurzy_vybranych_men(vyber, dostupne_meny)

    # Výpočet převodu z CZK do vybraných měn
    prevody = vypocet_prevodu(castka_v_czk, kurzy)


def opakovani_prevodniku_men():
    
    """Funkce pro opakování převodníku měn"""

    while True:
        prevodnik_men()
        
        # Opakovaní nebo ukončení převodníku měn na základě uživatelského vstupu
        opakovat = input("Chcete úrovést další převod? (ano/ne): ").strip().lower()
        separator()
        
        if opakovat != "ano":
            print("Ukončuji převodník měn. Děkuji za použití!")
            separator()
            break


if __name__ == "__main__":
    opakovani_prevodniku_men()