from ctypes import pythonapi

input("Anna käyttäjätunnus:")
input("Anna salasana:")

oikea_käyttäjätunnus = "python"
oikea_salasana = "rules"

max_yritykset = 5
yritykset = 0

while yritykset < max_yritykset:
    käyttäjätunnus= input("Anna käyttäjätunnus: ")
    salasana= input("Anna salasana: ")

    if käyttäjätunnus == oikea_käyttäjätunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    else:
        yritykset += 1
        if yritykset < max_yritykset:
            print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")
else:
    print("Pääsy evätty.")

