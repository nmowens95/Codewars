# Instructions:
'''
Consider an array/list of sheep where some sheep may be missing from their place. 
We need a function that counts the number of sheep present in the array (true means present).
'''

# Solution:

def count_sheeps(sheep):
    count = 0
    for a in sheep:
        if a == True:
            count += 1
        elif a == False:
            pass
        else:
            pass
    return count


# Test case:
'''
import codewars_test as test
from solution import count_sheeps

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        array1 = [True,  True,  True,  False,
                  True,  True,  True,  True ,
                  True,  False, True,  False,
                  True,  False, False, True ,
                  True,  True,  True,  True ,
                  False, False, True,  True ];
        
        result = count_sheeps(array1)
        test.assert_equals(result, 17, f"There are 17 sheeps in total, not {result}")
'''