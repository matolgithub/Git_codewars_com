from itertools import permutations

def next_bigger(n=1234567089):
    possible_number_list = []
    result_number = -1
    if len(str(n)) > 1:
        possible_number_list = [''.join(simb) for simb in permutations(str(n))]
        possible_number_list = list(set(possible_number_list))
        possible_number_list = sorted([int(item) for item in possible_number_list])
        if len(possible_number_list) > 1:
            search_index = possible_number_list.index(n) + 1
            result_number = possible_number_list[search_index]
            # print(possible_number_list)
            # print(search_index, result_number)
    print(result_number)
    return result_number


next_bigger()
