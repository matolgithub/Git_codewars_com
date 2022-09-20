def rgb(r=1, g=2, b=3):
    hex_result = ''
    rgb_list = [r, g, b]
    hex_conv_list = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    for item in rgb_list:
        if int(item) < 0:
            hex_result += '00'
        elif int(item) > 255:
            hex_result += 'FF'
        else:
            first = int(int(item) / 16)
            second = int(item) % 16
            hex_result += hex_conv_list[first]
            hex_result += hex_conv_list[second]

    print(hex_result)
    
    return hex_result


rgb()