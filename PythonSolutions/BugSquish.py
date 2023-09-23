'''
Take debugging to a whole new level:

Given a string, remove every single bug.

This means you must remove all instances of the word 'bug' from within a given string, unless the word is plural ('bugs').

For example, given 'obugobugobuoobugsoo', you should return 'ooobuoobugsoo'.

Another example: given 'obbugugo', you should return 'obugo'.

Note that all characters will be lowercase.

Happy squishing!
'''

# Answer:

def debug(input_str):
    result = []
    i = 0
    while i < len(input_str):
        if input_str[i:i+3] == 'bug':
            if i + 3 < len(input_str) and input_str[i+3] == 's':
                result.append('bugs')
                i += 4  # Skip 'bugs'
            else:
                i += 3  # Skip 'bug'
        else:
            result.append(input_str[i])
            i += 1

    return ''.join(result)

'''
Sample Tests:
import codewars_test as test
from solution import debug

sample_test_cases = [
    ('obugobugobuoobugsoo', 'ooobuoobugsoo'),
    ('obbugugo', 'obugo'),
    ('bugs bunny', 'bugs bunny'),
    ('bugs buggy', 'bugs gy'),
]

@test.describe('Sample tests')
def sample_tests():
    for s, expected in sample_test_cases:
        @test.it(f'debug({s!r})')
        def _():
            test.assert_equals(debug(s), expected)
'''