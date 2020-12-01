def manacher(S):
    radius = [0] * len(S)
    i, j = 0, 0
    while i < len(S):
        while i - j >= 0 and i + j < len(S) and S[i - j] == S[i + j]:
            j += 1
        radius[i] = j
        k = 1
        while i - k >= 0 and i + k < len(S) and k + radius[i - k] < j:
            radius[i + k] = radius[i - k]
            k += 1
        i += k
        j -= k
    return radius

def palindromes(S):
    n = len(S)
    p = [[0] * (n + 1), [0] * n]
    for z in range(2):
        l, r = 0, 0
        for i in range(n):
            zz = 0 if z == 1 else 1
            t = r - i + zz
            if i < r:
                p[z][i] = min(t, p[z][l + t])
            L, R = i - p[z][i], i + p[z][i] - zz
            while L != 0 and R + 1 < n and S[L - 1] == S[R + 1]:
                p[z][i] += 1
                L -= 1
                R += 1
            if R > r:
                l = L
                r = R
    return p

def enumerate_palindromes(S):
    [even, odd] = palindromes(S)
    res = [0] * (2 * len(S) - 1)
    even = even[1::]
    for i in range(2 * len(S) - 1):
        if i % 2 == 0:
            res[i] = 2 * odd[i // 2] + 1
        else:
            res[i] = 2 * even[i // 2]
    return res
