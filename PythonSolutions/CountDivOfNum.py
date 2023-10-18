'''
Count the number of divisors of a positive integer n.

Random tests go up to n = 500000.

Examples (input --> output)
4 --> 3 // we have 3 divisors - 1, 2 and 4
5 --> 2 // we have 2 divisors - 1 and 5
12 --> 6 // we have 6 divisors - 1, 2, 3, 4, 6 and 12
30 --> 8 // we have 8 divisors - 1, 2, 3, 5, 6, 10, 15 and 30
Note you should only return a number, the count of divisors. The numbers between 
parentheses are shown only for you to see which numbers are counted in each case.
'''

# Answer:

def divisors(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += 1
    return total

'''
Sample Tests:
import codewars_test as test
from solution import divisors

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(divisors(1), 1) 
        test.assert_equals(divisors(4), 3)
        test.assert_equals(divisors(5), 2)
        test.assert_equals(divisors(12), 6)
        test.assert_equals(divisors(30), 8)
        test.assert_equals(divisors(4096), 13)
'''