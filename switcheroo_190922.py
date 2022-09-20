# def switcheroo(s='aabacbaa' ):
#     new_str = ""
#     for letter in s:
#         if letter == "a":
#             new_str += "b"
#         elif letter == "b":
#             new_str += "a"
#         else:
#             new_str += letter
#     print(new_str)

#     return new_str


def switcheroo(string):
    return ((string.replace('a','x')).replace('b','a')).replace('x','b')


switcheroo()