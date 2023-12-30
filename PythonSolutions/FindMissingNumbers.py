'''
You will get an array of numbers.

Every preceding number is smaller than the one following it.

Some numbers will be missing, for instance:

[-3,-2,1,5] //missing numbers are: -1,0,2,3,4
Your task is to return an array of those missing numbers:

[-1,0,2,3,4]
'''

# Answer:

def find_missing_numbers(arr):
    return [x for x in range(arr[0], arr[-1]+1) if x not in arr] if arr else []
'''
Sample Tests:
import codewars_test as test
from solution import find_missing_numbers

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_missing_numbers([-3,-2,1,4]), [-1,0,2,3])
        test.assert_equals(find_missing_numbers([-1,0,1,2,3,4]), [])
        test.assert_equals(find_missing_numbers([]), [])
        test.assert_equals(find_missing_numbers([0]), [])
        test.assert_equals(find_missing_numbers([-4,4]), [-3,-2,-1,0,1,2,3])
'''