def main():
    ex1 = "Hello"
    ex2 = [72, 33, -73, 84, -12, -3, 13, -13, -68]
    ex3 = "Sunshine"

    res_1 = encrypt(ex1)
    res_2 = decrypt(ex2)
    res_3 = encrypt(ex3)

    print(res_1)
    print(res_2)
    print(res_3)


def encrypt(line):
    codes_list = []

    if line:
        codes_list.append(ord(line[0]))
        for index in range(1, len(line)):
            codes_list.append(ord(line[index]) - ord(line[index-1]))
    
    return codes_list


def decrypt(codes_list):
    line = ""
    
    if codes_list:
        line += chr(codes_list[0])
        last_num = codes_list[0]

        for index in range(1, len(codes_list)):
            char_number = chr(last_num + codes_list[index]) 
            line += char_number
            last_num = ord(char_number)

    return line


if __name__ == "__main__":
    main()
