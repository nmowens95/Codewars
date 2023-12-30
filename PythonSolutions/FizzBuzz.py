# Title: Fizz Buzz

# Instructions:
'''
Return an array containing the numbers from 1 to N, where N is the parametered value.

Replace certain values however if any of the following conditions are met:

If the value is a multiple of 3: use the value "Fizz" instead
If the value is a multiple of 5: use the value "Buzz" instead
If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead
N will never be less than 1.

Method calling example:

fizzbuzz(3) -->  [1, 2, "Fizz"]
'''

# Answer:

def fizzbuzz(nums):
    the_buzz = []
    for num in range(1, nums + 1):
        if num % 5 == 0 and num % 3 == 0:
            the_buzz.append("FizzBuzz")
        elif num % 3 == 0:
            the_buzz.append("Fizz")
        elif num % 5 == 0:
            the_buzz.append("Buzz")
        else:
            the_buzz.append(num)
    return the_buzz

# Sample Tests:
'''
import codewars_test as test
from solution import fizzbuzz

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Should fizzify 10 numbers correctly')
    def basic_test_cases():
        expected = [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz']
        test.assert_equals(fizzbuzz(10), expected, 'Fails with 10 numbers!')

    @test.it('Should fizzify 30 numbers correctly')
    def basic_test_cases():
        expected = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz"]
        test.assert_equals(fizzbuzz(30), expected, 'Fails with 30 numbers!')

    @test.it('Should fizzify 1 number correctly')
    def basic_test_cases():
        expected = [1]
        test.assert_equals(fizzbuzz(1), expected, 'Fails with 1 number!')

    @test.it('Should fizzify 100 numbers correctly')
    def basic_test_cases():
        expected = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz", "Fizz", 52, 53, "Fizz", "Buzz", 56, "Fizz", 58, 59, "FizzBuzz", 61, 62, "Fizz", 64, "Buzz", "Fizz", 67, 68, "Fizz", "Buzz", 71, "Fizz", 73, 74, "FizzBuzz", 76, 77, "Fizz", 79, "Buzz", "Fizz", 82, 83, "Fizz", "Buzz", 86, "Fizz", 88, 89, "FizzBuzz", 91, 92, "Fizz", 94, "Buzz", "Fizz", 97, 98, "Fizz", "Buzz"]
        test.assert_equals(fizzbuzz(100), expected, 'Fails with 100 numbers!') 
'''