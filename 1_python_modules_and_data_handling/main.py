#Task 1 Your Mood Today

import mood_responses

while True:
    mood = input("What emotion are you feeling right now? ")
    print(mood_responses.mood_response(mood))
    more_moods = input("Would you like to continue to enter more emotions (Y or N): ")
    if more_moods.upper() == "Y":
        continue
    elif more_moods.upper() == "N":
        break
    else:
        print("Please enter Y or N, reinitializing mood input.")
        continue

'''
In this main file I import mood_responses as the module that has our mood_response function. In a while loop I ask the user to input their emotion and then print out what that motion returns when
we call the mood_response function from the mood_responses module. I then use the input more_moods to determine if we shouold continue to enter more emotions and either continue or break the loop basd off of our users
'''