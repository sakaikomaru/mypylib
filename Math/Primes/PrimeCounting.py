def prime_counting(n):
    r = int(n ** 0.5)
    assert r * r <= n and (r + 1) ** 2 > n
    V = [0] + [n // i for i in range(1, r + 1)]
    V += list(range(V[-1] - 1, 0, -1))
    S = [i - 1 for i in V]
    for p in range(2, r + 1):
        if S[-p] > S[-p + 1]:
            sp = S[-p + 1]
            p2 = p * p
            for i in range(1, 2 * r + 1):
                v = V[i]
                if v < p2:
                    break
                S[i] -= (S[-(v // p) if v // p <= r else i * p] - sp)
    return S[1]