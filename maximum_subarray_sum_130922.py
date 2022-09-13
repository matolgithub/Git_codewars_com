# def max_sequence(arr=[-21, -21, 29, 14, -25, -10, 9, 1, 9, -25, -11, -14, -1, -27, -4, 2, -3, 7, -7, -17, 9, 1, 10, 25, -29, 6, -21, -7, 25, 0, 24, -4, -10, -19, -23, 18, -22, 3, -7, -23, -22, -1, -23, -10, 19, 10, -22, 19, -16, 17]):
    # max = 0
    # max_length =  len(arr)
    # min_length = 0
    # result = 0
    # dict_max = []
    # if arr != []:
    #     while min_length != max_length:
    #         for element in range(min_length, max_length):
    #             for max_len in range(max_length):
    #                 max_list = [item for item in arr[min_length: max_len]]
    #                 # dict_max[sum(max_list)] = max_list
    #                 dict_max.append(sum(max_list))
    #                 if sum(max_list) > result:
    #                     result = sum(max_list)
    #             min_length += 1
    # print(result)
    # # print(dict_max)

    # return result

    # maximum = 0
    # local_maximum = 0
    # for i in arr:
    #     if local_maximum > 0:
    #         local_maximum += i
    #         if local_maximum < 0:
    #             local_maximum = 0
    #         elif local_maximum > maximum:
    #             maximum = local_maximum
    #     elif i > 0:
    #         local_maximum += i
    # # print(maximum)
    # return maximum

def max_sequence(arr=[1, 3, -7, 10]):
    max, curr = 0, 0
    for x in arr:
        curr += x
        if curr < 0:
            curr = 0 
        if curr > max:
            max = curr
    print(max)
    return max


max_sequence()
