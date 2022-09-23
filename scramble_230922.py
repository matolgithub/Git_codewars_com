from collections import Counter

def scramble(s1='wiphxiwxnxdrzwwrrtmc', s2='rrzprrww'):
# def scramble(s1='wiphx', s2='iph'):
    # print(False if False in [item in s1 for item in s2] else True)
    # return False if False in [item in s1 for item in s2] else True


    # flag = True
    # for item in s2:
    #     if item in s1:
    #         s1 = s1.replace(item, '', 1)
    #     else:
    #         flag = False
    # print(flag)
    # return flag


    print(Counter(s2) - Counter(s1) == Counter())
    return Counter(s2) - Counter(s1) == Counter()

    # or:
    # return len(Counter(s2)- Counter(s1)) == 0
    

scramble()


# a = {
#     'a': 1,
#     'b': [2, True, 'f']
# }

# print(a.pop('a'), f'\n{a}')
# print(a.pop('a'))
# a.update([('a', 5), ('c', {2: 'fveve'})])
# print(a)