# Instructions:
'''
You'll be given a list of two strings, and each will contain exactly one colon (":")
in the middle (but not at beginning or end). The length of the strings, before and after the colon, are random.
Your job is to return a list of two strings (in the same order as the original list), but with the characters after each colon swapped.
'''

# Solution:

def tail_swap(strings):
    head0, tail0 = strings[0].split(":")
    head1, tail1 = strings[1].split(":")
    return [head0 + ':' + tail1, head1 + ':' + tail0]


# Test case:
'''
import codewars_test as test
from solution import tail_swap

sample_test_cases = [
#     strings                 expected
    (['abc:123', 'cde:456'], ['abc:456', 'cde:123']),
    (['a:12345', '777:xyz'], ['a:xyz'  , '777:12345']),
]

@test.describe('Sample tests')
def sample_tests():
    @test.it('')
    def _():
        for strings, expected in sample_test_cases:
            msg = f'tail_swap({strings!r})'
            test.assert_equals(tail_swap(strings), expected, msg)
'''