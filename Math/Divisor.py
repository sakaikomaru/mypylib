def divisor(n):
    ret = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ret.append(i)
            if i * i != n:
                ret.append(n // i)
        i += 1
    return sorted(ret)
