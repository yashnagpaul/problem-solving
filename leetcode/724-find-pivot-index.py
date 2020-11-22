# Given an array of integers nums,
# write a method that returns the "pivot" index of this array.

# We define the pivot index as the index where
# the sum of all the numbers to the left of the index is equal to
# the sum of all the numbers to the right of the index.

# If no such index exists, we should return -1.
# If there are multiple pivot indexes, you should return the left-most pivot index.

class Solution:
    def pivotIndex(self, nums):

        totalSum = sum(nums)
        runningSum = 0

        for i in range(0, len(nums)):
            if i > 0:
                runningSum = runningSum + nums[i-1]
            else:
                runningSum = 0

            remainingSum = totalSum - (runningSum + nums[i])

            if runningSum == remainingSum:
                return i

        return -1


object_A = Solution()
print(object_A.pivotIndex([1, 2, 3, 1, 1, 1]))
