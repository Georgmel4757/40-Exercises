def main():
    ex_1 = "()()()"
    ex_2 = "((()))"
    ex_3 = "((()))(())()()(()())"
    ex_4 = "((())())(()(()()))"

    res_1 = split(ex_1)
    res_2 = split(ex_2)
    res_3 = split(ex_3)
    res_4 = split(ex_4)

    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)


def split(line):
    count_first = 0
    count_last = 0
    sign_line = ""
    result = []

    for sign in line:
        if sign == "(":
            count_first += 1
            sign_line += sign 
        elif sign == ")":
            count_last += 1
            sign_line += sign 
        
        if count_first and count_last and count_first == count_last:
            result.append(sign_line)
            count_first = 0
            count_last = 0
            sign_line = ""

    return result


if __name__ == "__main__":
    main()
