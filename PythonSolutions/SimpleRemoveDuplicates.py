# Title: Simple Remove Duplicates

# Instructions:
'''
Remove the duplicates from a list of integers, keeping the last ( rightmost ) occurrence of each element.

Example:
For input: [3, 4, 4, 3, 6, 3]

remove the 3 at index 0
remove the 4 at index 1
remove the 3 at index 3
Expected output: [4, 6, 3]
'''

# Answer:

def solve(arr): 
    last_occurrences = {}
    result = []

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] not in last_occurrences:
            last_occurrences[arr[i]] = i

    for element, index in last_occurrences.items():
        result.append(element)

    result.reverse()
    return result

# Sample Tests:
'''
import codewars_test as test
from solution import solve


@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(solve([3,4,4,3,6,3]),[4,6,3])
        test.assert_equals(solve([1,2,1,2,1,2,3]),[1,2,3])
        test.assert_equals(solve([1,2,3,4]),[1,2,3,4])
        test.assert_equals(solve([1,1,4,5,1,2,1]),[4,5,2,1])
'''