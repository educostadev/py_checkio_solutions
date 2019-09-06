#!/usr/bin/env checkio --domain=py run house-password

# 
# END_DESC

import re
# https://py.checkio.org/en/mission/house-password/
# Input: A password as string with letters and digits
# Output: Is the password safe or not as boolean
# Conditions: A password is safe when:
# (1) lengh is greater than or equal to 10
# (2) has at leat one digit
# (3) has at least one uppercase letter
# (4) has at least one lowercase letter
def checkio(data: str) -> bool:
    # Check if data lenght is >= 10 and
    # Check if data has a digit and
    # Check if data has a uppercase And
    # Check if data has lower case
    # The password is strong then return true otherwise false.
    return len(data) >= 10 and re.search("[0-9]", data) != None and re.search("[a-z]", data) != None and re.search("[A-Z]", data) != None
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")