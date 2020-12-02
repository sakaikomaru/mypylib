def sieve_of_eratosthenes(M=10 ** 6):
    p = [1] * (M + 1)
    p[0] = p[1] = 0
    for x in range(2, int(M ** 0.5) + 1):
        if p[x]:
            for y in range(x * x, M + 1, x):
                p[y] = 0
    return p

def enumerate_primes(M = 10 ** 6):
    if M <= 1:
        return []
    d = sieve_of_eratosthenes(M)
    primes = []
    for i in range(len(d)):
        if d[i]:
            primes.append(i)
    return primes
