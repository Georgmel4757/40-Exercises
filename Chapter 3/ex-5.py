def main():
    ex1 = "abcabcbb"
    ex2 = "aaaaaa"
    ex3 = "abcde"
    ex4 = "abcda"

    res_1 = longestNonrepeatingSubstring(ex1)
    res_2 = longestNonrepeatingSubstring(ex2)
    res_3 = longestNonrepeatingSubstring(ex3)
    res_4 = longestNonrepeatingSubstring(ex4)

    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)
 

def longestNonrepeatingSubstring(line):
    unique_signs = set()
    temp_line = ""
    result = ""
    line = line.strip()
    
    if not line:
        return None

    for sign in line:
        if sign not in unique_signs:
            unique_signs.add(sign)
            temp_line += sign
        else:
            if len(temp_line) > len(result):
                result = temp_line
            unique_signs.clear()
            temp_line = ""

    if len(temp_line) > len(result):
        result = temp_line

    return result


if __name__ == "__main__":
    main()