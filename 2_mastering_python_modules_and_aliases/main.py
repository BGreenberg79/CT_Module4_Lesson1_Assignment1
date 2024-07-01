#Task 1 Custom Module With Alias

import text_utils as tu

while True:
    custom_string = input("Enter a custom message: ")
    transformation = input("Do you want to reverse your message or capitalize it: ")
    if transformation.lower() == "capitalize":
        print(tu.capitalize_string(custom_string))
    elif transformation.lower() == "reverse":
        print(tu.reverse_string(custom_string))
    else:
        print("Invalid input. Please enter reverse or capitalize")
    cont_string = input("Enter another message? (Y or N): ")
    if cont_string.upper() == "Y":
        continue
    elif cont_string.upper() == "N":
        break
    else:
        print("Invalid input, reinitializing program")
        continue

'''
I start off this main file by importing the text_utils module and aliasing as it's initials tu. Then in a while loop I take inputs for a custom string as the argument we will run through our functions and transformation to decide which function to call.
If the transformation input is capitalize I call within a print statement the capitalize_string function from the tu alias module with custom_string passed through. In an elif statement if the input is reverse I similarly call from the tu alias module the reverse_string function with custom string as argument inside a print statement.
If neither capitalize or reverse is given as the transformation input I use an else statement to print that the input was invalid. I then use a cont_string input variable to ask the user if they would like to add another message.
If they input "Y" we use the continue keyword, elif if they enter "N" we break, and in an else statement I print that the response was invalid and that I am reinitializing the program folllowed by the continue keyword again.
'''