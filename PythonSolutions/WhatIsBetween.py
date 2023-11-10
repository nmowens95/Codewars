# Title: What is between?

# Instructions:
'''
WComplete the function that takes two integers (a, b, where a < b) 
and return an array of all integers between the input parameters, including them.

For example:

a = 1
b = 4
--> [1, 2, 3, 4]
'''

# Answer:

def between(a,b):
    new_arr = []
    for num in range(a, b + 1):
        new_arr.append(num)
    return new_arr

# Sample Tests:
'''
import codewars_test as test
from solution import between

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(between(1, 4), [1, 2, 3, 4])
        test.assert_equals(between(-2, 2), [-2, -1, 0, 1, 2])
'''