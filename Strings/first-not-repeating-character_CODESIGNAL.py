def firstNotRepeatingCharacter(s):

    # initiate 2 empty lists
    # first one stores the unique values we've seen so far
    # second keeps track of the values that have been repeated

    unique_so_far = list()
    repeated_already = list()

    # loop through the argument string and add the current value to the appropriate list
    for i in range(len(s)):
        if (s[i] not in unique_so_far) and (s[i] not in repeated_already):
            unique_so_far.append(s[i])
        elif (s[i] not in unique_so_far) and (s[i] in repeated_already):
            continue
        elif (s[i] in unique_so_far) and (s[i] not in repeated_already):
            unique_so_far.remove(s[i])
            repeated_already.append(s[i])

    # return the first value [0 index] from the list of unique values
    return unique_so_far[0] if len(unique_so_far) > 0 else "_"


if __name__ == "__main__":
    assert firstNotRepeatingCharacter("abacabad") == 'c', "Should be 'c'"
