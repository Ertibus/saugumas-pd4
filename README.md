# 4 praktinė užduotis <br /> Sukurti slaptažodžių valdymo sistemą. 
## Privalomos slaptažodžių valdymo sistemos funkcijos:

* Paleidus sistemą pirmą kartą sukuriamas .csv arba .txt failas. Išjungiant sistemą šis failas turi būti užšifruojamas AES algoritmu. Kitą kartą paleidus sistemą failas yra dešifruojamas. (4 taškai)
* Naujo slaptažodžio išsaugojimas: užpildžius formą (pavadinimas, slaptažodis, URL/aplikacija, komentaras), visa jos informacija saugojama .csv arba .txt faile. Slaptažodžiui pritaikomas šifravimo algoritmas (pvz.: AES, DES ar RSA. Renkatės savo nuožiūra). (3 taškai)
* Slaptažodžio paieška pagal pavadinimą. (2 taškai)
* Slaptažodžio atnaujinimas pagal pavadinimą: suradus tinkamą slaptažodį jis pakeičiamas naujai įvestu. Naujam slaptažodžiui taip pat turi būti pritaikytas šifravimo algoritmas. (2 taškai) 
* Slaptažodžio ištrynimas pagal pavadinimą: suradus tinkamą slaptažodį visa informacija apie jį ištrinama iš .csv arba .txt failo. (2 taškai)

## Papildomos funkcijos:

* Paleidus sistemą pirmą kartą reikalinga vartotojo paskyros sukūrimo forma: slapyvardis, slaptažodis (šifruojamas PBKDF2, Bcrypt, Scrypt, Argon2 arba pasirenkant maišos funkciją). Kuriant vartotojo paskyrą yra sugeneruojamas ir vartotojui priskiriamas .csv arba .txt failas. Failas yra užšifruojamas AES algoritmu. (3 taškai)
* Prisijungimas prie sistemos: vartotojui prijungus failas dešifruojamas. (3 taškai)
* Atsitiktinio slaptažodžio generavimo funkcija (panaudojama kuriant naują slaptažodį). (2 taškai)
* Papildoma funkcija slaptažodžio paieškai pagal pavadinimą: suradus tinkamą slaptažodį jis iškart nerodomas, pateikiamas tik jo užšifruotas rezultatas. Paspaudus mygtuką rodyti parodomas slaptažodis. (2 taškai)
* Mygtukas galintis nukopijuoti slaptažodį į iškarpinę. (2 taškai) 

# Programos informacija
## Requirements:
Python 3.5.2+

PyQt5 (Can be installed with pip install pyqt5)

pyCrypto (Can be installed with pip install pycrypto)

Pyperclip (Can be installed with pip install pyperclip)
