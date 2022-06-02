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
    
    sign = "o"
    hexagon = ""
    count_circles = product
    count_spaces = product

    for i in range(1, product * 2):
        spaces = " " * count_spaces
        circles = " ".join(sign * count_circles)
        hexagon += "{0}{1}{0}".format(spaces, circles)
        if i < product:
            count_circles += 1
            count_spaces -= 1
        else:
            count_circles -= 1
            count_spaces += 1

        hexagon += "\n"
    
    hexagon = hexagon.rstrip("\n")

    return hexagon


if __name__ == "__main__":
    main()
