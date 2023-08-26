# Instructions:
'''
This function should test if the factor is a factor of base.
Return true if it is a factor or false if it is not.
'''

# Answer:

def check_for_factor(base, factor):
    if base % factor == 0:
        return True
    return False

'''
Sample Tests:
import codewars_test as test
from solution import check_for_factor

@test.describe("Fixed Tests")
def fixed_tests():    
    @test.it("Should return True")
    def should_return_true():
        test.assert_equals(check_for_factor(10, 2), True)
        test.assert_equals(check_for_factor(63, 7), True)
        test.assert_equals(check_for_factor(2450, 5), True)
        test.assert_equals(check_for_factor(24612, 3), True)
        
    @test.it("Should return False")
    def should_return_false():
        test.assert_equals(check_for_factor(9, 2), False)
        test.assert_equals(check_for_factor(653, 7), False)
        test.assert_equals(check_for_factor(2453, 5), False)
        test.assert_equals(check_for_factor(24617, 3), False)
'''