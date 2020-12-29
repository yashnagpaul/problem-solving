# Define a function plusMinus, which will recieve an array of integers:
# Print the ratios of positive, negative and zero values in the array.
# Each value should be printed on a separate line with 6 digits after the decimal.
# The function should not return a value.

def plusMinus(arr):
    pos = []
    neg = []
    zero = []
    for i in range(0, len(arr)):
        if arr[i] > 0:
            pos.append(arr[i])
        elif arr[i] == 0:
            zero.append(arr[i])
        elif arr[i] < 0:
            neg.append(arr[i])
    print(round(len(pos)/len(arr), 6))
    print(round(len(neg)/len(arr), 6))
    print(round(len(zero)/len(arr), 6))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
