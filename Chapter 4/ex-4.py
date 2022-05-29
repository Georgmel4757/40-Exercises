def main():
    print(longest_run([1, 2, 3, 5, 6, 7, 8, 9]))
    print(longest_run([1, 2, 3, 10, 11, 15]))
    print(longest_run([5, 4, 2, 1]))
    print(longest_run([3, 5, 7, 10, 15]))
 

def longest_run(nums):
    count = 1
    temp = 1
    is_down = False
    is_up = False

    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] == 1:
            if is_down:
                temp, is_down = 2, False
                continue
            is_up, is_down = True, False
            temp += 1
        elif nums[i+1] - nums[i] == -1:
            if is_up:
                temp, is_up = 2, False
                continue
            is_down, is_up= True, False
            temp += 1
        elif temp > count:
            count = temp
            temp = 1

    if temp > count:
        count = temp
        temp = 1
            
    return count


if __name__ == "__main__":
    main()