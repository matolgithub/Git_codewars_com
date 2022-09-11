# def solution(s="ghghghHdjdjdLcncn"):
#     new_string = ""
#     for symbol in s:
#         if symbol != symbol.upper():
#             new_string += symbol
#         else:
#             new_string += symbol.replace(symbol, f" {symbol}")
#     print(new_string)
#     return new_string

def solution(s="ghghghHdjdjdLcncn"):
    # print(''.join(' ' + c if c.isupper() else c for c in s))
    return ''.join(' ' + c if c.isupper() else c for c in s)

solution()

