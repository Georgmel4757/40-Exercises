def main():
    ex_1 = ["AZYWABBCATTTA", 'A']
    ex_2 = ["$AA$BBCATT$C$$B$", '$']
    ex_3 = ["ZZABCDEF", 'Z']

    res_1 = countUniqueBooks(*ex_1)
    res_2 = countUniqueBooks(*ex_2)
    res_3 = countUniqueBooks(*ex_3)

    print(res_1)
    print(res_2)
    print(res_3)


def countUniqueBooks(line, unique_sign):
    flag = False
    unique_signs = set()

    if line.count(unique_sign) % 2 != 0:
        return -1

    for sign in line:
        if sign == unique_sign:
            flag = not(flag)
        elif flag:
            unique_signs.add(sign)
    
    return len(unique_signs)


if __name__ == "__main__":
    main()