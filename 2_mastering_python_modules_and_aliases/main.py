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