def main():
    ex1 = 1234567890123456
    ex2 = 1234567890123452

    res_1 = validateCard(ex1)
    res_2 = validateCard(ex2)

    print(res_1)
    print(res_2)


def validateCard(num_list):
    if len(str(num_list)) < 14 or 19 < len(str(num_list)):
        return False

    num_list = list(str(num_list))
    last_num = int(num_list.pop())
    num_list.reverse()
    
    temp_list = []
    for i in range(len(num_list)):
        if i % 2 == 0:
            doubled_num = int(num_list[i]) * 2
            while doubled_num > 9:
                amount_figure = 0
                for sign in str(doubled_num):
                    amount_figure += int(sign) 
                doubled_num = amount_figure
                
            temp_list.append(doubled_num)
        else:
            temp_list.append(int(num_list[i]))
    
    amount_str = str(sum(temp_list))
    difference = 10 - int(amount_str[-1])

    return difference == last_num


if __name__ == "__main__":
    main()
