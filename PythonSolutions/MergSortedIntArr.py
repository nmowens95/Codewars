# Title: Merging sorted integer arrays (without duplicates)

# Instructions:
'''
Write a function that merges two sorted arrays into a single one. 
The arrays only contain integers. Also, the final outcome must be sorted and not have any duplicate.
'''

# Answer:

# simple short answer
def merge_arrays(first, second): 
    new_arr = set(first + second)
    return sorted(new_arr)

# Sample Tests:
'''
test.describe('Example Tests')
def example_tests():
    test.assert_equals(merge_arrays([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])        
    test.assert_equals(merge_arrays([2, 4, 8], [2, 4, 6]), [2, 4, 6, 8])  
'''