# Instructions:
'''
Create a method that takes as input a name, city, and state to welcome a person. 
Note that name will be an array consisting of one or more values that should be joined
together with one space between each, and the length of the name array in test cases will vary.
'''
# This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!

# Answer:

def say_hello(name, city, state):
    names = " ".join(name)
    return (f"Hello, {names}! Welcome to {city}, {state}!")

# Used "".join() to seperate the names, then used the f string to enter the variables, passing all test cases

'''
Sample Tests:
import codewars_test as test
from solution import say_hello

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'), 'Hello, John Smith! Welcome to Phoenix, Arizona!')
        test.assert_equals(say_hello(['Franklin','Delano','Roosevelt'], 'Chicago', 'Illinois'), 'Hello, Franklin Delano Roosevelt! Welcome to Chicago, Illinois!')
        test.assert_equals(say_hello(['Wallace','Russel','Osbourne'],'Albany','New York'), 'Hello, Wallace Russel Osbourne! Welcome to Albany, New York!')
        test.assert_equals(say_hello(['Lupin','the','Third'],'Los Angeles','California'), 'Hello, Lupin the Third! Welcome to Los Angeles, California!')
        test.assert_equals(say_hello(['Marlo','Stanfield'],'Baltimore','Maryland'), 'Hello, Marlo Stanfield! Welcome to Baltimore, Maryland!')
'''