# def array_diff(a, b):
#     result_list = []
#     if b != []:
#         for symbol in b:
#             for digit in a:
#                 if symbol != digit:
#                     result_list.append(digit)
#     else:
#         result_list = a
    
#     return result_list


# if __name__ == "__main__":
#     array_diff()


# def array_diff(a, b):
#     result_list = []
#     if b != []:
#         for symbol in a:
#             if symbol in b:
#                 continue
#             else:
#                 result_list.append(symbol)
#     else:
#         result_list = a
#     print(result_list)

#     return result_list


# if __name__ == "__main__":
#     array_diff()

def array_diff(a, b):
    return [x for x in a if x not in b]
