# def comp(array1=[121, 144, 19, 161, 19, 144, 19, 11], array2=[121, 14641, 20736, 361, 25921, 361, 20736, 361]):
    # array1 = sorted(list(item ** 2 for item in array1))
    # array2 = sorted(array2)
    # print(array1)
    # print(array2)

    # return False  if sorted(list(item ** 2 for item in array1)) != sorted(array2) or array1 is None or array2 is None else True


# def comp(array1=[121, 144, 19, 161, 19, 144, 19, 11], array2=[121, 14641, 20736, 361, 25921, 361, 20736, 361]):
#     if array1 is None or array1 == [] or array1 == {}:
#         return False
#     elif array2 is None or array2 == [] or array2 == {}:
#         return False
#     elif sorted(list(item ** 2 for item in array1)) != sorted(array2):
#         return False
#     elif len(array1) != len(array2):
#         return False
#     else:
#         return True

# def comp(array1=[121, 144, 19, 161, 19, 144, 19, 11], array2=[121, 14641, 20736, 361, 25921, 361, 20736, 361]):
#     if array1 is None or array2 is None:
#         return False
#     elif array1 == [] and array2 == []:
#         return True
#     elif array1 == [] or array1 == {}:
#         return False
#     elif array2 == [] or array2 == {}:
#         return False
#     elif sorted(list(item ** 2 for item in array1)) != sorted(array2):
#         return False
#     elif len(array1) != len(array2):
#         return False
#     elif sorted(list(item ** 2 for item in array1)) == sorted(array2):
#         return True

# def comp(array1, array2):
#     try:
#         return sorted([i ** 2 for i in array1]) == sorted(array2)
#     except:
#         return False


def comp(a1, a2):
    return isinstance(a1, list) and isinstance(a2, list) and sorted(x*x for x in a1) == sorted(a2)


comp()
