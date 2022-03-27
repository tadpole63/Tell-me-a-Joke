#tell me a joke
import random #will be crucial to telling the joke

joke_1 = "I used to work at an orange juice factory.  Yea, I got canned.  They really put the squeez on me."
joke_2 = "a ham sandwich walks into a bar and orders a beer.  The bartender says 'we dont serve food here'"
joke_3 = "What do you call an alligator detective? An investi-gator."

print("Press space to initialize the program") #explains program initilaziation to the user
user_joke = str(input("")) #allows user to initialize the program
if user_joke == " ": #command initialization selection structure
   while user_joke == " ":  #the loop allows us the option to have the user re enter the input if they give an invalid input
        print("if you want to hear a joke, enter the command 'Tell me a joke' if not, type 'No'") #explains commands to user
        user_joke = str(input("")) #prints blank space for user to enter command
        if user_joke == "Tell me a joke": #selection structure if user provides adequate command
            joke = [joke_1, joke_2, joke_3] #list of variables above for jokes.  Random module randomizes it 
            tell_a_joke = random.choice(joke) #rancom module utilized to choose a random variable to assign to "joke" and assigns it to "tell_a_joke"
            print(tell_a_joke) #prints the random joke
            break #breaks loop
        elif user_joke == "No": #if user types in the no joke command so we can have an error option for an invalid input
            print("Have a nice day!")
            break #breaks loop
        else:
            print("error code 1: invalid input")
else:
    print("error code 2")        
    

input("\n\nPress enter to exit")


    #this is a test block of code
    #to see if I can tab over multiple lines at once
    #let's see how this goes