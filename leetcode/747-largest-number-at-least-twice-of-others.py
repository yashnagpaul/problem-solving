# In a given integer array nums, there is always exactly one largest element.

# Find whether the largest element in the array is
# at least twice as muchas every other number in the array.

# If it is, return the index of the largest element, otherwise return -1.

class Solution:
    def dominantIndex(self, nums) -> int:
        if len(nums) <= 1:
            return 0

        largestNum = max(nums)
        indexLargest = nums.index(largestNum)
        nums.pop(indexLargest)
        secondLargestNum = max(nums)
        if secondLargestNum*2 <= largestNum:
            return indexLargest
        else:
            return -1
