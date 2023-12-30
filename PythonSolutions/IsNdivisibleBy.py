# Title: Is n divisible by (...)?

# Instructions:
'''
Create a function that checks if the first argument n is divisible by all other arguments (return true if no other arguments)

Example:

(6,1,3)--> true because 6 is divisible by 1 and 3
(12,2)--> true because 12 is divisible by 2
(100,5,4,10,25,20)--> true
(12,7)--> false because 12 is not divisible by 7
'''

# Answer:

def is_divisible(n, *args):
    for divisor in args:
        if n % divisor != 0:
            return False
    return True

# Sample Tests:
'''
import codewars_test as test
from solution import is_divisible

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(is_divisible(3,3,4),False);
        test.assert_equals(is_divisible(12,3,4),True);
        test.assert_equals(is_divisible(8,3,4,2,5),False);
        test.assert_equals(is_divisible(48,3,4,2),True);
        test.assert_equals(is_divisible(100,5,10,20,25),True);
        test.assert_equals(is_divisible(100,5),True);
        test.assert_equals(is_divisible(4,4,2,4,4,4,4,4,4),True);
        test.assert_equals(is_divisible(5,2),False);
        test.assert_equals(is_divisible(17,17,17,17),True);
        test.assert_equals(is_divisible(17,1),True);
'''