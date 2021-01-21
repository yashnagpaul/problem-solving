class Solution:

    def search(self, nums: List[int], target: int) -> int:

        arr = [nums]  # create a new array to halve each time

        while(len(arr) > 1):  # While array length > 1

            mid = (len(arr) / 2) if (len(arr) %
                                     2 == 0) else ((len(arr)+1) / 2)  # the mid index will be this

            if arr[mid] == target:  # Manually test this part

                return target

            elif target > arr[mid]:

                arr = arr[arr.index(mid): len(arr)]

            elif target < arr[mid]:

                arr = arr[0: arr.index(mid)]

        return -1
