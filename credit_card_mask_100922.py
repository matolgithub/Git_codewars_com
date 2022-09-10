# # return masked string
# def maskify(cc='123456789'):
#     masked_string =''
#     if 0 <= len(cc) <= 4:
#         masked_string = cc
#     else:
#         masked_string = '#' * (len(cc) - 4) + cc[-4:]
    
#     # print(masked_string)
#     return masked_string


# maskify()

# return masked string
def maskify(cc='123456789'):
    
    return cc if 0 <= len(cc) <= 4 else '#' * (len(cc) - 4) + cc[-4:]
