# Title: Is He Gonna Survive

# Instructions:
'''
A hero is on his way to the castle to complete his mission. 
However, he's been told that the castle is surrounded with a couple of powerful dragons! 
each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. 
Assuming he's gonna grab a specific given number of bullets and move forward to fight another 
specific given number of dragons, will he survive?

Return true if yes, false otherwise :)
'''

# Answer:

def hero(bullets, dragons):
    if bullets >= 2 * dragons:
        return True
    return False

# Sample Tests:
'''
import codewars_test as test
from solution import hero

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(hero(10, 5), True)
'''