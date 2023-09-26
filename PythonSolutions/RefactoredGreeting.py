'''
The following code could use a bit of object-oriented artistry. While it's a simple method and works just fine as it is, in a larger system it's best to organize methods into classes/objects. (Or, at least, something similar depending on your language)

Refactor the following code so that it belongs to a Person class/object. Each Person instance will have a greet method. The Person instance should be instantiated with a name so that it no longer has to be passed into each greet method call.

Here is how the final refactored code would be used:

joe = Person('Joe')
joe.greet('Kate') # should return 'Hello Kate, my name is Joe'
joe.name          # should == 'Joe'
'''

# Answer:

class Person():
    def __init__(self, name):
        self.name = name
    
    
    def greet(self, your_name):
        return f'Hello {your_name}, my name is {self.name}'

'''
Sample Tests:
import codewars_test as test
from solution import *

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        jack = Person("Jack")
        jill = Person("Jill")

        test.assert_equals(jack.greet("Jill"), "Hello Jill, my name is Jack")
        test.assert_equals(jack.greet("Mary"), "Hello Mary, my name is Jack")

        test.assert_equals(jill.greet("Jack"), "Hello Jack, my name is Jill")
        test.assert_equals(jill.name, 'Jill', "Person's name could not be retrieved")
'''