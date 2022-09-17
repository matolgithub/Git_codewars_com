def zeros(n=30):
    degree = 1
    num_zero = 0
    while n > 5 ** degree:
        d = int(n / 5 ** degree)
        num_zero += d
        degree += 1
    print(num_zero)
    return num_zero


zeros()