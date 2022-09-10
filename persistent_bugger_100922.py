def persistence(n=978):
    count_times = 0
    if len(str(n)) > 1:
        while True:
            new_n = 1
            for digit in str(n):
                new_n *= int(digit)
            count_times += 1
            if len(str(new_n)) == 1:
                break
            else:
                n = new_n

    print(count_times)
    return count_times


persistence()