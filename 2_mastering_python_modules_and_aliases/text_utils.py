#Task 1 Custom Module With Alias

def reverse_string(s):
    reversed_str = s[::-1]
    return reversed_str

def capitalize_string(s):
    capital_str = s.title()
    return capital_str

'''
I define two functions we will call in the main.py file from this text_utils.py module. In reverse_string(s) for the string s we assign a new variable reversed_str which will be the string s using the slice [::-1] to
slice through by a -1 step starting at the last character and ending with the first. This new variable is then returned from the function. In capitalize_string(s) I assign the variable capital_str which is the input string s after the built-in titlecase method has been applied.
I then return the new capital_str string.
'''