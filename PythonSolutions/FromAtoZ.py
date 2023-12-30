# Title: From A to Z

# Instructions:
'''
Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

Examples
"a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
"h-o" ➞ "hijklmno"
"Q-Z" ➞ "QRSTUVWXYZ"
"J-J" ➞ "J"
'''

# Answer:

def gimme_the_letters(letters):
    start = ord(letters[0])
    end = ord(letters[2])
    string = ''
    for i in range(start, end + 1):
        string += chr(i)
    return string

# Sample Tests:
'''
import codewars_test as test
from solution import gimme_the_letters

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(gimme_the_letters("a-z"), "abcdefghijklmnopqrstuvwxyz")
        test.assert_equals(gimme_the_letters("h-o"), "hijklmno")
        test.assert_equals(gimme_the_letters("Q-Z"), "QRSTUVWXYZ")
        test.assert_equals(gimme_the_letters("J-J"), "J")
        test.assert_equals(gimme_the_letters("a-b"), "ab")
        test.assert_equals(gimme_the_letters("A-A"), "A")
        test.assert_equals(gimme_the_letters("g-i"), "ghi")
        test.assert_equals(gimme_the_letters("H-I"), "HI")
        test.assert_equals(gimme_the_letters("y-z"), "yz")
        test.assert_equals(gimme_the_letters("e-k"), "efghijk")
        test.assert_equals(gimme_the_letters("a-q"), "abcdefghijklmnopq")
        test.assert_equals(gimme_the_letters("F-O"), "FGHIJKLMNO")   
'''