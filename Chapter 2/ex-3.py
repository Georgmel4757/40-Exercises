def main():
    ex1 = ["butl", "beautiful"]
    ex2 = ["butlz", "beautiful"]
    ex3 = ["tulb", "beautiful"]
    ex4 = ["bbutl", "beautiful"]

    res_1 = canComplete(*ex1)
    res_2 = canComplete(*ex2)
    res_3 = canComplete(*ex3)
    res_4 = canComplete(*ex4)

    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)


def canComplete(signs, line):
    last_position = 0

    for letter in signs:
        position = line.find(letter)
        if position != -1 and position >= last_position:
            line = line.replace(letter, "", 1)
            last_position = position
        else:
            return False
        
    return True


if __name__ == "__main__":
    main()
