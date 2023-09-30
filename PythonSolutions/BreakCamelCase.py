# Instructions:

'''
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

'''

# Answer:

def solution(words):
    split = ""
    for letters in words:
        if letters.isupper():
           split += " " + letters
        else:
            split += letters
    return split

'''
Sample Tests:
test.assert_equals(solution("helloWorld"), "hello World")
test.assert_equals(solution("camelCase"), "camel Case")
test.assert_equals(solution("breakCamelCase"), "break Camel Case")
'''