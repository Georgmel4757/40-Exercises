def main():
    print(twoProduct([1, 2, 3, 9, 4, 5, 15, 3], 45))
    print(twoProduct([1, 2, 3, 9, 4, 15, 3, 5], 45))
    print(twoProduct([1, 2, -1, 4, 5, 6, 10, 7], 20))
    print(twoProduct([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    print(twoProduct([100, 12, 4, 1, 2], 15))
 

def twoProduct(nums, product):
    min_diff = len(nums)
    unique_couple = []
    result = []

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i == j:
                continue
            elif min_diff == 0:
                return result
            if (j - i < min_diff and nums[i] * nums[j] == product and             
                    sorted([nums[i], nums[j]]) not in unique_couple):  
                result = [nums[i], nums[j]]
                unique_couple.append(sorted([nums[i], nums[j]]))
                min_diff = j - i
    
    return result


if __name__ == "__main__":
    main()