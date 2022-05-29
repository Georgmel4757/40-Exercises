def main():
    ex1 = "6 * 4 = 24"
    ex2 = "18 / 17 = 2"
    ex3 = "16 * 10 = 160 = 14 + 120"

    res_1 = formula(ex1)
    res_2 = formula(ex2)
    res_3 = formula(ex3)

    print(res_1)
    print(res_2)
    print(res_3)
 

def formula(line):
    signs = line.split("=")

    if not line.strip() or not signs:
        return None

    results = [eval(sign) for sign in signs]
    for index in range(len(results)-1):
        if results[index] != results[index+1]:
            return False

    return True



if __name__ == "__main__":
    main()