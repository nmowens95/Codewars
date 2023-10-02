# Title: Reverse Words

# Instructions:
'''
Complete the function that accepts a string parameter, 
and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''

# Answer:
def reverse_words(text):
    reversed = []
    text = text.split(" ")
    for words in text:
        words = words[::-1]
        reversed.append(words)
    return " ".join(reversed)


# Sample Tests
'''
import codewars_test as test
from solution import reverse_words

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')
        test.assert_equals(reverse_words('apple'), 'elppa')
        test.assert_equals(reverse_words('a b c d'), 'a b c d')
        test.assert_equals(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')
'''