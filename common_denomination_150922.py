def convert_fracts(lst):
    if type(lst) == list:
        new_lst = []
    elif type(lst) == tuple:
        new_lst = ()
    # elif type(lst) == dict:
    #     new_lst = {}
    list_denom = [item[1] for item in lst]
    min_denom = 1
    length_list = len(lst)

    while True:
        count = 0
        for item in list_denom:
            if min_denom % item == 0:
                count += 1
        if count == length_list:
            break
        else:
            min_denom += 1
        
    for item in lst:
        index = int(min_denom / item[1])
        if type(item) == list:
            new_lst.append([(item[0] * index), (item[1] * index)])
        elif type(item) == tuple:
            new_lst += (((item[0] * index), (item[1] * index)), )
        # elif type(item) == dict:
        #     new_lst += frozenset({item[0] * index, item[1] * index})
    # print(new_lst)

    return new_lst

convert_fracts()
