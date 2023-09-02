# Instructions:
'''
Check to see if a string has the same amount of 'x's and 'o's. The method must return 
a boolean and be case insensitive. The string can contain any char.
'''

# Solution:

def xo(string):
    string = string.lower()
    
    count_x = string.count("x")
    count_o = string.count("o")
    
    return count_x == count_o


# Test case:
'''
import codewars_test as test
from solution import xo

@test.describe("Sample tests")
def _():
    test_cases = [
        ("ooxx",    True),
        ("xooxx",   False),
        ("ooxXm",   True), # Comparison is case-insensitive
        ("zpzpzpp", True), # when no 'x' and 'o' is present should return true
        ("zzoo",    False),
        ("oxOx",    True),
        ("",        True),  # Empty string contains equal amount of x and o
    ]
    for s, expected in test_cases:
        @test.it(f"{s = }")
        def _():
            test.assert_equals(xo(s), expected)
'''