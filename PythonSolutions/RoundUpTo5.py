# Title: Round up to the next multiple of 5

# Instructions:
'''
Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?

Examples:

input:    output:
0    ->   0
2    ->   5
3    ->   5
12   ->   15
21   ->   25
30   ->   30
-2   ->   0
-5   ->   -5
etc.
Input may be any positive or negative integer (including 0).

You can assume that all inputs are valid integers.
'''

# Answer:

def round_to_next5(n):
    quotient = n // 5
    remainder = n % 5
    if remainder != 0:
        n = (quotient * 5) + 5
    return n

# Sample Tests:
'''
inp = 0
out = round_to_next5(inp)
test.assert_equals(out, 0, "Input: {}".format(inp))

inp = 1
out = round_to_next5(inp)
test.assert_equals(out, 5, "Input: {}".format(inp))

inp = -1
out = round_to_next5(inp)
test.assert_equals(out, 0, "Input: {}".format(inp))

inp = 5
out = round_to_next5(inp)
test.assert_equals(out, 5, "Input: {}".format(inp))

inp = 7
out = round_to_next5(inp)
test.assert_equals(out, 10, "Input: {}".format(inp))

inp = 20
out = round_to_next5(inp)
test.assert_equals(out, 20, "Input: {}".format(inp))

inp = 39
out = round_to_next5(inp)
test.assert_equals(out, 40, "Input: {}".format(inp))
'''