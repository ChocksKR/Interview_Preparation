# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#     [-1, 0, 1],
#     [-1, -1, 2]
# ]

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        i=0
        result = set()
        while nums[i] < 0:
            for j in range(i+1,len(nums)):
                for k in range (j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.add(tuple([nums[i],nums[j],nums[k]]))
            i = i+1
        return result

def findTriplets(arr):

    found = False

    # sort array elements
    arr.sort()

    for i in range(len(arr)):

        # initialize left and right
        l = i + 1
        r = len(arr) - 1
        x = arr[i]
        while (l < r):

            if (x + arr[l] + arr[r] == 0):
                # print elements if it's sum is zero
                print(x, arr[l], arr[r])
                l+=1
                r-=1
                found = True


            # If sum of three elements is less
            # than zero then increment in left
            elif (x + arr[l] + arr[r] < 0):
                l+=1

            # if sum is greater than zero than
            # decrement in right side
            else:
                r-=1

    if (found == False):
        print(" No Triplet Found")

sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))

findTriplets([-1, 0, 1, 2, -1, -4])