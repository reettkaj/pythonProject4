import random
tietokoneen_luku= random.randint(1 , 10)
print("Arvaa kokonaisluku väliltä 1-10.")

while True:
    pelaajan_arvaus = int(input("Anna arvauksesi: "))

    if pelaajan_arvaus < tietokoneen_luku:
        print("Liian pieni luku.")
    elif pelaajan_arvaus > tietokoneen_luku:
        print("Liian iso luku.")
    else:
        print("Oikein!")
        break


