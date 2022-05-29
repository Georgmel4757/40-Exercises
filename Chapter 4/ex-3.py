def main():
    print(digitsCount(4666))
    print(digitsCount(544))
    print(digitsCount(121317))
    print(digitsCount(0))
    print(digitsCount(12345))
    print(digitsCount(1289396387328))
 

def digitsCount(num):
    if num // 10 == 0:
        return 1
    else:
        return 1 + digitsCount(num//10) 
    

if __name__ == "__main__":
    main()