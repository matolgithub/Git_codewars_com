from curses.ascii import isdigit


def same_structure_as(original=[ [ [ ], [ ] ] ], other=[ [ 1, 1 ] ]):
    original_str, other_str = str(original), str(other)
    result_list = []
    if len(original_str) == len(other_str):
        for item in range(len(original_str)):
            if original_str[item].isdigit() and other_str[item].isdigit():
                result_list.append(True)
            elif original_str[item] == other_str[item]:
                result_list.append(True)
            else:
                result_list.append(False)
        print(result_list)
        if False in result_list:
            result = False
        else:
            result = True
    else:
        result = False
    print(result)    
    return result


same_structure_as()
