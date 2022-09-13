# def pig_it(text='Pig latin is cool !'):
#     list_text = text.split()
#     new_list = []
#     for item in list_text:
#         if item.isalpha():
#             item = item[1:] + item[0] + 'ay'
#             # print(item)
#             new_list.append(item)
#         else:
#             new_list.append(item)
#     new_text = ' '.join(new_list)
#     # print(new_text)
#     return new_text


from curses.ascii import isalpha


def pig_it(text='Pig latin is cool !'):
    # list_text = text.split()
    # new_list = []
    # for item in list_text:
    #     if item.isalpha():
    #         item = item[1:] + item[0] + 'ay'
    #         new_list.append(item)
    #     else:
    #         new_list.append(item)
    # new_text = ' '.join(new_list)
    # print(new_text)
    print(' '.join(list(item[1:] + item[0] + 'ay' if item.isalpha() else item for item in text.split())))
    return ' '.join(list(item[1:] + item[0] + 'ay' if item.isalpha() else item for item in text.split()))

pig_it()