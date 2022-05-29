def main():
    print(sumsUp([1, 2, 3, 4, 5]))
    print(sumsUp([1, 2, 3, 7, 9]))
    print(sumsUp([10, 9, 7, 2, 8]))
    print(sumsUp([1, 6, 5, 4, 8, 2, 3, 7]))


def sumsUp(nums):
    result=[]

    if not nums:
        return None

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] == nums[j]:
                continue
            if (nums[i] + nums[j] == 8 and 
                    sorted([nums[i], nums[j]]) not in result):
                result.append(sorted([nums[i], nums[j]]))

    return result
    

if __name__ == "__main__":
    main()