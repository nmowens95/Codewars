# Title: Boiled Eggs

# Instructions:
'''
You are the greatest chef on earth. No one boils eggs like you! Your restaurant is always full of guests, who love your boiled eggs. But when there is a greater order of boiled eggs, you need some time, because you have only one pot for your job. How much time do you need?

Your Task
Implement a function, which takes a non-negative integer, representing the number of eggs to boil. It must return the time in minutes (integer), which it takes to have all the eggs boiled.

Rules
you can put at most 8 eggs into the pot at once
it takes 5 minutes to boil an egg
we assume, that the water is boiling all the time (no time to heat up)
for simplicity we also don't consider the time it takes to put eggs into the pot or get them out of it
Example (Input --> Output)
0 --> 0
5 --> 5
10 --> 10

'''

# Answer:

def cooking_time(eggs):
    batches = (eggs + 7) // 8
    
    # Calculate the total time (5 minutes per egg per batch)
    time = batches * 5
    
    return time

# Sample Tests:
'''
import codewars_test as test
from solution import cooking_time

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals( cooking_time(0), 0 )
        test.assert_equals( cooking_time(5), 5 )
        test.assert_equals( cooking_time(10), 10 )
'''