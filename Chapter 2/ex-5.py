def main():
    ex1 = ["toe", "ocelot", "maniac"]
    ex2 = ["many", "carriage", "emit", "apricot", "animal"]
    ex3 = ["hoops", "chuff", "bot", "bottom"]

    res_1 = sameVowelGroup(ex1)
    res_2 = sameVowelGroup(ex2)
    res_3 = sameVowelGroup(ex3)

    print(res_1)
    print(res_2)
    print(res_3)


def sameVowelGroup(words):
    result = []
    vowels = "aeiouy"

    if not words:
        return result
    
    first_word = words[0]
    result.append(first_word)
    vow_first = {sign for sign in first_word if sign in vowels}

    for index in range(1, len(words)):
        vow_next = {sign for sign in words[index] if sign in vowels}
        if vow_first == vow_next:
            result.append(words[index])

    return result


if __name__ == "__main__":
    main()
