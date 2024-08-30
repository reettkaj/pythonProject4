while True:
    tuumat = float(input("Anna tuumien määrä, negatiivinen luku lopettaa ohjleman.: "))
    if tuumat < 0:
        print("Ohjelma lopetetaan.")
        break

    sentit= tuumat * 2.54
    print(F"(tuumat)Tuumaa on {sentit:.2f} senttimetriä.")
