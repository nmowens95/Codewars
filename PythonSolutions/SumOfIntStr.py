# Title: Sum of integers in string

# Instructions:
'''
Your task in this kata is to implement a function that 
calculates the sum of the integers inside a string. For example, 
in the string "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", 
the sum of the integers is 3635.

Note: only positive integers will be tested.
'''

# Answer:

def sum_of_integers_in_string(input_str):
    sum_of_integers = 0
    current_number = ''
    for char in input_str:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                sum_of_integers += int(current_number)
                current_number = ''
    if current_number:
        sum_of_integers += int(current_number)
    return sum_of_integers

# Sample Tests:
'''
import codewars_test as test
from solution import sum_of_integers_in_string

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        exampleTests = (
        ("12.4", 16),
        ("h3ll0w0rld", 3),
        ("2 + 3 = ", 5),
        ("Our company made approximately 1 million in gross revenue last quarter.", 1),
        ("The Great Depression lasted from 1929 to 1939.", 3868),
        ("Dogs are our best friends.", 0),
        ("C4t5 are 4m4z1ng.", 18),
        ("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", 3635)
        )

        for testString, correctAnswer in exampleTests:
            test.assert_equals(sum_of_integers_in_string(testString), correctAnswer)
'''