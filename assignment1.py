import math

def find_period(L0, L1):
    g = 9.81  # yerçekimi ivmesi
    for L in range(L0, L1 + 1):
        T = 2 * math.pi * math.sqrt(L / g)
        print("When L =", round(float(L), 1), "m, T =", round(T, 1), "s")

    # ilk ve son uzunluklar için periyotlar
    T0 = 2 * math.pi * math.sqrt(L0 / g)
    T1 = 2 * math.pi * math.sqrt(L1 / g)
    return T0, T1

# örnek çalıştırma
find_period(2, 10)
