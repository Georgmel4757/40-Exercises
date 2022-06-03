from fractions import Fraction
import re


def main():
    print(fractions("0.(6)"))
    print(fractions("1.(1)"))
    print(fractions("3.(142857)"))
    print(fractions("0.19(2367)"))
    print(fractions("0.1097(3)"))
 

def fractions(number):
    if not isinstance(number, str):
        return None
    if not re.fullmatch(r"\d+\.\d*\(\d+\)", number.strip()):
        return None

    integer, real = number.strip().split(".")
    period = re.findall(r"\(\d+\)", real)[0][1:-1]
    mixed_part = re.findall(r"\d*\(", real)[0][:-1]
    
    if mixed_part:
        numerator = int(mixed_part + period) - int(mixed_part)
        denominator = int("9" * len(period)) * 10 ** len(mixed_part)
        dec = int(integer) + Fraction(numerator, denominator)
    else:
        numerator = int(period)
        denominator = int("9" * len(period))
        dec = int(integer) + Fraction(numerator, denominator)

    result = "{0}/{1}".format(dec.numerator, dec.denominator)
    
    return result


if __name__ == "__main__":
    main()