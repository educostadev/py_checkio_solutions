#!/usr/bin/env checkio  --domain=py run absolute-sorting

# Let's try some sorting. Here is an array with the specific rules.
# 
# The array        (a tuple)        has various numbers. You should sort it, but sort it by absolute value in ascending order.    For example, the sequence (-20, -5, 10, 15) will be sorted like so: (-5, 10, 15, -20).    Your function should return the sorted list  or tuple.
# 
# Precondition:The numbers in the array are unique by their absolute values.
# 
# Input:An array of numbers , a tuple..
# 
# Output:The list or tuple (but not a generator) sorted by absolute values in ascending order.
# 
# Addition:The results of your function will be shown as a list in the tests explanation panel.
# 
# Precondition:    len(set(abs(x) for x in array)) == len(array)
# 0 < len(array) < 100
# all(isinstance(x, int) for x in array)
# all(-100 < x < 100 for x in array)
# 
# 
# 
# END_DESC

def checkio(numbers_array: tuple) -> list:
    return numbers_array

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(list(checkio((-20, -5, 10, 15))))

    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")