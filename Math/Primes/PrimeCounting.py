def countPrimes(n):
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
