def main():
    ex1 = "jOn SnoW, kINg IN thE noRth."
    ex2 = "sansa stark, lady of winterfell."
    ex3 = "TYRION LANNISTER, HAND OF THE QUEEN."

    res_1 = correctTitle(ex1)
    res_2 = correctTitle(ex2)
    res_3 = correctTitle(ex3)

    print(res_1)
    print(res_2)
    print(res_3)


def correctTitle(line):
    result = ""
    exclusion = ["and", "the", "of", "in"]

    line = line.lower()

    if not line:
        return None

    temp = ""
    for sign in line:
        if sign == " " or sign == "-":
            if temp not in exclusion:
                result += "{0}{1}".format(temp.capitalize(), sign)
            else:
                result += "{0}{1}".format(temp, sign)
            temp = ""
        else:
            temp += sign

    if temp not in exclusion:
        result += "{0}".format(temp.capitalize())
    else:
        result += "{0}".format(temp)

    return result


if __name__ == "__main__":
    main()
