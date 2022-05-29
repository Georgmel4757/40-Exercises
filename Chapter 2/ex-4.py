def main():
    ex1 = [16, 28]
    ex2 = [0,]
    ex3 = [1, 2, 3, 4, 5, 6]

    res_1 = sumDigProd(*ex1)
    res_2 = sumDigProd(*ex2)
    res_3 = sumDigProd(*ex3)

    print(res_1)
    print(res_2)
    print(res_3)


def sumDigProd(*args):
    amount = sum(args)
    product_figure = 0
    
    while amount > 9:
        product_figure = 1
        for sign in str(amount):
            product_figure *= int(sign) 
        amount = product_figure
    
    return product_figure


if __name__ == "__main__":
    main()
