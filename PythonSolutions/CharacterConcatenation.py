# Instructions:
'''
Given a string, you progressively need to concatenate the first letter from the left and the first letter to the right and "1", then the second letter from the left and the second letter to the right and "2", and so on.

If the string's length is odd drop the central element.

For example:

char_concat("abcdef")    == 'af1be2cd3'
char_concat("abc!def")   == 'af1be2cd3' # same result
'''

# Answer:

def char_concat(word):
    txt = ''
    for i in range(len(word) // 2):
        txt += word[i] + word[-(i + 1)] + str(i + 1)
    return txt

'''
Sample Tests:
import codewars_test as test
from solution import char_concat

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(char_concat("abc def"), 'af1be2cd3', "Should work for example test")
        test.assert_equals(char_concat("CodeWars"), 'Cs1or2da3eW4', "Should work for 'CodeWars'")
        test.assert_equals(char_concat("CodeWars Rocks"), 'Cs1ok2dc3eo4WR5a 6rs7', "Should work for two words, like 'CodeWars Rocks'")
        test.assert_equals(char_concat("1234567890"), '101292383474565', "Should work for numbers")
        test.assert_equals(char_concat("$'D8KB)%PO@s"), "$s1'@2DO38P4K%5B)6", "Should work for random strings")
'''