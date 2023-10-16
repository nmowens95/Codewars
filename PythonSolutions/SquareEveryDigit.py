# Title: Square Every Digit

# Instructions:
'''
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.
'''

# Answer:

def square_digits(num):
    num = str(num)
    new_num = ""
    for n in num:
        squared_digit = int(n) ** 2
        new_num += (str(squared_digit))
    return int(new_num)

# Sample Tests:
'''
import codewars_test as test
from solution import square_digits

@test.describe("Premade tests: ")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(square_digits(9119), 811181)
'''