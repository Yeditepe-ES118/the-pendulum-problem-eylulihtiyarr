def find_period(L0: int, L1: int):
    """
    Prints periods for pendulum lengths between L0 and L1 (inclusive),
    and returns (T0, T1) for L0 and L1 respectively.
    """
    if not (isinstance(L0, int) and isinstance(L1, int)):
        raise TypeError("L0 and L1 must be integers")
    if not (L1 > L0 > 0):
        raise ValueError("L1 must be greater than L0, and both > 0")

    T0 = 2 * 3.14159 * ((L0 / 9.81) ** 0.5)
    T1 = 2 * 3.14159 * ((L1 / 9.81) ** 0.5)

    for L in range(L0, L1 + 1):
        T = 2 * 3.14159 * ((L / 9.81) ** 0.5)
        print(f"When L = {L:5.1f} m,  T = {T:4.1f} s")

    return T0, T1
