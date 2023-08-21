# Instructions:
'''
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59
'''

# Solution:

def past(h, m, s):
    result = 0
    if 0 <= h <= 23:
        result += (h * 60 * 60) * 1000
    if 0 <= m <= 59:
        result += (m * 60) * 1000
    if 0 <= s <= 59:
        result += s * 1000
    return result


# Test case:
'''
import codewars_test as test
from solution import past

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(past(0,1,1),61000)
        test.assert_equals(past(1,1,1),3661000)
        test.assert_equals(past(0,0,0),0)
        test.assert_equals(past(1,0,1),3601000)
        test.assert_equals(past(1,0,0),3600000)
'''