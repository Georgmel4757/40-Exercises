def main():
    print(takeDownAverage(["95%", "83%", "90%", "87%", "88%", "93%"]))
    print(takeDownAverage(["10%"]))
    print(takeDownAverage(["53%", "79%"]))
 

def takeDownAverage(nums):
    nums = [int(num[:-1]) for num in nums]
    average = sum(nums)/len(nums)
    result = (len(nums)+1) * (average - 5) - sum(nums)
    
    return "{0}%".format(round(result))
    

if __name__ == "__main__":
    main()