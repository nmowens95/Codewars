'''
Given a number return the closest number to it that is divisible by 10.

Example input:

22
25
37
Expected output:

20
30
40
'''

# Answer:

def closest_multiple_10(num):
    diff = num % 10
    if diff < 5:
        return num - diff
    return num + (10 - diff)


'''
Sample Tests:
from solution import closest_multiple_10
import codewars_test as test

@test.describe('closest_multiple_10')
def _():
    @test.it('sample tests')
    def _():
        test.assert_equals(closest_multiple_10(54), 50)
        test.assert_equals(closest_multiple_10(55), 60)
'''