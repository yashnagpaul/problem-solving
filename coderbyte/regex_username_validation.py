# A function that takes a string parameter,
# determine if the string is a valid username according to the following rules:

# 1. The username is between 4 and 25 characters.
# 2. It must start with a letter.
# 3. It can only contain letters, numbers, and the underscore character.
# 4. It cannot end with an underscore character.

import re


def CodelandUsernameValidation(strParam):
    return "true" if len(strParam) <= 25 and len(strParam) >= 4 and bool(re.match('\w', strParam)) and bool(re.match('\D', strParam)) and bool(re.match("\w", strParam)) and strParam[len(strParam)-1] != "_" else "false"


# keep this function call here
print(CodelandUsernameValidation(input()))
