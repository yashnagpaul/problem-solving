# Have the function QuestionsMarks(str) take the str string parameter,
# which will contain single digit numbers, letters, and question marks,
# and check if there are exactly 3 question marks between every pair of two numbers that add up to 10.
# If so, then your program should return the string true,
# otherwise it should return the string false.
# If there aren't any two numbers that add up to 10 in the string,
# then your program should return false as well.

def QuestionsMarks(strParam):

    numbers = []
    true = 0
    q_marks = 0

    for i in range(len(strParam)):
        if strParam[i] == '?':
            q_marks += 1
        elif type(strParam[i]) == int:
            for i in range(len(numbers)):
                if numbers[i] + strParam[i] == 10:

                    x = numbers[strParam[i]]
                    y = strParam[i]

                    for i in range(x, y):
                        if strParam[i] == '?':
                            q_marks += 1
                    if q_marks == 3:
                        true += 1
                    else:
                        return False

                elif numbers[i] + strParam[i] == 10 and q_marks != 3:
                    return False
            numbers[strParam[i]] = i

    return True if true > 0 else False


# keep this function call here
print(QuestionsMarks(input()))
