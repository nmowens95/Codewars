# Instructions:
'''
In this Kata, you will be given a string that has lowercase letters and numbers. 
Your task is to compare the number groupings and return the largest number. Numbers will not have leading zeros.

For example, solve("gh12cdy695m1") = 695, because this is the largest of all number groupings.
'''

# Answer:

def solve(s:str) -> int:
    current_number = ""
    max_number = None

    for char in s:
        if char.isdigit():
            current_number += char
        elif current_number:
            number = int(current_number)
            if max_number is None or number > max_number:
                max_number = number
            current_number = ""

    if current_number:
        number = int(current_number)
        if max_number is None or number > max_number:
            max_number = number

'''
Sample Tests:
import codewars_test as test
from solution import solve

@test.it("Basic tests")
def _():
    test.assert_equals(solve('gh12cdy695m1'),695)
    test.assert_equals(solve('2ti9iei7qhr5'),9)
    test.assert_equals(solve('vih61w8oohj5'),61)
    test.assert_equals(solve('f7g42g16hcu5'),42)
    test.assert_equals(solve('lu1j8qbbb85'),85)
'''