# Instructions:

'''
Correct this code so that it takes one argument, x, and returns "x is more than zero" 
if x is positive (and nonzero), and otherwise, returns "x is equal to or less than zero." 
In both cases, replace x with the actual value of x.
'''

# Answer:

def corrections(x):
    if x > 0:
        return str(x) + " " + "is more than zero."
    else:
        return str(x) + " " + "is equal to or less than zero."

'''
Sample Tests:
import codewars_test as test
from solution import corrections
@test.describe('Fixed Tests')
def fixed_tests():
    @test.it('Simple Cases')
    def example_cases():
        test.assert_equals(corrections(8),"8 is more than zero.")
        test.assert_equals(corrections(1),"1 is more than zero.")
        test.assert_equals(corrections(-2),"-2 is equal to or less than zero.")
        test.assert_equals(corrections(-1),"-1 is equal to or less than zero.")
        test.assert_equals(corrections(0),"0 is equal to or less than zero.")
'''