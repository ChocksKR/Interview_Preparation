#brute force

def twoSumBruteForce(nums, target):
    for i in range(0,len(nums)):
        for j in range (0,i):
            if nums[i]+nums[j] == target:
                return [i, j]

def twoSumOptimized(nums, target):
    dictionary = {}
    for i in range(0,len(nums)):
        dictionary[nums[i]] = i


    for i in range(0,len(nums)):
        second_num = target - nums[i]
        if second_num in dictionary:
            return [i,dictionary.get(second_num)]

print(twoSumOptimized([2, 7, 11, 15], 9))


