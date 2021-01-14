class Solution:
    def search(self, nums: List[int], target: int) -> int:

        arr = nums

        while(True):
            mid = len(arr) if len(arr) % 2 == 0 else len(arr)+1
            if mid == target:
                return target
            elif target > mid:
                arr = arr[arr.index(mid):len(arr)-1]
            elif target < mid:
                arr = arr[0:arr.index(mid)]
