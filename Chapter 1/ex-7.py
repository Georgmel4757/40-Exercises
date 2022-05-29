def main():
    ex_1 = "abbccc"
    ex_2 = "77777geff"
    ex_3 = "abc" 
    ex_4 = "" 

    res_1 = toStarShorthand(ex_1)
    res_2 = toStarShorthand(ex_2)
    res_3 = toStarShorthand(ex_3)
    res_4 = toStarShorthand(ex_4)

    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)


def toStarShorthand(line):
    last_sign = ''
    count = 1
    result = ''

    for sign in line:
        if sign == last_sign:
            count += 1
        elif count == 1:
            result += last_sign
            count = 1
        else:
            result += '{0}*{1}'.format(last_sign, count)
            count = 1
        
        last_sign = sign
    
    if count == 1:
        result += last_sign
    else:
        result += '{0}*{1}'.format(last_sign, count)
    
    return result


if __name__ == "__main__":
    main()