def zero_and_one(s="0101011110011101001100011011100010100"):
    # total_count = len(s.replace("10", "").replace("01", ""))
    # # print(total_count)
    # return total_count
    # print(s.replace("10", "").replace("01", ""))
    s = s.replace("10", "")
    s = s.replace("01", "")
    print(s)
    print(len(s))

zero_and_one()