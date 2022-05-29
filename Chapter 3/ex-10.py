def main():
    ex1 = "Tesh3 th5e 1I lov2e way6 she7 j4ust i8s."
    ex2 = "the4 t3o man5 Happ1iest of6 no7 birt2hday steel8!"
    ex3 = "is2 Thi1s T4est 3a"
    ex4 = "4of Fo1r pe6ople g3ood th5e the2"
    ex5 = " "

    res_1 = rearrange(ex1)
    res_2 = rearrange(ex2)
    res_3 = rearrange(ex3)
    res_4 = rearrange(ex4)
    res_5 = rearrange(ex5)

    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)
    print(res_5)
 

def rearrange(line):
    words = {}
    result = ""

    if not line:
        return None
    
    for fragment in line.split():
        index = ""
        word = ""
        for sign in fragment:
            if sign.isdigit():
                index += sign
            else:
                word += sign
        if index:
            words[int(index)] = word

    for i in range(1, len(words)+1):
        result += "{0} ".format(words[i])

    return result.rstrip()


if __name__ == "__main__":
    main()