# def duplicate_count(text="abcdeaB"):
#     count_total = 0
#     for symbol_1 in text.lower():
#         count_double = 0
#         for symbol_2 in text.lower():
#             if symbol_1 == symbol_2:
#                 count_double += 1
#         if count_double >= 2:
#             count_total += 1
#             # text = text.lower().replace(symbol_2, '')
#         text = text.lower().replace(symbol_1, '')
#     # print(count_total)

#     return count_total

def duplicate_count(s="abcdeaB"):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])


duplicate_count()