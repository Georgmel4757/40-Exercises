def main():
    ex_1 = [451999277, 41177722899]
    ex_2 = [1222345, 12345]
    ex_3 = [666789, 12345667]
    ex_4 = [33789, 12345337]

    res_1 = trouble(*ex_1)
    res_2 = trouble(*ex_2)
    res_3 = trouble(*ex_3)
    res_4 = trouble(*ex_4)

    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)


def trouble(num1, num2):
    if type(num1) != int or type(num2) != int:
        return False
        
    num1 = str(num1)
    num2 = str(num2)

    unique_sign1 = set(num1)
    for sign in unique_sign1:
        if num1.count(sign) == 3 and num2.count(sign) == 2:
            return True

    return False


if __name__ == "__main__":
    main()