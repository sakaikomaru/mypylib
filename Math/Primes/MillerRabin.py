from random import randint


def miller_rabin(n, check):
    d, s = n - 1, 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for a in check:
        if n <= a:
            return True
        a = pow(a, d, n)
        if a == 1:
            continue
        r = 1
        while a != n - 1:
            if r == s:
                return False
            a = a * a % n
            r += 1
    return True


def is_prime32(n):
    return miller_rabin(n, [2, 7, 61])


def is_prime64(n):
    return miller_rabin(n, [2, 3, 5, 7, 325, 9375, 28178, 450775, 9780504, 1795265022])


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n & 1 == 0:
        return False
    if n < 4759123141:
        return is_prime32(n)
    if n < 18446744073709551615:
        return is_prime64(n)
    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1
    for _ in range(100):
        a = randint(1, n - 1)
        t = d
        y = pow(a, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = (y * y) % n
            t <<= 1
        if y != n - 1 and t & 1 == 0:
            return False
    return True
