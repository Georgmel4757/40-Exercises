def main():
    ex_1 = "hello_edabit"
    ex_2 = "helloEdabit"
    ex_3 = "is_modal_open"
    ex_4 = "getColor"

    res_1 = toCamelCase(ex_1)
    res_2 = toSnakeCase(ex_2)
    res_3 = toCamelCase(ex_3)
    res_4 = toSnakeCase(ex_4)

    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)


def toCamelCase(line):
    flag = False
    result = ""

    for sign in line:
        if flag:
            result += sign.upper()
            flag = False
        elif sign == "_":
            flag = True
        else:
            result += sign

    return result
        

def toSnakeCase(line):
    result = ""

    for sign in line:
        if sign.isupper():
            result += "_{}".format(sign.lower())
        else:
            result += sign

    return result


if __name__ == "__main__":
    main()
