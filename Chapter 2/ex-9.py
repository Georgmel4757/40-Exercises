def main():
    ex1 = 1
    ex2 = 7
    ex3 = 19
    ex4 = 21

    res_1 = hexLattice(ex1)
    res_2 = hexLattice(ex2)
    res_3 = hexLattice(ex3)
    res_4 = hexLattice(ex4)

    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)


def hexLattice(number):
    count = 1
    product = 1
    while count < number:
        count += product * 6
        product += 1

    if count != number:
        return "Invalid"
    
    result = ""
    
    circles = product
    spaces = product
    sign = "o"
    for i in range(1, product * 2):
        if i < product:
            result += (f"{' '*spaces + f'{sign} '*circles}".rstrip()
                        + f"{' '*spaces}")
            circles += 1
            spaces -= 1
        else:
            result += (f"{' '*spaces + f'{sign} '*circles}".rstrip() 
                    + f"{' '*spaces}")
            circles -= 1
            spaces += 1

        result += "\n"
    
    result = result.rstrip("\n")

    return result


if __name__ == "__main__":
    main()
