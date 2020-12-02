from math import gcd
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


def brent_rho(n):
    m = 1 << n.bit_length() // 8 + 1
    for c in range(1, 99):
        f = lambda x: (x * x + c) % n
        y, r, q, g = 2, 1, 1, 1
        while g == 1:
            x = y
            for _ in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                for _ in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            r <<= 1
        if g < n:
            if is_prime(g):
                return g
            elif is_prime(n // g):
                return n // g


def prime_factor(n):
    i = 2
    ret = {}
    while i * i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
        if k:
            ret[i] = k
        i += 1 + i % 2
        if i != 101 or n < 2 ** 20:
            continue
        while n > 1:
            if is_prime(n):
                ret[n], n = 1, 1
                continue
            j = brent_rho(n)
            k = 0
            while n % j == 0:
                n //= j
                k += 1
            ret[j] = k
    if n > 1:
        ret[n] = 1
    return ret


def prime_factor_with_sort(n):
    pf = prime_factor(n)
    ret = []
    for p in sorted(pf.keys()):
        ret += [p] * pf[p]
    return ret
