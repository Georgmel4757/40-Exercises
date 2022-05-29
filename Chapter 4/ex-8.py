from fractions import Fraction


def main():
    print(fractions("0.(6)"))
    print(fractions("1.(1)"))
    print(fractions("3.(142857)"))
    print(fractions("0.19(2367)"))
    print(fractions("0.1097(3)"))
 

def fractions(num):
    integer, real = num.strip().split(".")
    is_period = False
    left_num = ""
    period = "" 

    for sign in real:
        if sign.isdigit() and not is_period:
            left_num += sign
        elif sign.isdigit() and is_period:
            period += sign
        elif sign == "(":
            is_period = True
        elif sign == ")":
            is_period = False
            break
    
    if left_num:
        numerator = int(left_num+period) - int(left_num)
        denominator = int("9"*len(period)) * 10**len(left_num)
        dec = int(integer) + Fraction(numerator, denominator)
    else:
        numerator = int(period)
        denominator = int("9"*len(period))
        dec = int(integer) + Fraction(numerator, denominator)

    result = "{0}/{1}".format(dec.numerator, dec.denominator)
    
    return result


if __name__ == "__main__":
    main()