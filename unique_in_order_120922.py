# import collections

# def unique_in_order(iterable='AAAABBBCcDAABBB'):
#     print([i for i, j in collections.Counter(iterable).items()])
#     return [i for i, j in collections.Counter(iterable).items()]


def unique_in_order(iterable='AAAABBBCcDAABBB'):
    list = []
    if iterable == '' or iterable == []:
        return []
    else:
        list.append(iterable[0])
        for item in range(1, len(iterable)):
            if iterable[item] != list[-1]:
                list.append(iterable[item])
        # print(list)
        return list


unique_in_order()