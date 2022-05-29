def main():
    print(generateNonconsecutive(1))
    print(generateNonconsecutive(2))
    print(generateNonconsecutive(3))
    print(generateNonconsecutive(4))
 
def generateNonconsecutive(num):
    numbers = []
    max_int = 2 ** num

    for i in range(max_int):
        temp_num = format(i, "b").zfill(num)
        if temp_num.find("11") != -1:
            continue
        else:
            numbers.append(temp_num)
    
    return " ".join(numbers)


if __name__ == "__main__":
    main()