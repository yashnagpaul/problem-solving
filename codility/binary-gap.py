# Write a function that, given a positive integer N,
# returns the length of its longest binary gap.
# The function should return 0 if N doesn't contain a binary gap.

def solution(n: int):
    binary = bin(n)
    zero_count = 0
    biggest_gap = 0
    for digit in binary:
        if digit == 0:
            1
    return(binary)


solution(1234)
