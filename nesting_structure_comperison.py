# def same_structure_as(original=[ [ [ ], [ ] ] ], other=[ [ 1, 1 ] ]):
#     original_str, other_str = str(original), str(other)
#     result_list = []
#     if len(original_str) == len(other_str):
#         for item in range(len(original_str)):
#             if original_str[item].isdigit() and other_str[item].isdigit():
#                 result_list.append(True)
#             elif original_str[item] == other_str[item]:
#                 result_list.append(True)
#             else:
#                 result_list.append(False)
#         print(result_list)
#         if False in result_list:
#             result = False
#         else:
#             result = True
#     else:
#         result = False
#     # print(result)    
#     return result

def same_structure_as(original=[ [ [ ], [ ] ] ], other=[ [ 1, 1 ] ]):
    if type(original) != list or type(other) != list or len(original) != len(other) or type(original) != type(other):
        return False
    for x, y in zip(original, other):
        if type(x) != type(y) and x not in other:
            return False
        if type(x) == list and type(y) == list:
            return same_structure_as(x,y)
    return True


same_structure_as()
