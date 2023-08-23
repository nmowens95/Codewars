# Instructions:
'''
Given a random non-negative number, you have to return 
the digits of this number within an array in reverse order.
'''

# Solution:

def digitize(n):
    return [int(x) for x in str(n)[::-1]]

# Notes:
''' 
We stringified the digits so instead of working with a whole number, we can
access the individual digits. From there we wanted to reverse those digits.
We then use a list comprehension converting each letter to an int.
'''

# Test case:
'''
import codewars_test as test
from solution import digitize

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(digitize(35231),[1,3,2,5,3])
        test.assert_equals(digitize(0),[0])
        test.assert_equals(digitize(23582357),[7,5,3,2,8,5,3,2])
        test.assert_equals(digitize(984764738),[8,3,7,4,6,7,4,8,9])
        test.assert_equals(digitize(45762893920),[0,2,9,3,9,8,2,6,7,5,4])
        test.assert_equals(digitize(548702838394),[4,9,3,8,3,8,2,0,7,8,4,5])
'''