def main():
    ex1 = 3
    ex2 = 30
    ex3 = 321
    ex4 = 123

    res_1 = isNew(ex1)
    res_2 = isNew(ex2)
    res_3 = isNew(ex3)
    res_4 = isNew(ex4)

    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)


def isNew(number):
    if number < 0:
        return None

    signs = [sign for sign in str(number) if sign != "0"]
    zeros = [sign for sign in str(number) if sign == "0"]
    signs.sort()

    for zero in zeros:
        signs.insert(1, zero)
    
    min_num = int("".join(signs))

    return min_num >= number


if __name__ == "__main__":
    main()
