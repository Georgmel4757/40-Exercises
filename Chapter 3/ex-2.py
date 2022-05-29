import re


def main():
    ex1 = "flag"
    ex2 = "Apple"
    ex3 = "button"
    ex4 = "     "
    ex5 = "I like to eat honey waffles."
    ex6 = "Do you think it is going to rain today?"

    res_1 = translateWord(ex1)
    res_2 = translateWord(ex2)
    res_3 = translateWord(ex3)
    res_4 = translateSentence(ex4)
    res_5 = translateSentence(ex5)
    res_6 = translateSentence(ex6)

    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)
    print(res_5)
    print(res_6)


def translateWord(word):
    vowels = "aeiouy"
    consonants = "qwrtpsdfghjklzxcvbnm"
    word = word.strip()

    if not word:
        return ""
    
    if not word[0].isalpha():
        return None

    if word[0].lower() in vowels:
        return "{0}yay".format(word)

    elif word[0].lower() in consonants:
        temp_word = ""
        for i, sign in enumerate(word):
            if sign.lower() in vowels:
                if word[0].isupper():
                    return "{0}{1}{2}{3}ay".format(
                        word[i].upper(), word[i+1:], 
                        temp_word[0].lower(), temp_word[1:])
                else:
                    return "{0}{1}ay".format(word[i:], temp_word)
            else:
                temp_word += sign

        temp_word = "{0}ay".format(word)

        return temp_word


def translateSentence(line):
    result = ""

    if not line.strip():
        return ""

    for fragment in line.split():
        for word in re.findall(r"[A-Za-z]+", fragment):
            temp_word = translateWord(word)
            fragment = fragment.replace(word, temp_word, 1)
        result += "{0} ".format(fragment)
    
    return result.rstrip()

if __name__ == "__main__":
    main()