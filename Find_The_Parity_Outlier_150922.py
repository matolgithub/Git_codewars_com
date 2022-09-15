def find_outlier(integers=[160, 3, 1719, 19, 11, 13, -21]):
    if len([item for item in integers if item % 2 != 0]) == 1:
        result = [item for item in integers if item % 2 != 0][0]
    elif len([item for item in integers if item % 2 != 1]) == 1:
        result = [item for item in integers if item % 2 != 1][0]
    print(result)
    return result


find_outlier()
