# Instructions:
'''
Story
Ben has a very simple idea to make some profit: he buys something and 
sells it again. Of course, this wouldn't give him any profit at all if 
he was simply to buy and sell it at the same price. Instead, he's going 
to buy it for the lowest possible price and sell it at the highest.

Task
Write a function that returns both the minimum and maximum number of the given list/array.

Examples (Input --> Output)
[1,2,3,4,5] --> [1,5]
[2334454,5] --> [5,2334454]
[1]         --> [1,1]
'''

# Answer:

def min_max(lst):
    return [min(lst), max(lst)]

'''
import codewars_test as test
from solution import min_max

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(min_max([1,2,3,4,5]), [1, 5])
        test.assert_equals(min_max([2334454,5]), [5, 2334454])
'''