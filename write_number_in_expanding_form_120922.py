# def expanded_form(num=4982342):
    # result_string = ''
    # length = len(str(num))
    # num_list = [int(item) for item in list(str(num))]
    # count = 0
    # for number in num_list:
    #     if number != 0:
    #         if count == 0:
    #             number  = number * (10 ** (length - 1))
    #             result_string += str(number)
    #         else:
    #             number  = number * (10 ** (length - 1))
    #             result_string += f" + {number}"
    #         length -= 1 
    #         count += 1
    #     elif number == 0:
    #         length -= 1 
    #         count += 1
    # # print(result_string)
    # return result_string

def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

expanded_form()