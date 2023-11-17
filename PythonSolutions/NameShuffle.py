# Title: Name Shuffle

# Instructions:
'''
Write a function that returns a string in which firstname is swapped with last name.

Example(Input --> Output)

"john McClane" --> "McClane john"

For example:

a = 1
b = 4
--> [1, 2, 3, 4]
'''

# Answer:

def name_shuffler(names):
    names = names.split()
    if len(names) >= 2:
        swapped = names[-1] + " " + names[0]
        return swapped

# Sample Tests:
'''
import codewars_test as test
from solution import name_shuffler

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(name_shuffler('john McClane'),'McClane john')
        test.assert_equals(name_shuffler('Mary jeggins'),'jeggins Mary')
        test.assert_equals(name_shuffler('tom jerry'),'jerry tom')
'''