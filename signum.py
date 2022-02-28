number = input("Írj be egy számot!")


if int(number) > 0:
    print("Pozitív")
elif int(number) < 0:
    print("Negatív")
else:
    print("A szám nulla.")

birth_year = int(input("Ír be, melyik évben születtél!"))

if birth_year > 2022 or 2022 < birth_year:
    print("Hiba!")
elif birth_year < 2020:
    print("Te nem ebben az évtizedben születtél.")
else:
    print("Te ebben az évtizedben születtél.")

