def count_smileys(arr=[':)', ';(', ';}', ':-D']):
    count_smileys = 0
    valid_smile_elements = [';', ':', '-', '~']
    if arr != []:
        for item in arr:
            if item[-1] == ')' or item[-1] == 'D':
                if len(item) == 3:
                    if item[1] == '-' or item[1] == '~':
                        if item[0] == ':' or item[0] == ';':
                            count_smileys += 1
                elif len(item) == 2:
                    if item[0] == ':' or item[0] == ';':
                        count_smileys += 1
    print(count_smileys)

    return count_smileys


count_smileys()