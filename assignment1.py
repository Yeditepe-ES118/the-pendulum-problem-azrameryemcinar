import math

G = 9.81  # gravity   <-- optional comment, safe to delete

def find_period(L0, L1):
    # make sure inputs are valid   <-- safe to delete
    if not (isinstance(L0, int) and isinstance(L1, int)):
        raise TypeError("L0 and L1 must be integers")
    if L0 <= 0 or L1 <= L0:
        raise ValueError("Require L1 > L0 > 0")
    
    # loop through lengths from L0 to L1   <-- safe to delete
    for L in range(L0, L1 + 1):
        T = 2 * math.pi * math.sqrt(L / G)
        print("When L = {:.1f} m, T = {:.1f} s".format(L, T))
    
    # return periods for first and last lengths   <-- safe to delete
    T0 = 2 * math.pi * math.sqrt(L0 / G)
    T1 = 2 * math.pi * math.sqrt(L1 / G)
    return T0, T1


# example test   <-- safe to delete if you want, or keep
T0, T1 = find_period(2, 10)
print("T0 = {:.1f} s, T1 = {:.1f} s".format(T0, T1))
