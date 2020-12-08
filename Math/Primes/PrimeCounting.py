def count_primes(n):
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

def faster_count_primes(n):
    v = int(n ** 0.5)
    higher = [0] * (v + 2)
    lower  = [0] * (v + 2)
    used   = [False] * (v + 2)
    result = n - 1
    for p in range(2, v + 1):
        lower[p] = p - 1
        higher[p] = n // p - 1
    for p in range(2, v + 1):
        if lower[p] == lower[p - 1]:
            continue
        temp = lower[p - 1]
        result -= higher[p] - temp
        pxp = p * p
        end = min(v, n // pxp)
        j = 1 + (p & 1)
        for i in range(p + j, end + 2, j):
            if used[i]:
                continue
            d = i * p
            if d <= v:
                higher[i] -= higher[d] - temp
            else:
                higher[i] -= lower[n // d] - temp
        for i in range(v, pxp - 1, -1):
            lower[i] -= lower[i // p] - temp
        for i in range(pxp, end + 1, p * j):
            used[i] = True
    return result

def fastest_count_primes(n):
    if n < 2:
        return 0
    v = int(n ** 0.5) + 1
    smalls = [i // 2 for i in range(1, v + 1)]
    smalls[1] = 0
    s = v // 2
    roughs = [2 * i + 1 for i in range(s)]
    larges = [(n // (2 * i + 1) + 1) // 2 for i in range(s)]
    skip = [False] * v

    pc = 0
    for p in range(3, v):
        if smalls[p] <= smalls[p - 1]:
            continue

        q = p * p
        pc += 1
        if q * q > n:
            break
        skip[p] = True
        for i in range(q, v, 2 * p):
            skip[i] = True

        ns = 0
        for k in range(s):
            i = roughs[k]
            if skip[i]:
                continue
            d = i * p
            larges[ns] = larges[k] - (larges[smalls[d] - pc] if d < v else smalls[n // d]) + pc
            roughs[ns] = i
            ns += 1
        s = ns
        for j in range((v - 1) // p, p - 1, -1):
            c = smalls[j] - pc
            e = min((j + 1) * p, v)
            for i in range(j * p, e):
                smalls[i] -= c

    for k in range(1, s):
        m = n // roughs[k]
        s = larges[k] - (pc + k - 1)
        for l in range(1, k):
            p = roughs[l]
            if p * p > m:
                break
            s -= smalls[m // p] - (pc + l - 1)
        larges[0] -= s

    return larges[0]
