#Task 1 Your Mood Today
positive_mood_list = ["happy", "joyful", "pleasant", "excited", "grateful"]
negative_mood_list= ["sad", "angry", "afraid", "concerned", "tired"]

def mood_response(mood):
    global positive_mood_list
    global negative_mood_list
    if mood in positive_mood_list:
        return f"We're so glad to hear that today you are feeling {mood}!"
    elif mood in negative_mood_list:
        return f"We're so sorry to hear that today you are feeling {mood}."
    else:
        print("This is a new emotion for our system. Let's figure out how to classify it if you feel this way in the future.")
        while True:
            mood_category = input("Is this mood positive or negative? ")
            if mood_category.lower() == "positive":
                positive_mood_list.append(mood)
                return f"We're happy to hear that you feel {mood} and have added it to the positive emotion list!"
            if mood_category.lower() == "negative":
                negative_mood_list.append(mood)
                return f"We're sorry to hear you feel {mood} and have added it to the negative emotion list in case you feel this way again."
            else:
                print("Please enter a valid input, positive or negative to help educate our emotion data set.")
                continue

'''
In mood_responses.py I build the module with our mood_response function. I start by making our positive_mood_list and negative_mood_list global so if it is an emotion not already in our list it will be stored and not reinitialize each time we call our function in the main.py while loop.
Then if the mood is in positive_mood_list a return an f-string with a positive upbeat message, and if it is in negative I return an f-string that is apologetic.
In the else block if the entered mood is in neither list I inform the user that it will be added to one of these lists once they classify this mood for our system.
I then initiate a new while loop where we can define the mood as positive or negative. Based off of the reponse I then append the mood to the appropriate list and return either a positive or apologetic f-string that also informs that the feeling has been added to the appropriate list.
In the else block I print that the input was invalid and ask for a positive or negative entry to better educate the system before using the continue keyword.
'''