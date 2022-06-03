def main():
    ex1 = (523, 76)
    ex2 = (9132, 5564)
    ex3 = (8732, 91255)

    res_1 = maxPossible(*ex1)
    res_2 = maxPossible(*ex2)
    res_3 = maxPossible(*ex3)

    print(res_1)
    print(res_2)
    print(res_3)
 

def maxPossible(num1, num2):
    if type(num1) != int or type(num2) != int:
        return None
        
    num1 = str(num1)
    num2 = str(num2)

    result = ""
    for sign_num1 in num1:
        if num2 and sign_num1 < max(num2):
            result += max(num2)
            num2 = num2.replace(max(num2), "", 1)
        else:
            result += sign_num1

    return result



if __name__ == "__main__":
    main()