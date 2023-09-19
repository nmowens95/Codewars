'''
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. 
They would like your help with an application form that will tell prospective members 
which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 
7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input
Input will consist of a list of pairs. Each pair contains information for a single potential member. 
Information consists of an integer for the person's age and an integer for the person's handicap.

'''

# Answer:

def open_or_senior(data):
    return ["Senior" if age >= 55 and handicap > 7 else "Open" for age, handicap in data]

'''
Sample Tests:
import codewars_test as test
from solution import open_or_senior

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():    
        test.assert_equals(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]),['Open', 'Senior', 'Open', 'Senior'])
        test.assert_equals(open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)]),['Open', 'Open', 'Senior', 'Open'])
'''