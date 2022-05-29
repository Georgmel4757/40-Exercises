def main():
    ex1 = ("ABAB", "CDCD") 
    ex2 = ("ABCBA", "BCDCB")
    ex3 = ("FFGG", "CDCD")
    ex4 = ("FFFF", "ABCD") 

    res_1 = sameLetterPattern(*ex1)
    res_2 = sameLetterPattern(*ex2)
    res_3 = sameLetterPattern(*ex3)
    res_4 = sameLetterPattern(*ex4)

    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)
 

def sameLetterPattern(line1, line2):
    pattern = {}

    if len(line1) != len(line2):
        return False

    for index in range(len(line1)):
        sign1 = line1[index]
        sign2 = line2[index]

        if sign1 in pattern.keys() and sign2 != pattern[sign1]:
            return False
        else:
            pattern[sign1] = sign2
        
    return True


if __name__ == "__main__":
    main()