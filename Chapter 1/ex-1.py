def main():
    n = 10
    k = 7
    line = "hello my name is Bessie and this is my essay"
    esse = get_esse(n, k, line)
    print(esse)


def get_esse(n, k, line):
    count_sign = 0
    result = ""

    for word in line.split():
        if count_sign + len(word) <= k:
            result += "{} ".format(word)
            count_sign += len(word)

        elif len(word) <= k:
            result = "{}\n{} ".format(result.rstrip(), word)
            count_sign = len(word)
    
    return result.strip()
        

if __name__ == "__main__":
    main()
