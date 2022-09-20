def land_perimeter(arr=[
    'XOOXO',
    'XOOXO', 
    'OOOXO', 
    'XXOXO', 
    'OXOOO']):
    res_perimeter = sum([item.count('X') for item in arr]) * 4
    for i, j in enumerate(arr):
        for k in range(len(j)):
            if k == 0 and j[k] == 'X':
                if j[k + 1] == 'X':
                    res_perimeter -= 2
            elif k == len(j) and j[k] == 'X':
                if j[k - 1] == 'X':
                    res_perimeter -= 2
            elif k in range(2, len(j) - 2):
                if j[k] == 'X':
                    if j[k - 1] == 'X' and j[k + 1] == 'X':
                        res_perimeter -= 4
                    elif j[k - 1] == 'X' or j[k + 1] == 'X':
                        res_perimeter -= 2
            for m in range(len(arr)):
                if m == 1 and arr[m][k] == 'X':
                    if arr[m - 1] == 'X' and arr[m + 1] == 'X':
                        res_perimeter -= 4
                    elif  arr[m - 1] == 'X' or arr[m + 1] == 'X':
                        res_perimeter -= 2
                elif m == len(arr) - 1 and arr[m][k] == 'X':
                    if arr[m-1][k] == 'X':
                        res_perimeter -= 2
                elif m in range(2, len(arr) - 2):
                    if arr[m - 1] == 'X' and arr[m + 1] == 'X':
                        res_perimeter -= 4
                    elif  arr[m - 1] == 'X' or arr[m + 1] == 'X':
                        res_perimeter -= 2


    print(res_perimeter)
    return res_perimeter


    # output = [list(row) for row in arr]
    # p_dict = {5:0, 4:1, 3:2, 2:3, 1:4}
    # perimeter = 0
    # for i,row in enumerate(arr):
    #     for j,char in enumerate(row):
    #         if arr[i][j] == 'X':
    #             count = 1
    #             if (j-1) >= 0 and arr[i][j-1] == 'X':
    #                 count += 1
    #             if (j+1) < len(row) and arr[i][j+1] == 'X':
    #                 count += 1
    #             if (i-1) >= 0 and arr[i-1][j] == 'X':
    #                 count += 1
    #             if (i+1) < len(arr) and arr[i+1][j] == 'X':
    #                 count += 1
    #             output[i][j] = [count]
    #             perimeter += p_dict[count]
    #         else:
    #             output[i][j] = [0]
    # return "Total land perimeter: {}".format(perimeter)

land_perimeter()
