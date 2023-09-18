# Instructions:
'''
Complete the function/method so that it returns the url with anything after the anchor (#) removed.

Examples
"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"
'''

# Answer:

def remove_url_anchor(url):
    new_url = ""
    for char in url:
        if char == "#":
            break
        new_url += char
    return new_url


'''
Sample Tests:
import codewars_test as test
from solution import remove_url_anchor

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(remove_url_anchor("www.codewars.com#about"), "www.codewars.com")
        test.assert_equals(remove_url_anchor("www.codewars.com/katas/?page=1#about"), "www.codewars.com/katas/?page=1")
        test.assert_equals(remove_url_anchor("www.codewars.com/katas/"), "www.codewars.com/katas/")
'''