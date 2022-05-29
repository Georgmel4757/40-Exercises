def main():
    ex_1 = 39
    ex_2 = 999
    ex_3 = 4

    res_1 = bugger(ex_1)
    res_2 = bugger(ex_2)
    res_3 = bugger(ex_3)

    print(res_1)
    print(res_2)
    print(res_3)


def bugger(number):
    product = 1
    persistence = 0

    while number > 9:
        for char in str(number):
            product *= int(char)
        persistence += 1
        number = product
        product = 1

    return persistence


if __name__ == "__main__":
    main()