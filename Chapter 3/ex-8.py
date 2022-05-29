def main():
    ex1 = 11211230
    ex2 = 13001120
    ex3 = 23336014
    ex4 = 11

    res_1 = palindromedescendant(ex1)
    res_2 = palindromedescendant(ex2)
    res_3 = palindromedescendant(ex3)
    res_4 = palindromedescendant(ex4)

    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)
 

def palindromedescendant(number):
    number = str(number)
    while len(number) > 1:
        if number == number[::-1]:
            return True
        temp = ""
        for i in range(0, len(number), 2):
            temp += str(int(number[i]) + int(number[i+1]))
        number = temp
    
    return False
        

if __name__ == "__main__":
    main()