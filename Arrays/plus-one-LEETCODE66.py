# Given a non-empty array of decimal digits
# representing a non-negative integer,
# increment one to the integer.

# The digits are stored such that the most significant digit
# is at the head of the list,
# and each element in the array contains a single digit.

# You may assume the integer does not contain
# any leading zero, except the number 0 itself.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

class Solution:
    def plusOne(self, digits):
        # map through the array,
        # convert digits into strings in order to join all the characters, and
        # combine all elements into a single string
        stringify = ''.join(list(map(str, digits)))

        # now, convert that result into an integer
        numerified = int(stringify)

        # add one
        numerified = numerified + 1

        # convert the answer back into a string
        stringified = str(numerified)

        # finally, to make sure the answer's length == the length of the original parameter
        # add leading zeroes to our final answer if needed
        # loop through that string and convert each character into an integer,
        # and place them in an array
        return [int(char) for char in stringified.zfill(len(digits))]
