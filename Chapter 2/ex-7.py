def main():
    ex1 = 0
    ex2 = 18
    ex3 = 126
    ex4 = 909

    res_1 = numToEng(ex1)
    res_2 = numToEng(ex2)
    res_3 = numToEng(ex3)
    res_4 = numToEng(ex4)

    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)


def numToEng(number):
    zero_nine = {
        "1": "one", "2": "two", "3": "three", 
        "4": "four", "5": "five", "6": "six",
        "7": "seven", "8": "eight", "9": "nine",
        "0": "zero"}
    
    twenty_ninety = {
        "2": "twenty", "3": "thirty", 
        "4": "forty", "5": "fifty", "6": "sixty",
        "7": "seventy", "8": "eighty", "9": "ninety"}
    
    exclusion = {
        "10": "ten", "11": "eleven", "12": "twelve",
        "13": "thirteen", "15": "fifteen"}
        
    result = ""

    if type(number) != int or number < 0 or 999 < number:
        return None

    num_str = str(number)
    length_num = len(num_str)

    while len(num_str) != 0:
        if len(num_str) == 3:
            result += "{0} hundred ".format(zero_nine[num_str[0]])
            num_str = num_str[1:]
            
        elif len(num_str) == 2:
            first_sign = num_str[0]
            second_sign = num_str[1]
            
            if num_str in exclusion:
                result += "{0}".format(exclusion[num_str])
                num_str = ""
            elif first_sign == "0":
                num_str = second_sign
            elif first_sign == "1" and second_sign in "46789":
                if zero_nine[second_sign][-1] != "t":
                    result += "{0}teen".format(zero_nine[second_sign])
                else:
                    result += "{0}een".format(zero_nine[second_sign])
                num_str = ""
            else:
                result += "{0} ".format(twenty_ninety[first_sign])
                num_str = second_sign

        elif len(num_str) == 1:
            if num_str != "0":
                result += "{0}".format(zero_nine[num_str])
            elif length_num == 1 and num_str == "0":
                result = "zero"
            num_str = ""

    return result.strip()


if __name__ == "__main__":
    main()
