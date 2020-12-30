# Write a function that, given a positive integer N,
# returns the length of its longest binary gap.
# The function should return 0 if N doesn't contain a binary gap.

import re


class Solution:
    def binaryGap(self, n: int) -> int:

        # binary = str(bin(n))[2:] if (str(bin(n))[1] != "\d") else bin(n)

        binary = bin(n)  # 110 -> 1
        zero_count = 0
        one_count = 0
        biggest_gap = 0

        for digit in binary:

            if (digit == '0'):
                zero_count += 1
            else:
                one_count += 1
                if biggest_gap < zero_count:
                    biggest_gap = zero_count+1
                zero_count = 0  # reset zero count
                # now see if we have 2 consecutive non-zero values
                if (one_count > 1) and (biggest_gap < one_count):
                    biggest_gap = 1
                # if we've found 2 consecutive ones, reset one count
                one_count = 0 if one_count > 1 else one_count

        return biggest_gap
