import re


def main():
    ex1 = "How the Avocado Became the Fruit of the Global Trade"
    ex2 = "Why You Will Probably Pay More for Your Christmas Tree This Year"
    ex3 = "Hey Parents, Surprise, Fruit Juice Is Not Fruit"
    ex4 = "Visualizing Science"

    res_1 = getHashTags(ex1)
    res_2 = getHashTags(ex2)
    res_3 = getHashTags(ex3)
    res_4 = getHashTags(ex4)

    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)


def getHashTags(line):
    max_words = []

    for fragment in re.findall(r"[A-Za-z]+", line):
        fragment = fragment.lower()
        if not len(max_words):
            max_words.append(fragment)
            continue
        for i, word in enumerate(max_words):
            if len(fragment) > len(word):
                max_words.insert(i, fragment)
                break
        if len(max_words) < 3 and fragment not in max_words:
            max_words.append(fragment)
        elif len(max_words) == 4:
            max_words.pop()

    max_words = [f"#{word}" for word in max_words]
                
    return max_words
        

if __name__ == "__main__":
    main()