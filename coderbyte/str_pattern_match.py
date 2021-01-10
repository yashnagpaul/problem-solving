# Have the function QuestionsMarks(str) take the str string parameter,
# which will contain single digit numbers, letters, and question marks,
# and check if there are exactly 3 question marks between every pair of two numbers that add up to 10.
# If so, then your program should return the string true,
# otherwise it should return the string false.
# If there aren't any two numbers that add up to 10 in the string,
# then your program should return false as well.

def QuestionsMarks(strParam):
    true = False
    countQ = 0
    previousDigit = 0
    for i in strParam:
        if type(i) == int:
            if i + previousDigit == 10 and countQ == 3:
                true = True
            previousDigit = int(i)
        elif i == '?':
            countQ += 1

    return 'true' if true else 'false'


# keep this function call here
print(QuestionsMarks(input()))
