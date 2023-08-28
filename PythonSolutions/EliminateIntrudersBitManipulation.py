# Instructions:
'''
You are given a string representing a number in binary. Your task is to delete all the 
unset bits in this string and return the corresponding number (after keeping only the '1's).

In practice, you should implement this function:

def eliminate_unset_bits(number):
Examples
eliminate_unset_bits("11010101010101") ->  255 (= 11111111)
eliminate_unset_bits("111") ->  7
eliminate_unset_bits("1000000") -> 1
eliminate_unset_bits("000") -> 0
'''

# Solution:

def eliminate_unset_bits(number):
    return 2 ** (number.count("1")) - 1


# Test case:
'''
from solution import eliminate_unset_bits
import codewars_test as test

@test.describe("Example tests")
def _():
    @test.it("Tests")
    def __():
        test.assert_equals(eliminate_unset_bits("11010101010101"), 255)
        test.assert_equals(eliminate_unset_bits("111"), 7)
        test.assert_equals(eliminate_unset_bits("1000000"), 1)
        test.assert_equals(eliminate_unset_bits("000"), 0)
'''