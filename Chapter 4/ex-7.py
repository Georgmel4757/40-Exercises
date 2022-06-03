def main():
    print(isExact(6))
    print(isExact(24))
    print(isExact(125))
    print(isExact(720))
    print(isExact(1024))
    print(isExact(40320))
 

def isExact(num, index=1, factorial=1):
    factorial *= index
    num1 = num/index
    if num1 == 1:
        return [factorial, index]
    if num1 < 1:
        return []
    index += 1
    return isExact(num1, index, factorial)


if __name__ == "__main__":
    main()