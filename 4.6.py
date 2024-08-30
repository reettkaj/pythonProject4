import random
pisteiden_määrä = int(input("Anna pisteiden määrä: "))
n_ympyrän_sisällä = 0

for _ in range(pisteiden_määrä):
    x = random.uniform(- 1,1)
    y = random.uniform(-1,1)
    if x**2 + y**2 < 1:
        n_ympyrän_sisällä += 1

pi_likiarvo = 4 * n_ympyrän_sisällä / pisteiden_määrä
print(f"Piin likiarvo on: {pi_likiarvo:.6f}")