def nty_wyraz(a1, q, n):
    an = a1 * (q**(n - 1))
    return an

def suma(a1, q, n):
    if q == 1:
        sn = a1 * n
    else:
        sn = a1 * ((1 - q**n) / (1 - q))
    return sn
