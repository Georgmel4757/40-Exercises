def main():
    ex_1 = ["Sam I am!", "Green eggs and ham."]
    ex_2 = ["Sam I am!", "Green eggs and HAM."]
    ex_3 = ["You are off to the races", "a splendid day."]
    ex_4 = ["and frequently do?", "you gotta move."]

    res_1 = doesRhyme(*ex_1)
    res_2 = doesRhyme(*ex_2)
    res_3 = doesRhyme(*ex_3)
    res_4 = doesRhyme(*ex_4)

    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)


def doesRhyme(line1, line2):
    vowels = "aeiouy"

    last_word1 = line1.split()[-1]
    last_word2 = line2.split()[-1]

    vowels_set1 = {sign.lower() for sign in last_word1 if sign.lower() in vowels}
    vowels_set2 = {sign.lower() for sign in last_word2 if sign.lower() in vowels}

    return (vowels_set1 == vowels_set2)


if __name__ == "__main__":
    main()