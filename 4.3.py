luvut = []

while True:
    syöte = input("Anna luku, tyhjä merkkijono lopettaa toiminnan: ")
    if syöte == "":
        break

    try:
        luku = float(syöte)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen syöte, anna jokin luku.")

if luvut:
    pienin = min(luvut)
    suurin = max(luvut)
    print("Pienin luku on", pienin)
    print("Suurin luku on", suurin)