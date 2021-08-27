# py2 sameNAttack.py
import primefac


def same_n_attack(n, e1, e2, c1, c2):
    def egcd(a, b):
        x, lastX = 0, 1
        y, lastY = 1, 0
        while b != 0:
            q = a // b
            a, b = b, a % b
            x, lastX = lastX - q * x, x
            y, lastY = lastY - q * y, y
        return lastX, lastY

    s = egcd(e1, e2)
    s1 = s[0]
    s2 = s[1]
    if s1 < 0:
        s1 = -s1
        c1 = primefac.modinv(c1, n)
        if c1 < 0:
            c1 += n
    elif s2 < 0:
        s2 = -s2
        c2 = primefac.modinv(c2, n)
        if c2 < 0:
            c2 += n
    m = (pow(c1, s1, n) * pow(c2, s2, n)) % n
    return m
