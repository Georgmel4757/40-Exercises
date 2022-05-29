def main():
    ex1 = 4
    ex2 = 9
    ex3 = 206

    res_1 = ulam(ex1)
    res_2 = ulam(ex2)
    res_3 = ulam(ex3)

    print(res_1)
    print(res_2)
    print(res_3)
 

def ulam(number):
    ulan_set = {1, 2}
    ulan_nums = [1, 2]

    if number < 1:
        return None 
    if number == 1:
        return 1
    elif number == 2:
        return 2

    i = 3
    while len(ulan_nums) != number:
        count = 0
        for j in range(0, len(ulan_nums)):
            if ((i - ulan_nums[j]) in ulan_set and 
                    ulan_nums[j] != (i - ulan_nums[j])):
                count += 1
            if count > 2:
                break

        if count == 2:
            ulan_nums.append(i)
            ulan_set.add(i)
        i += 1
    
    return ulan_nums[-1]


if __name__ == "__main__":
    main()
