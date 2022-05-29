def main():
    ex1 = 2
    ex2 = 12
    ex3 = 16

    res_1 = convertToRoman(ex1)
    res_2 = convertToRoman(ex2)
    res_3 = convertToRoman(ex3)

    print(res_1)
    print(res_2)
    print(res_3)
 

def convertToRoman(number):
    result = ''
    arabic_to_roman = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    for arabic, roman in arabic_to_roman.items():
        result += number // arabic * roman
        number %= arabic

    return result


if __name__ == "__main__":
    main()