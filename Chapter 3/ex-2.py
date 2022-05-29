import re


def main():
    ex1 = "flag"
    ex2 = "Apple"
    ex3 = "button"
    ex4 = ""
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
    
    elif not word[0].isalpha():
        return None

    if word[0].lower() in vowels:
        return "{0}yay".format(word)

    elif word[0].lower() in consonants:
        temp = ""
        for i, sign in enumerate(word):
            if sign.lower() in vowels:
                if word[0].isupper():
                    temp = "{0}{1}{2}{3}ay".format(
                        word[i].upper(), word[i+1:], 
                        temp[0].lower(), temp[1:])
                else:
                    temp = "{0}{1}ay".format(word[i:], temp) 
                return temp
            else:
                temp += sign

        return temp


def translateSentence(line):
    if not line:
        return ""

    for word in re.findall(r"[A-Za-z]+", line):
        result = translateWord(word)
        line = line.replace(word, result, 1)
    
    return line

if __name__ == "__main__":
    main()