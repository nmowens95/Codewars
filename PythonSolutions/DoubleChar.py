# Instructions:
'''
Given a string, you have to return a string in which each character
(case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
'''

# Solution:

def double_char(input_string):
    output_string = ""
    for char in input_string:
        output_string += char * 2
    return output_string


# Test case:
'''
test.assert_equals(double_char("String"),"SSttrriinngg")
test.assert_equals(double_char("Hello World"),"HHeelllloo  WWoorrlldd")
test.assert_equals(double_char("1234!_ "),"11223344!!__  ")
'''