def euler_phi(n):
    p = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            p = p * (i - 1) // i
            while n % i == 0:
                n //= i
        i += 1
    return [p, p * (n - 1) // n][n > 1]

def euler_phi_table(n):
    euler = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if euler[i] == i:
            for j in range(i, n + 1, i):
                euler[j] = euler[j] // i * (i - 1)
    return euler

